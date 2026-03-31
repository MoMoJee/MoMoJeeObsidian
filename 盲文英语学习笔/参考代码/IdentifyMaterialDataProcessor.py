import os
import threading
import time
import pickle
from collections import defaultdict
from queue import Queue
from typing import Dict, List, Union

import pandas as pd
import torch
from torch.utils.data import DataLoader, Dataset
import socket
import NevNetsDefiner
from PredictionVisualizer import PredictionVisualizer
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QTimer, pyqtSignal, QObject, Qt
import sys

from utils import Filters
from CNNTrain import TrainingConfig, create_model, load_training_artifacts
from prediction_results_db import PredictionResultsDB



class TestDataset(Dataset):
    """测试数据集类"""

    def __init__(self, data):
        self.data = data

    def __len__(self):
        return 1  # 假设每个文件只包含一个样本

    def __getitem__(self, idx):
        return torch.tensor(self.data, dtype=torch.float32)


class ModelInfo:
    """模型信息类，用于存储单个模型的所有信息"""

    def __init__(self, model_dir: str):
        self.model_dir = model_dir
        self.config = None
        self.label_encoder = None
        self.model = None
        self.device = None
        self.model_file_path = None
        self.filter_modes = None  # 新增：每个模型专用的预处理模式

        # 加载模型信息
        self._load_model_artifacts()

    def _load_model_artifacts(self):
        """加载模型目录中的所有产物"""
        try:
            print(f"正在加载模型目录: {self.model_dir}")

            # 验证目录结构
            self._validate_model_directory()

            # 加载配置
            config_path = os.path.join(self.model_dir, "config.json")
            self.config = TrainingConfig.load(config_path)
            print(f"配置文件加载成功: {config_path}")

            # 推断该模型的预处理模式
            self.filter_modes = self._infer_filter_modes_from_config()
            print(f"模型 {self.model_dir} 使用预处理模式: {self.filter_modes}")

            # 加载LabelEncoder
            label_encoder_path = os.path.join(self.model_dir, "label_encoder.pkl")
            with open(label_encoder_path, 'rb') as f:
                self.label_encoder = pickle.load(f)
            print(f"LabelEncoder加载成功: {label_encoder_path}")

            # 查找模型文件
            self.model_file_path = self._find_model_file()
            print(f"模型文件找到: {self.model_file_path}")

            # 加载模型
            self._load_model()
            print(f"模型加载成功，类别数: {len(self.label_encoder.classes_)}")
            print(
                f"类别映射: {dict(zip(self.label_encoder.classes_, self.label_encoder.transform(self.label_encoder.classes_)))}")

        except Exception as e:
            raise RuntimeError(f"加载模型目录 {self.model_dir} 失败: {e}")

    def _infer_filter_modes_from_config(self):
        """从当前模型配置推断使用的预处理模式"""
        config = self.config
        modes = []

        if config.normalize:
            modes.append("normalize")
        elif config.uni_baseline:
            if config.std:
                modes.append("uni_baseline_std")
            else:
                modes.append("uni_baseline")
        elif config.std:
            modes.append("std")
        else:
            modes.append("default")

        return modes

    def _validate_model_directory(self):
        """验证模型目录结构"""
        if not os.path.exists(self.model_dir):
            raise FileNotFoundError(f"模型目录不存在: {self.model_dir}")

        required_files = ["config.json", "label_encoder.pkl"]
        for file_name in required_files:
            file_path = os.path.join(self.model_dir, file_name)
            if not os.path.exists(file_path):
                raise FileNotFoundError(f"必需文件不存在: {file_path}")

    def _find_model_file(self):
        """查找模型文件"""
        # 常见的模型文件模式
        model_patterns = [
            f"best_model_{self.config.model_type.lower()}.pth",
            "best_model_cnn_deeper.pth",
            "best_model_cnn.pth",
            "best_model.pth",
        ]

        for pattern in model_patterns:
            model_path = os.path.join(self.model_dir, pattern)
            if os.path.exists(model_path):
                return model_path

        # 如果没有找到标准名称，搜索所有.pth文件
        pth_files = [f for f in os.listdir(self.model_dir) if f.endswith('.pth')]
        if pth_files:
            model_path = os.path.join(self.model_dir, pth_files[0])
            print(f"警告: 使用找到的第一个.pth文件: {pth_files[0]}")
            return model_path

        raise FileNotFoundError(f"在模型目录 {self.model_dir} 中找不到模型文件")

    def _load_model(self):
        """加载模型"""
        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

        # 根据配置创建模型
        self.model = create_model(self.config).to(self.device)

        # 加载模型权重
        self.model.load_state_dict(torch.load(self.model_file_path, map_location=self.device))
        self.model.eval()

        print(f"模型加载到设备: {self.device}")


class OpticalFiberDataTrainer:
    def __init__(self, save_path: str = "best_model_cnn.pth", raw_path: str = ".\data\raw", ):
        pass


class VisualizationManager(QObject):
    """可视化管理器 - 负责管理GUI组件和信号"""

    # 定义信号
    new_file_signal = pyqtSignal(str, object, dict)  # file_path, original_data, processed_data
    chunk_prediction_signal = pyqtSignal(str, object, str, float,
                                         str)  # model_path, chunk_idx, predicted_class, confidence, filter_mode
    final_results_signal = pyqtSignal(dict, dict, str)  # model_confidences, model_consecutive_counts, filter_mode

    def __init__(self, large_ui_mode: bool = False):
        super().__init__()
        self.app = None
        self.visualizer = None
        self.large_ui_mode = large_ui_mode
        print(f"开始初始化可视化管理器... 大UI模式: {self.large_ui_mode}")

    def initialize_gui(self):
        """在主线程中初始化GUI"""
        print("准备在主线程中启动可视化界面...")

        try:
            # 检查是否已经有QApplication实例
            if QApplication.instance() is None:
                self.app = QApplication(sys.argv)
                print("创建新的QApplication实例")
            else:
                self.app = QApplication.instance()
                print("使用现有的QApplication实例")

            # 设置应用样式
            self.app.setStyle('Fusion')

            # 创建可视化器，传入大UI模式参数
            self.visualizer = PredictionVisualizer(large_ui_mode=self.large_ui_mode)

            # 连接信号到槽 - 使用Qt.QueuedConnection确保线程安全
            print("开始连接信号到槽...")
            self.new_file_signal.connect(
                self.visualizer.on_new_file_received,
                Qt.QueuedConnection
            )
            self.chunk_prediction_signal.connect(
                self.visualizer.update_chunk_prediction,
                Qt.QueuedConnection
            )
            self.final_results_signal.connect(
                self.visualizer.update_final_results,
                Qt.QueuedConnection
            )
            print("信号槽连接完成")

            # 显示界面
            self.visualizer.show()
            self.visualizer.raise_()  # 确保窗口在最前面
            self.visualizer.activateWindow()  # 激活窗口

            print(f"PredictionVisualizer GUI 初始化成功 - 大UI模式: {self.large_ui_mode}")

            # 处理事件以确保界面响应
            self.app.processEvents()

            return True

        except Exception as e:
            print(f"GUI初始化失败: {e}")
            import traceback
            traceback.print_exc()
            return False

    def start_event_loop(self):
        """启动Qt事件循环"""
        if self.app:
            print("启动Qt事件循环...")
            # 不要调用app.exec_()，因为这会阻塞主线程
            # 而是使用定时器来处理事件
            self.timer = QTimer()
            self.timer.timeout.connect(self.app.processEvents)
            self.timer.start(50)  # 每50ms处理一次事件
            print("Qt事件循环已启动")


class OpticalFiberDataProcessor:
    def __init__(self, model_dirs: Union[str, List[str]], mode: str = "socket", enable_visualization: bool = False,
                 large_ui_mode: bool = False, **kwargs):
        """
        使用新的模型目录方式初始化处理器

        :param model_dirs: 单个模型目录路径字符串，或多个模型目录路径的列表
        :param mode: 运行模式。默认为 socket 监听端口 65432。设置为 file，从文件导入，同时需要指定 file_path 关键字变量
        :param enable_visualization: 是否启用可视化界面，默认 False
        :param large_ui_mode: 是否启用大UI模式，仅显示三个模型的检测结果，默认 False
        :key file_path: file模式所需的文件路径
        :key uniform_filter_modes: 强制所有模型使用统一的预处理模式列表（覆盖各自的配置）
        """

        # 添加数据库初始化
        self.prediction_db = PredictionResultsDB("optical_fiber_predictions.db")
        print("已初始化预测结果数据库")


        # 处理模型目录参数
        if isinstance(model_dirs, str):
            self.model_dirs = [model_dirs]
        else:
            self.model_dirs = model_dirs

        # 加载所有模型信息
        self.models_info = {}
        for model_dir in self.model_dirs:
            try:
                model_info = ModelInfo(model_dir)
                self.models_info[model_dir] = model_info
                print(f"成功加载模型: {model_dir}")
            except Exception as e:
                print(f"加载模型失败 {model_dir}: {e}")
                continue

        if not self.models_info:
            raise RuntimeError("没有成功加载任何模型")

        # 从第一个成功加载的模型获取基础配置（主要用于兼容性）
        self.primary_model_info = list(self.models_info.values())[0]

        # 检查是否强制使用统一的预处理模式
        self.use_uniform_filter_modes = "uniform_filter_modes" in kwargs
        if self.use_uniform_filter_modes:
            self.uniform_filter_modes = kwargs["uniform_filter_modes"]
            print(f"使用统一预处理模式（覆盖各模型配置）: {self.uniform_filter_modes}")
        else:
            print("使用各模型专用的预处理模式")

        self.mode = mode
        self.large_ui_mode = large_ui_mode

        if mode == "file":
            if "file_path" in kwargs:
                self.file_path = kwargs["file_path"]
            else:
                raise ValueError("在 file 模式下，必须指定 file_path 参数")

        # 添加socket相关的属性
        self.socket_queue = Queue()
        self.socket_thread = None
        self.socket_running = False


        # 可视化相关
        self.enable_visualization = enable_visualization
        self.vis_manager = None
        self.gui_thread = None

        if self.enable_visualization:
            print(f"开始初始化可视化管理器... 大UI模式: {self.large_ui_mode}")
            self.vis_manager = VisualizationManager(large_ui_mode=self.large_ui_mode)
            self._setup_visualization()


    def _setup_visualization(self):
        """设置可视化组件"""
        try:
            print("设置可视化组件...")

            # 创建可视化管理器（已在__init__中创建）
            # 在主线程中初始化GUI
            if self.vis_manager.initialize_gui():
                print("可视化组件设置成功")
                # 启动事件循环
                self.vis_manager.start_event_loop()

                # 创建定时器来定期处理Qt事件
                self.event_timer = QTimer()
                self.event_timer.timeout.connect(self._process_qt_events)
                self.event_timer.start(100)  # 每100ms处理一次事件
            else:
                print("可视化组件设置失败")
                self.enable_visualization = False

        except Exception as e:
            print(f"可视化设置失败: {e}")
            import traceback
            traceback.print_exc()
            self.enable_visualization = False


    def _process_qt_events(self):
        """处理Qt事件"""
        try:
            if self.vis_manager and self.vis_manager.app:
                self.vis_manager.app.processEvents()
        except Exception as e:
            print(f"处理Qt事件时出错: {e}")

    def _emit_new_file_signal(self, file_path, original_data, processed_data):
        """发送新文件信号"""
        if self.enable_visualization and self.vis_manager:
            try:
                print(f"准备发送新文件信号: {file_path}")
                self.vis_manager.new_file_signal.emit(file_path, original_data, processed_data)
                print("已发送新文件信号到可视化界面")

                # 强制处理事件
                if self.vis_manager.app:
                    self.vis_manager.app.processEvents()
                    QApplication.processEvents()  # 额外的事件处理

            except Exception as e:
                print(f"发送新文件信号失败: {e}")
                import traceback
                traceback.print_exc()

    def _emit_chunk_prediction_signal(self, model_path, chunk_idx, predicted_class, confidence, filter_mode):
        """发送chunk预测信号"""
        if self.enable_visualization and self.vis_manager:
            try:
                print(f"发送chunk预测信号: {model_path}, chunk_{chunk_idx}, {predicted_class}, {confidence:.3f}")
                self.vis_manager.chunk_prediction_signal.emit(model_path, chunk_idx, predicted_class, confidence,
                                                              filter_mode)

                # 强制处理事件
                if self.vis_manager.app:
                    self.vis_manager.app.processEvents()

            except Exception as e:
                print(f"发送chunk预测信号失败: {e}")

    def _emit_final_results_signal(self, model_confidences, model_consecutive_counts, filter_mode):
        """发送最终结果信号"""
        if self.enable_visualization and self.vis_manager:
            try:
                print("发送最终结果信号...")
                self.vis_manager.final_results_signal.emit(model_confidences, model_consecutive_counts, filter_mode)

                # 强制处理事件
                if self.vis_manager.app:
                    self.vis_manager.app.processEvents()

                print("最终结果信号已发送")
            except Exception as e:
                print(f"发送最终结果信号失败: {e}")

    def _get_filter_kwargs_for_model(self, model_info: ModelInfo):
        """根据模型配置获取预处理参数"""
        config = model_info.config
        kwargs = {}

        if hasattr(config, 'uni_baseline') and config.uni_baseline:
            if hasattr(config, '_left_margin'):
                kwargs["_left_margin"] = config._left_margin
            if hasattr(config, '_right_margin'):
                kwargs["_right_margin"] = config._right_margin
            if hasattr(config, '_vibration_threshold'):
                kwargs["_vibration_threshold"] = config._vibration_threshold

        return kwargs

    def _socket_listener(self):
        """在单独线程中运行的socket监听器"""
        print("Socket监听线程启动...")
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind(("localhost", 65432))
            s.listen()
            print("Socket监听已启动，等待连接...")

            while self.socket_running:
                try:
                    # 设置超时，避免无限阻塞
                    s.settimeout(1.0)
                    conn, addr = s.accept()

                    with conn:
                        csv_path = conn.recv(1024).decode()
                        print(f"接收到数据路径: {csv_path}")
                        # 将数据路径放入队列
                        self.socket_queue.put(csv_path)

                except socket.timeout:
                    # 超时继续循环，检查是否需要停止
                    continue
                except Exception as e:
                    if self.socket_running:
                        print(f"Socket监听错误: {e}")

        print("Socket监听线程结束")

    def _process_socket_queue(self):
        """处理socket队列中的数据"""
        while not self.socket_queue.empty():
            try:
                csv_path = self.socket_queue.get_nowait()
                print(f"开始处理数据: {csv_path}")
                # TODO: 这里需要修复socket模式的预测逻辑
                self._forecast_single_file(csv_path)
            except Exception as e:
                print(f"处理队列数据时出错: {e}")

    def _data_filter(self, data_path_modes_s: Dict[str, List[str]], model_info: ModelInfo):
        """
        数据预处理 - 根据特定模型的配置进行预处理

        :param data_path_modes_s: 格式：{<路径1>: [方法A, 方法B], <路径2>: []}
        :param model_info: 模型信息，用于获取预处理参数
        """

        filtered_result = {}

        # 使用模型配置中的参数
        _filter = Filters(input_length=model_info.config.input_length,
                          step_size=model_info.config.step_size)

        # 获取模型特定的预处理参数
        filter_kwargs = self._get_filter_kwargs_for_model(model_info)

        for data_path, modes in data_path_modes_s.items():
            if not modes:
                filtered_result[data_path] = {"default": _filter.default_filter(data_path=data_path)}
                continue

            filtered_result[data_path] = {}

            for mode in modes:
                try:
                    if mode == "default":
                        filtered_result[data_path][mode] = _filter.default_filter(data_path=data_path)

                    elif mode == "normalize":
                        filtered_result[data_path][mode] = _filter.normalize_filter(data_path=data_path)

                    elif mode == "diff":
                        raise KeyError(f"预处理方式 {mode} 尚未完善，请勿使用")

                    elif mode == "std":
                        filtered_result[data_path][mode] = _filter.standardize_filter(data_path=data_path)

                    elif mode == "uni_baseline":
                        if not filter_kwargs:
                            print(f"警告: 模型 {model_info.model_dir} 没有 uni_baseline 所需参数，跳过此预处理模式")
                            continue
                        filtered_result[data_path][mode] = _filter.uni_baseline_filter(
                            data_path=data_path, **filter_kwargs
                        )

                    elif mode == "uni_baseline_std":
                        if not filter_kwargs:
                            print(f"警告: 模型 {model_info.model_dir} 没有 uni_baseline_std 所需参数，跳过此预处理模式")
                            continue
                        filtered_result[data_path][mode] = _filter.uni_baseline_std_filter(
                            data_path=data_path, **filter_kwargs
                        )

                    else:
                        raise ValueError(f"预处理方式 {mode} 不是有效的方式")

                except Exception as e:
                    print(f"警告: 模型 {model_info.model_dir} 执行预处理模式 {mode} 时出错: {e}")
                    print(f"跳过此预处理模式")
                    continue

        return filtered_result

    def _result_saver(self):
        """保存检测数据"""
        pass

    def _forecast(self, test_path_mode=None):
        """
        预测过程 - 每个模型使用自己的预处理模式

        :param test_path_mode: 形如 {<文件路径>: ["normalize", "std", "uni_baseline"]}，仅在使用统一预处理模式时有效
        """

        # 短暂延迟确保可视化界面有时间处理
        time.sleep(0.5)

        # 准备文件路径
        if test_path_mode is None:
            test_files = self.file_path
        else:
            test_files = list(test_path_mode.keys())

        for path in test_files:
            if self.mode == "file":
                print(f"\n——————————按回车，对数据 {path} 的预测开始——————————")
                input()
            else:
                print(f"\n—————————对数据 {path} 的预测开始——————————")

            # 初始化当前文件的预测结果收集器
            file_predictions = {}

            # 加载原始数据用于可视化
            original_data = None
            if self.enable_visualization:
                try:
                    original_data = pd.read_csv(path)
                    print("原始数据加载成功，准备可视化")
                except Exception as e:
                    print(f"可视化数据加载失败: {e}")

            # 对每个模型分别处理
            for model_dir, model_info in self.models_info.items():
                print(f"\n使用模型: {model_dir}")

                # 确定该模型使用的预处理模式
                if self.use_uniform_filter_modes:
                    # 使用统一的预处理模式
                    filter_modes = self.uniform_filter_modes
                    print(f"使用统一预处理模式: {filter_modes}")
                else:
                    # 使用模型专用的预处理模式
                    filter_modes = model_info.filter_modes
                    print(f"使用模型专用预处理模式: {filter_modes}")

                # 使用当前模型的配置进行数据预处理
                try:
                    filtered_paths_datas = self._data_filter(
                        {path: filter_modes},
                        model_info=model_info
                    )
                except Exception as e:
                    print(f"模型 {model_dir} 数据预处理失败: {e}")
                    continue

                # 发送新文件信号（仅在第一个模型时发送）
                if (self.enable_visualization and original_data is not None and
                        model_dir == list(self.models_info.keys())[0]):
                    self._emit_new_file_signal(path, original_data, filtered_paths_datas)

                filtered_path_datas = filtered_paths_datas[path]

                for filter_mode, filtered_path_data in filtered_path_datas.items():
                    print(f"  使用预处理模式: {filter_mode}")

                    # 用于存储当前模型的综合置信度
                    model_confidences = defaultdict(float)
                    # 用于存储当前模型的连续置信度统计
                    model_consecutive_counts = defaultdict(lambda: {"current": 0, "max": 0})
                    current_best_class = None

                    for chunk_idx, chunk_data in filtered_path_data.items():
                        test_dataset = TestDataset(chunk_data)
                        test_loader = DataLoader(test_dataset, batch_size=1, shuffle=False)

                        try:
                            predicted_classes, confidences = NevNetsDefiner.test_model(
                                model_info.model,
                                model_info.device,
                                test_loader,
                                model_info.label_encoder
                            )

                            # 收集每个 chunk 的置信度
                            for cls, conf in zip(predicted_classes, confidences):
                                model_confidences[cls] += conf

                            # 获取当前chunk预测类别及其置信度
                            current_class = predicted_classes[0]
                            current_confidence = confidences[0]

                            # 实时更新可视化界面
                            if self.enable_visualization:
                                self._emit_chunk_prediction_signal(
                                    model_dir, chunk_idx, current_class, current_confidence, filter_mode
                                )

                            print(f"    Chunk {chunk_idx}: {current_class} (置信度: {current_confidence:.3f})")

                            # 连续预测统计
                            if current_class == current_best_class:
                                model_consecutive_counts[current_class]["current"] += 1
                                if model_consecutive_counts[current_class]["current"] > \
                                        model_consecutive_counts[current_class]["max"]:
                                    model_consecutive_counts[current_class]["max"] = \
                                        model_consecutive_counts[current_class]["current"]
                            else:
                                if current_best_class is not None:
                                    if model_consecutive_counts[current_best_class]["current"] > \
                                            model_consecutive_counts[current_best_class]["max"]:
                                        model_consecutive_counts[current_best_class]["max"] = \
                                            model_consecutive_counts[current_best_class]["current"]
                                model_consecutive_counts[current_class]["current"] = 1
                                if model_consecutive_counts[current_class]["max"] == 0:
                                    model_consecutive_counts[current_class]["max"] = 1
                                current_best_class = current_class

                        except Exception as e:
                            print(f"错误发生在模型 {model_dir} 对数据 {path} 的 {chunk_idx} 执行预测时。详情： {e}")

                    # 综合判断最终预测类别
                    if model_confidences:
                        final_class = max(model_confidences.items(), key=lambda x: x[1])[0]
                        final_confidence = model_confidences[final_class]
                        print(
                            f"  最终预测类别（模型 {model_dir}）：{final_class}，总置信度：{final_confidence:.4f}，预处理模式：{filter_mode}")

                        # 收集当前模型的预测结果
                        file_predictions[model_dir] = (final_class, final_confidence)

                    # 连续置信度统计
                    if model_consecutive_counts:
                        max_count_class = max(model_consecutive_counts.items(), key=lambda x: x[1]["max"])[0]
                        max_count = model_consecutive_counts[max_count_class]["max"]
                        print(f"  模型 {model_dir} 连续猜测最强值：{max_count_class}，最大连续出现次数：{max_count}")

                    # 发送最终结果信号
                    self._emit_final_results_signal(
                        {model_dir: dict(model_confidences)},
                        {model_dir: dict(model_consecutive_counts)},
                        filter_mode
                    )

            # 在处理完所有模型后，保存到数据库
            try:
                if file_predictions:
                    notes = f"批量预测完成，模式: {self.mode}"
                    self._save_prediction_to_db(file_predictions, path, notes)
                    print(f"已将文件 {path} 的预测结果保存到数据库")
                else:
                    print(f"文件 {path} 没有有效的预测结果")
            except Exception as e:
                print(f"保存预测结果到数据库时出错: {e}")

    def _forecast_single_file(self, file_path, show_forecast_progress=True):
        """处理单个文件的预测逻辑（从_forecast方法中提取）"""
        print(f"\n—————————对数据 {file_path} 的预测开始——————————")

        # 初始化当前文件的预测结果收集器
        file_predictions = {}

        # 加载原始数据用于可视化
        original_data = None
        if self.enable_visualization:
            try:
                original_data = pd.read_csv(file_path)
                print("原始数据加载成功，准备可视化")
            except Exception as e:
                print(f"可视化数据加载失败: {e}")

        # 对每个模型分别处理
        for model_dir, model_info in self.models_info.items():
            print(f"\n使用模型: {model_dir}")

            # 确定该模型使用的预处理模式
            if self.use_uniform_filter_modes:
                filter_modes = self.uniform_filter_modes
                print(f"使用统一预处理模式: {filter_modes}")
            else:
                filter_modes = model_info.filter_modes
                print(f"使用模型专用预处理模式: {filter_modes}")

            # 使用当前模型的配置进行数据预处理
            try:
                filtered_paths_datas = self._data_filter(
                    {file_path: filter_modes},
                    model_info=model_info
                )
            except Exception as e:
                print(f"模型 {model_dir} 数据预处理失败: {e}")
                continue

            # 发送新文件信号（仅在第一个模型时发送）
            if (self.enable_visualization and original_data is not None and
                    model_dir == list(self.models_info.keys())[0]):
                self._emit_new_file_signal(file_path, original_data, filtered_paths_datas)

            filtered_path_datas = filtered_paths_datas[file_path]

            for filter_mode, filtered_path_data in filtered_path_datas.items():
                print(f"  使用预处理模式: {filter_mode}")

                # 用于存储当前模型的综合置信度
                model_confidences = defaultdict(float)
                # 用于存储当前模型的连续置信度统计
                model_consecutive_counts = defaultdict(lambda: {"current": 0, "max": 0})
                current_best_class = None

                for chunk_idx, chunk_data in filtered_path_data.items():
                    test_dataset = TestDataset(chunk_data)
                    test_loader = DataLoader(test_dataset, batch_size=1, shuffle=False)

                    try:
                        predicted_classes, confidences = NevNetsDefiner.test_model(
                            model_info.model,
                            model_info.device,
                            test_loader,
                            model_info.label_encoder
                        )

                        # 收集每个 chunk 的置信度
                        for cls, conf in zip(predicted_classes, confidences):
                            model_confidences[cls] += conf

                        # 获取当前chunk预测类别及其置信度
                        current_class = predicted_classes[0]
                        current_confidence = confidences[0]

                        # 实时更新可视化界面
                        if self.enable_visualization:
                            self._emit_chunk_prediction_signal(
                                model_dir, chunk_idx, current_class, current_confidence, filter_mode
                            )

                        if show_forecast_progress:
                            print(f"    Chunk {chunk_idx}: {current_class} (置信度: {current_confidence:.3f})")

                        # 连续预测统计
                        if current_class == current_best_class:
                            model_consecutive_counts[current_class]["current"] += 1
                            if model_consecutive_counts[current_class]["current"] > \
                                    model_consecutive_counts[current_class]["max"]:
                                model_consecutive_counts[current_class]["max"] = \
                                    model_consecutive_counts[current_class]["current"]
                        else:
                            if current_best_class is not None:
                                if model_consecutive_counts[current_best_class]["current"] > \
                                        model_consecutive_counts[current_best_class]["max"]:
                                    model_consecutive_counts[current_best_class]["max"] = \
                                        model_consecutive_counts[current_best_class]["current"]
                            model_consecutive_counts[current_class]["current"] = 1
                            if model_consecutive_counts[current_class]["max"] == 0:
                                model_consecutive_counts[current_class]["max"] = 1
                            current_best_class = current_class

                    except Exception as e:
                        print(f"错误发生在模型 {model_dir} 对数据 {file_path} 的 {chunk_idx} 执行预测时。详情： {e}")

                # 综合判断最终预测类别
                if model_confidences:
                    final_class = max(model_confidences.items(), key=lambda x: x[1])[0]
                    final_confidence = model_confidences[final_class]
                    print(
                        f"  最终预测类别（模型 {model_dir}）：{final_class}，总置信度：{final_confidence:.4f}，预处理模式：{filter_mode}")

                    # 收集当前模型的预测结果
                    file_predictions[model_dir] = (final_class, final_confidence)

                # 连续置信度统计
                if model_consecutive_counts:
                    max_count_class = max(model_consecutive_counts.items(), key=lambda x: x[1]["max"])[0]
                    max_count = model_consecutive_counts[max_count_class]["max"]
                    print(f"  模型 {model_dir} 连续猜测最强值：{max_count_class}，最大连续出现次数：{max_count}")

                # 发送最终结果信号
                self._emit_final_results_signal(
                    {model_dir: dict(model_confidences)},
                    {model_dir: dict(model_consecutive_counts)},
                    filter_mode
                )

        # 在处理完所有模型后，保存到数据库
        try:
            if file_predictions:
                notes = f"单文件预测完成，模式: {self.mode}, 显示进度: {show_forecast_progress}"
                self._save_prediction_to_db(file_predictions, file_path, notes)
                print(f"已将文件 {file_path} 的预测结果保存到数据库")
            else:
                print(f"文件 {file_path} 没有有效的预测结果")
        except Exception as e:
            print(f"保存预测结果到数据库时出错: {e}")

    def _save_prediction_to_db(self, predictions_dict, file_path=None, notes=None):
        """
        将预测结果保存到数据库

        Args:
            predictions_dict: 预测结果字典，格式如 {'model_dir': ('prediction', confidence), ...}
            file_path: 文件路径
            notes: 备注信息
        """
        try:
            # 获取模型目录列表，确保按一致的顺序处理
            model_dirs = list(self.models_info.keys())

            # 确保有三个模型的结果，不足的用默认值填充
            model_predictions = []
            model_names = []

            for i in range(3):
                if i < len(model_dirs):
                    model_dir = model_dirs[i]
                    model_name = os.path.basename(model_dir) if model_dir else f"Model_{i + 1}"

                    if model_dir in predictions_dict:
                        prediction, confidence = predictions_dict[model_dir]
                        model_predictions.append((model_name, str(prediction), float(confidence)))
                    else:
                        model_predictions.append((model_name, "未预测", 0.0))
                else:
                    # 如果模型数量不足3个，用默认值填充
                    model_predictions.append((f"Model_{i + 1}", "未使用", 0.0))

            # 插入到数据库
            record_id = self.prediction_db.insert_prediction_result(
                model1_name=model_predictions[0][0],
                model1_prediction=model_predictions[0][1],
                model1_confidence=model_predictions[0][2],
                model2_name=model_predictions[1][0],
                model2_prediction=model_predictions[1][1],
                model2_confidence=model_predictions[1][2],
                model3_name=model_predictions[2][0],
                model3_prediction=model_predictions[2][1],
                model3_confidence=model_predictions[2][2],
                file_path=file_path,
                notes=notes
            )

            print(f"预测结果已保存到数据库，记录ID: {record_id}")

            return record_id

        except Exception as e:
            print(f"保存预测结果到数据库时出错: {e}")
            import traceback
            traceback.print_exc()
            return None

    def data_processor(self):
        if self.mode == "socket":
            # 启动socket监听线程
            self.socket_running = True
            self.socket_thread = threading.Thread(target=self._socket_listener, daemon=True)
            self.socket_thread.start()

            print("Socket模式已启动，UI界面保持响应状态")

            # 创建定时器来处理socket队列中的数据
            if self.enable_visualization and self.vis_manager:
                # 创建队列处理定时器
                self.queue_timer = QTimer()
                self.queue_timer.timeout.connect(self._process_socket_queue)
                self.queue_timer.start(100)  # 每100ms检查一次队列

                # 主线程专门处理Qt事件循环
                try:
                    while True:
                        if self.vis_manager and self.vis_manager.app:
                            self.vis_manager.app.processEvents()
                        time.sleep(0.01)  # 短暂休眠，避免CPU占用过高
                except KeyboardInterrupt:
                    print("接收到中断信号，正在停止...")
                    self.socket_running = False
                    if self.socket_thread:
                        self.socket_thread.join(timeout=2)
            else:
                # 没有可视化界面的情况下，简单循环处理队列
                try:
                    while True:
                        self._process_socket_queue()
                        time.sleep(0.1)
                except KeyboardInterrupt:
                    print("接收到中断信号，正在停止...")
                    self.socket_running = False
                    if self.socket_thread:
                        self.socket_thread.join(timeout=2)

        elif self.mode == "file":
            self._forecast()
        else:
            raise KeyError(f"mode 参数错误: 模式 {self.mode} 不存在")

    def stop_socket_listener(self):
        """停止socket监听器"""
        self.socket_running = False
        if self.socket_thread and self.socket_thread.is_alive():
            self.socket_thread.join(timeout=2)
            print("Socket监听线程已停止")


def get_csv_files_in_folder(folder_path: str) -> List[str]:
    """
    遍历指定文件夹，获取其中所有CSV文件相对于项目根目录的相对路径

    :param folder_path: 要搜索的文件夹路径
    :return: CSV文件相对路径的列表
    """
    csv_files = []

    # 检查文件夹是否存在
    if not os.path.exists(folder_path):
        raise ValueError(f"文件夹 {folder_path} 不存在")

    # 遍历文件夹中的所有文件
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            # 检查文件扩展名是否为.csv
            if file.lower().endswith('.csv'):
                # 获取完整路径
                full_path = os.path.join(root, file)
                # 转换为相对于项目根目录的相对路径
                relative_path = os.path.relpath(full_path)
                # 统一使用正斜杠（适用于跨平台）
                relative_path = relative_path.replace('\\', '/')
                csv_files.append(relative_path)

    # 检查文件夹是否存在
    if not csv_files:
        raise ValueError(f"文件夹 {folder_path} 中没有CSV文件")

    return csv_files


def sensor_monitor(large_ui_mode: bool = False
):
    """传感器监控模式 - 使用新的模型目录方式"""
    model_dir = ["models/CNN_4",
                 "models/ResNet_4",
                 "models/CPCNN_4"]

    # model_dir = ["models/CNNImproved",
    #              "models/ResNet",
    #              "models/CPCNN0907"]

    data_processor = OpticalFiberDataProcessor(
        model_dirs=model_dir,
        mode="socket",
        enable_visualization=True,
        large_ui_mode=large_ui_mode,
        file_path="NO_file_path",
    )
    data_processor.data_processor()


def file_test():
    """文件测试模式 - 使用新的模型目录方式"""
    file_path = ["screenshots/test_data_20250725201844/test_data_20250725201844_auto_screenshot_20250725_202006_data.csv",
                 "screenshots/test_data_20250725201844/test_data_20250725201844_auto_screenshot_20250725_202004_data.csv",
                 "screenshots/test_data_20250725201844/test_data_20250725201844_auto_screenshot_20250725_201953_data.csv",
                 ]

    model_dir = "models/model_FiberMaterialResNet_inputLength_60_stepSize_2_numSamplePerChunk[48, 60, 64]_prepareMode_uni_baseline_std_left_15_right_20_zooms_[0.8, 1, 1.2]_numEpochs_60"

    data_processor = OpticalFiberDataProcessor(
        model_dirs=model_dir,
        mode="file",
        file_path=file_path,
        enable_visualization=True
    )
    data_processor.data_processor()


def multi_model_test():
    """多模型测试 - 每个模型使用各自的预处理模式"""
    file_path = ["data/raw/AlphaBet_P/AlphaBet_P_auto_screenshot_20250608_195840_data.csv",
                 "AlphaBet_D_Number_4_auto_screenshot_20250608_211605_data.csv"]

    model_dirs = [
        "models/model_FiberMaterialCNNImproved_inputLength_70_stepSize_2_numSamplePerChunk[50, 60, 70]_prepareMode_normalize_zooms_[1]_numEpochs_60",
        "models/model_FiberMaterialCNNDeeper_inputLength_70_stepSize_2_numSamplePerChunk[50, 60, 70]_prepareMode_normalize_zooms_[1]_numEpochs_60",
        "models/model_CurvePatternCNN_inputLength_70_stepSize_2_numSamplePerChunk[50, 60, 70]_prepareMode_normalize_zooms_[1]_numEpochs_60",
    ]

    data_processor = OpticalFiberDataProcessor(
        model_dirs=model_dirs,
        mode="file",
        file_path=file_path,
        enable_visualization=True
        # 不指定 uniform_filter_modes，让每个模型使用自己的预处理方式
    )
    data_processor.data_processor()


def multi_model_test_uniform():
    """多模型测试 - 强制使用统一的预处理模式"""
    file_path = ["data/big/AlphaBet_L/AlphaBet_L_auto_screenshot_20250608_200409_data.csv"]

    model_dirs = [
        "models/model_FiberMaterialCNNDeeper_inputLength_60_stepSize_2_numSamplePerChunk[60]_prepareMode_uni_baseline_left_30_right_10_zooms_[1]_numEpochs_60",
        "models/model_FiberMaterialCNNImproved_inputLength_70_stepSize_2_numSamplePerChunk[50, 60, 70]_prepareMode_normalize_zooms_[1]_numEpochs_60",
        "models/model_FiberMaterialCNN_inputLength_70_stepSize_2_numSamplePerChunk[50, 60, 70]_prepareMode_normalize_zooms_[1]_numEpochs_60",
    ]

    data_processor = OpticalFiberDataProcessor(
        model_dirs=model_dirs,
        mode="file",
        file_path=file_path,
        enable_visualization=True,
        # uniform_filter_modes=["std"]  # 强制所有模型使用 normalize 预处理
    )
    data_processor.data_processor()


if __name__ == "__main__":
    sensor_monitor(large_ui_mode=True)
    # file_test()
    # multi_model_test()
    # multi_model_test_uniform()

    # TODO 把原来的展示三种预处理模式结果改为展示三个模型的（预处理结果？或者别的什么的，比如那个帅帅的三维图）
    # TODO 增加一个预处理模式来模拟此类行为：对于同一个分类，如果与其原始数据1比较，原始数据2可能表现为其第一、第二条曲线“凹”的程度相比较大，
    #  第四、第五条曲线“凹”的程度相比较小，而原始数据3表现可能为1、2、3条凹的程度小，4、5较大这样的情况