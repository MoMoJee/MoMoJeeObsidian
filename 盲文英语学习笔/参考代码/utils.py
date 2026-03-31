from typing import Dict
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt


class Filters:
    # TODO 给各个预处理结果生成图片示意怎么处理的 比如中值化就应该是绕在一起的一条线
    def __init__(self, input_length: int=200, step_size: int=20):
        self.input_length = input_length
        self.step_size = step_size
        self.filters = {
            'default': self.default_filter,
            'normalize': self.normalize_filter,
            'standardize': self.standardize_filter,
            'uni_baseline': self.uni_baseline_filter,
            'uni_baseline_std': self.uni_baseline_std_filter,
            'diff': self.diff_filter,
            'reverse_time': self.reverse_time_filter,
            'adjust_window': self.adjust_window_filter_path,
            'zoom': self.zoom_filter,
        }

    def _prepare_data(self, file_path: str = None)->Dict[str, pd.DataFrame]:
        """

        :param file_path: csv文件路径
        :return: {"chunk_id":, chunk 的 data(pd.DataFrame)} 的字典
        """

        if not file_path:
            raise ValueError(f"未指定csv文件地址")

        df = pd.read_csv(file_path).drop(columns=['Time (s)']).values
        total_samples = df.shape[0]
        num_samples_per_chunk = self.input_length
        step_size = self.step_size
        data = {}

        # 计算可以创建的chunk数量
        num_chunks = max(0, (total_samples - num_samples_per_chunk) // step_size + 1)

        for chunk_idx in range(num_chunks):
            start_idx = chunk_idx * step_size
            end_idx = start_idx + num_samples_per_chunk
            chunk = df[start_idx:end_idx]

            # 如果chunk的长度小于要求的samples per chunk，跳过
            if len(chunk) < num_samples_per_chunk:
                continue

            data[f'{start_idx}_{end_idx}'] = chunk

        if not data:
            raise ValueError(f'文件{file_path}中未找到数据或数据长度小于输入长度(即每个 num_samples_per_chunk 的样本数): {num_samples_per_chunk}')
        return data

    def default_filter(self, data_path: str):
        # data = pd.read_csv(data_path, nrows=200).drop(columns=['Time (s)']).values
        # 最原始的实现
        data = self._prepare_data(file_path=data_path)
        return data

    def normalize_filter(self, data_path: str):
        """
        中值化，将输入数据的平均值化为 0

        :param data_path: 文件地址
        :return: 预处理好的数据
        """
        raw_data = self._prepare_data(file_path=data_path)
        data = {}

        for chunk_idx, chunk in raw_data.items():
            mean = np.mean(chunk, axis=0)
            values = chunk - mean
            data[chunk_idx] = values

        return data

    def standardize_filter(self, data_path: str):
        """
        标准化

        将输入数据的方差化为 1

        :param data_path: 文件地址

        :return: 预处理好的数据

        """

        raw_data = self._prepare_data(file_path=data_path)
        data = {}

        for chunk_idx, chunk in raw_data.items():
            mean = np.mean(chunk, axis=0)
            std_for_mean = np.std(chunk, axis=0)
            values = (chunk - mean) / std_for_mean
            data[chunk_idx] = values

        return data

    def uni_baseline_filter(self, data_path: str, _left_margin: int | None, _right_margin: int | None,
                            _vibration_threshold: int | None = 10,
                            _extra_std: bool = False,):
        """
        统一基线标准化，处理"平静基线上突然被按下去一小段又回复"的情形
        先计算列数据的平静初始值、平静结束值的平均值作为初始值
        再用将其基线平移为 0 的方式将整列数据平移

        :param _extra_std: uni_baseline_std_filter 用，True则在统一基线后再加一次标准化
        :param data_path: 文件路径
        :param _left_margin: 左侧被视为稳定值的数据个数，缺省为 10
        :param _right_margin: 右侧被视为稳定值的数据个数，缺省为 10
        :param _vibration_threshold: 界定是波动 or 稳定 的数据波动阈值（差分）
        若不为 None 则 _left_margin 和 _right_margin 将无效
        直接程序以阈值界定当前数据是否为"波动"来决定"基线"。
        当差分绝对值大于阈值时说明"被按下了"或者"松回来了"

        :return: 处理好的数据
        """
        import warnings  # 添加warnings模块导入

        raw_data = self._prepare_data(file_path=data_path)
        data = {}
        # print(f"————开始对 {data_path} 的数据进行统一基线标准化处理————")

        # 设置默认值
        if _left_margin is None:
            _left_margin = 10
        if _right_margin is None:
            _right_margin = 10

        for chunk_idx, chunk in raw_data.items():
            chunk_array = np.array(chunk)
            baseline_values = []
            chunk_valid = True  # 标记这个chunk是否有效

            # 对每一列单独处理
            for col_idx in range(chunk_array.shape[1]):
                column_data = chunk_array[:, col_idx]

                if _vibration_threshold is not None:
                    # 基于振动阈值的模式
                    # 计算差分
                    diff_data = np.abs(np.diff(column_data))

                    # 找到稳定区域的开始和结束位置
                    # 稳定区域：连续的差分值都小于阈值
                    stable_mask = diff_data < _vibration_threshold

                    # 找到从开头开始的连续稳定区域（左侧基线）
                    left_stable_end = 0
                    for i in range(len(stable_mask)):
                        if stable_mask[i]:
                            left_stable_end = i + 1  # +1因为diff比原数据少一个元素
                        else:
                            break

                    # 找到从末尾开始的连续稳定区域（右侧基线）
                    right_stable_start = len(column_data)
                    for i in range(len(stable_mask) - 1, -1, -1):
                        if stable_mask[i]:
                            right_stable_start = i + 1  # +1因为diff比原数据少一个元素
                        else:
                            break

                    # 检查基线检测的有效性
                    has_left_baseline = left_stable_end > 0
                    has_right_baseline = right_stable_start < len(column_data)
                    has_transition = left_stable_end < right_stable_start  # 中间是否有突变区域

                    # 基线检测失败的情况：
                    # 1. 全部都是平静数据（没有突变）
                    # 2. 只有左侧基线，没有右侧基线（只下降不回升）
                    # 3. 只有右侧基线，没有左侧基线（从突变开始）
                    if not has_transition:
                        # 全部都是平静数据
                        warnings.warn(
                            f"Chunk {chunk_idx} Column {col_idx + 1}: 检测到全部为平静数据，无明显突变。此chunk将被丢弃。")
                        chunk_valid = False
                        break
                    elif has_left_baseline and not has_right_baseline:
                        # 只有左侧基线，数据下降后没有回升
                        warnings.warn(
                            f"Chunk {chunk_idx} Column {col_idx + 1}: 检测到数据下降后未回升到基线水平。此chunk将被丢弃。")
                        chunk_valid = False
                        break
                    elif not has_left_baseline and has_right_baseline:
                        # 只有右侧基线，从突变状态开始
                        warnings.warn(
                            f"Chunk {chunk_idx} Column {col_idx + 1}: 检测到数据从突变状态开始。此chunk将被丢弃。")
                        chunk_valid = False
                        break
                    elif not has_left_baseline and not has_right_baseline:
                        # 没有检测到任何基线
                        warnings.warn(f"Chunk {chunk_idx} Column {col_idx + 1}: 未检测到有效基线区域。此chunk将被丢弃。")
                        chunk_valid = False
                        break

                    # 提取左右基线区域的数据
                    baseline_points = []
                    if has_left_baseline:
                        baseline_points.extend(column_data[:left_stable_end])
                    if has_right_baseline:
                        baseline_points.extend(column_data[right_stable_start:])

                    baseline = np.mean(baseline_points)

                else:
                    # 基于边距的模式（不需要额外验证，因为总是能取到边距数据）
                    # 取左侧和右侧的稳定值
                    left_values = column_data[:_left_margin]
                    right_values = column_data[-_right_margin:]

                    # 计算左右两端的平均值作为基线
                    baseline = (np.mean(left_values) + np.mean(right_values)) / 2

                baseline_values.append(baseline)

            # 只有当chunk有效时才加入结果
            if chunk_valid:
                # 将基线数组转换为与chunk相同形状，用于广播运算
                baseline_array = np.array(baseline_values)

                # 执行基线平移，使基线为0
                normalized_chunk = chunk_array - baseline_array

                if _extra_std:
                    std_for_mean = np.std(normalized_chunk, axis=0)
                    normalized_chunk = normalized_chunk / std_for_mean

                data[chunk_idx] = normalized_chunk

            else:
                # chunk无效时的额外信息
                start_idx, end_idx = chunk_idx.split('_')
                print(f"警告：Chunk {chunk_idx} (数据范围 {start_idx}-{end_idx}) 已被丢弃，因为无法检测到有效的基线模式。")

        if len(data) == 0:
            warnings.warn("所有数据块都被丢弃，无有效数据返回。请检查数据质量或调整振动阈值参数。")

        # print(f"————对 {data_path} 的统一基线标准化处理数据处理结束————")
        return data

    def uni_baseline_std_filter(self, data_path: str, _left_margin: int | None, _right_margin: int | None,
                            _vibration_threshold: int | None = 10):

        uni_data = self.uni_baseline_filter(data_path=data_path, _left_margin=_left_margin, _right_margin=_right_margin, _vibration_threshold=_vibration_threshold, _extra_std=True)
        return uni_data

    def diff_filter(self, data_path: str):
        # TODO 我根本没改好这个函数，别用！
        df = pd.read_csv(data_path, nrows=201)
        time_col = df['Time (s)'].values
        df = df.drop(columns=['Time (s)'])
        values = df.values

        values = np.diff(values, axis=0)
        time_col = time_col[1:]  # 差分后时间列长度减1
        return values

    def reverse_time_filter(self, data_path: str):
        """
        时序倒置处理。这个只用于训练数据增强
        :param data_path:
        :return:
        """
        raw_data = self._prepare_data(file_path=data_path)
        reversed_data = {}

        for chunk_idx, chunk in raw_data.items():
            chunk_row_reversed = chunk[::-1]
            reversed_data[chunk_idx] = chunk_row_reversed

        return reversed_data

    @staticmethod
    def _adjust_window_size(_chunk, current_size, target_size):
        """
        调整窗口大小到目标大小

        :param _chunk: 当前窗口数据
        :param current_size: 当前窗口大小
        :param target_size: 目标窗口大小
        :return: 调整后的窗口数据
        """
        if current_size == target_size:
            return _chunk

        # 创建新的索引
        original_indices = np.arange(current_size)
        # 按比例缩放索引
        scaled_indices = np.linspace(0, current_size - 1, target_size)

        # 对每个特征进行插值
        interpolated_data = np.array([
            np.interp(scaled_indices, original_indices, feature)
            for feature in _chunk.T
        ]).T

        return interpolated_data


    def adjust_window_filter_path(self, data_path: str, target_chunk_size: int):
        """
        窗口长度（时序）缩放预处理（单个文件->数据），仅用于训练数据增强
        将当前定义的 self.input_length 长度的每个 chunk 的数据调整到 target_chunk_size 定义的每个 chunk 长度的数据

        :param data_path:
        :param target_chunk_size: 要调整到的目标窗口大小
        :return: {chunk_idx: adjusted_chunk} 形状的字典
        """

        raw_data = self._prepare_data(file_path=data_path)
        adjusted_data = {}

        for chunk_idx, chunk in raw_data.items():
            adjusted_chunk = self._adjust_window_size(_chunk=chunk, current_size=self.input_length, target_size=target_chunk_size)
            adjusted_data[chunk_idx] = adjusted_chunk

        return adjusted_data

    def adjust_window_filter_data(self, data: Dict[str, np.ndarray], target_chunk_size: int):
        """
        :param data:
        :param target_chunk_size:
        :return:
        """

        adjusted_data = {}
        for chunk_idx, chunk in data.items():
            adjusted_chunk = self._adjust_window_size(_chunk=chunk, current_size=self.input_length, target_size=target_chunk_size)
            adjusted_data[chunk_idx] = adjusted_chunk

        return adjusted_data


    def zoom_filter(self, data_path: str, zoom_factor: float):
        raw_data = self._prepare_data(file_path=data_path)
        zoomed_data = {}
        for chunk_idx, chunk in raw_data.items():
            zoomed_values = chunk.astype(np.float64) * np.float64(zoom_factor)
            zoomed_data[chunk_idx] = zoomed_values

        return zoomed_data



    def plot_lines(self, values: np.ndarray):
        """
        绘制多条曲线图，横坐标是200个值，纵坐标是各列的处理后数据。

        Args:
            values (np.ndarray): 处理后的数据，形状为 (200, 4)
        """
        # 创建横坐标（0到199）
        x = np.arange(values.shape[0])

        # 绘制每列数据的曲线
        plt.figure(figsize=(12, 8))

        for i in range(values.shape[1]):
            plt.plot(x, values[:, i], label=f'Column {i + 1}')

        # 添加标题和标签
        plt.title('Processed Data Across 200 Samples')
        plt.xlabel('Sample Index')
        plt.ylabel('Value')
        plt.legend()
        plt.grid(True)
        plt.show()







def test_uni_baseline_filter_chunks():
    # 测试代码
    import tempfile
    import os

    # 创建更长的测试数据：100个平静值 + 10个突变 + 100个平静值
    time_data = np.arange(0, 210, 1)

    # 模拟4个通道的数据
    baseline_start = [100, 200, 50, 300]  # 各通道的初始基线
    baseline_end = [102, 198, 52, 298]  # 各通道的结束基线（略有不同）

    test_data = {'Time (s)': time_data}

    for ch_idx, (start_val, end_val) in enumerate(zip(baseline_start, baseline_end)):
        channel_data = []

        # 前100个平静值（有小幅波动）
        for i in range(100):
            noise = np.random.normal(0, 1)  # 小幅随机波动
            channel_data.append(start_val + noise)

        # 中间10个突变值
        for i in range(10):
            # 从基线突然降低到约一半，然后逐渐恢复
            drop_value = start_val * 0.5 + (end_val - start_val * 0.5) * (i / 9)
            channel_data.append(drop_value)

        # 后100个平静值（有小幅波动）
        for i in range(100):
            noise = np.random.normal(0, 1)  # 小幅随机波动
            channel_data.append(end_val + noise)

        test_data[f'Channel_{ch_idx + 1}'] = channel_data

    # 创建临时CSV文件
    df = pd.DataFrame(test_data)
    temp_file = tempfile.NamedTemporaryFile(mode='w', suffix='.csv', delete=False)
    df.to_csv(temp_file.name, index=False)
    temp_file.close()

    try:
        print("=== 测试不同chunk大小的影响 ===")

        # 测试不同的chunk大小
        chunk_sizes = [30, 100, 210]  # 30: 会分成多个chunk, 100: 中等大小, 210: 全部数据

        for chunk_size in chunk_sizes:
            print(f"\n--- Chunk大小: {chunk_size} ---")

            filter_instance = Filters(input_length=chunk_size, step_size=chunk_size // 2)

            # 测试振动阈值模式
            result = filter_instance.uni_baseline_filter(data_path=temp_file.name, _left_margin=None,
                                                         _right_margin=None, _vibration_threshold=10)

            print(f"生成的chunk数量: {len(result)}")

            for chunk_idx, (chunk_name, chunk_data) in enumerate(result.items()):
                start_idx, end_idx = map(int, chunk_name.split('_'))
                print(f"\nChunk {chunk_idx + 1} ({chunk_name}):")
                print(f"  数据范围: {start_idx} 到 {end_idx}")
                print(f"  数据形状: {chunk_data.shape}")

                # 显示这个chunk的原始数据范围
                original_chunk = df.iloc[start_idx:end_idx].drop(columns=['Time (s)']).values
                print(f"  原始数据范围: [{original_chunk.min():.1f}, {original_chunk.max():.1f}]")
                print(f"  处理后数据范围: [{chunk_data.min():.1f}, {chunk_data.max():.1f}]")

                # 分析这个chunk包含的数据类型
                if start_idx < 100 and end_idx <= 100:
                    chunk_type = "纯前段平静数据"
                elif start_idx >= 110 and end_idx <= 210:
                    chunk_type = "纯后段平静数据"
                elif start_idx < 100 and end_idx > 110:
                    chunk_type = "跨越突变的完整数据"
                elif start_idx < 110 and end_idx > 100:
                    chunk_type = "包含前段平静+突变"
                elif start_idx < 110 and end_idx <= 110:
                    chunk_type = "包含突变+后段平静"
                else:
                    chunk_type = "其他"

                print(f"  数据类型: {chunk_type}")

                # 检查基线是否合理
                if chunk_type == "纯前段平静数据" or chunk_type == "纯后段平静数据":
                    # 对于纯平静数据，处理后应该接近0
                    avg_after = np.mean(chunk_data, axis=0)
                    print(f"  各通道平均值: {[f'{x:.2f}' for x in avg_after]} (应该接近0)")

                if chunk_idx >= 2:  # 只显示前几个chunk的详细信息
                    print("  ...")
                    break

        print("\n=== 分析chunk分割对基线检测的影响 ===")

        # 特别分析chunk_size=30的情况
        filter_instance = Filters(input_length=30, step_size=10)
        result = filter_instance.uni_baseline_filter(data_path=temp_file.name, _left_margin=None, _right_margin=None,
                                                     _vibration_threshold=20)

        print("chunk_size=10时的详细分析:")
        for chunk_name, chunk_data in result.items():
            start_idx, end_idx = map(int, chunk_name.split('_'))

            # 判断这个chunk是否能正确识别基线
            contains_transition = (start_idx < 110 and end_idx > 100)

            if contains_transition:
                print(f"\nChunk {chunk_name} 包含突变区域:")
                original_chunk = df.iloc[start_idx:end_idx].drop(columns=['Time (s)']).values

                # 手动验证基线检测
                for col_idx in range(original_chunk.shape[1]):
                    col_data = original_chunk[:, col_idx]
                    diff_data = np.abs(np.diff(col_data))

                    # 找稳定区域
                    stable_mask = diff_data < 20
                    left_stable_end = 0
                    for i in range(len(stable_mask)):
                        if stable_mask[i]:
                            left_stable_end = i + 1
                        else:
                            break

                    right_stable_start = len(col_data)
                    for i in range(len(stable_mask) - 1, -1, -1):
                        if stable_mask[i]:
                            right_stable_start = i + 1
                        else:
                            break

                    print(
                        f"  Channel_{col_idx + 1}: 左稳定区长度={left_stable_end}, 右稳定区长度={len(col_data) - right_stable_start}")

                    if left_stable_end > 0 or right_stable_start < len(col_data):
                        baseline_points = []
                        if left_stable_end > 0:
                            baseline_points.extend(col_data[:left_stable_end])
                        if right_stable_start < len(col_data):
                            baseline_points.extend(col_data[right_stable_start:])
                        expected_baseline = np.mean(baseline_points)
                        print(f"    计算出的基线: {expected_baseline:.2f}")

    finally:
        # 清理临时文件
        os.unlink(temp_file.name)


def test_prepare_data():
    test_filter = Filters(input_length=5, step_size=10)
    raw_data = test_filter._prepare_data(file_path="OldFiles/uni_baseline模式的测试数据.csv")
    normalized_data = test_filter.normalize_filter(data_path="OldFiles/uni_baseline模式的测试数据.csv")
    reversed_data = test_filter.reverse_time_filter(data_path="OldFiles/uni_baseline模式的测试数据.csv")
    adjusted_data = test_filter.adjust_window_filter_path(data_path="OldFiles/uni_baseline模式的测试数据.csv",
                                                          target_chunk_size=10)
    zoomed_data = test_filter.zoom_filter(data_path="OldFiles/uni_baseline模式的测试数据.csv", zoom_factor=0.5)
    print(f"{raw_data=}")
    print(f"{list(zoomed_data.values())=}")

# 运行测试
if __name__ == "__main__":
    # test_uni_baseline_filter_chunks()
    test_prepare_data()