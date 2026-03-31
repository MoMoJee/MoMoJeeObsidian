import torch
import torch.nn as nn
import torch.nn.functional as F
from torch.utils.data import DataLoader, Dataset
from sklearn.preprocessing import LabelEncoder
import pandas as pd
import numpy as np
import os
import socket



# TODO 运行中数据形状传给的错误处理
# TODO 智能读文件

# 定义模型结构
# TODO 换模型改这里就行
class FiberMaterialCNN(nn.Module):
    def __init__(self, input_channels, num_classes, input_length=200):
        super(FiberMaterialCNN, self).__init__()
        self.conv1 = nn.Conv1d(in_channels=input_channels, out_channels=64, kernel_size=3, stride=1, padding=1)
        self.conv2 = nn.Conv1d(in_channels=64, out_channels=128, kernel_size=3, stride=1, padding=1)
        self.conv3 = nn.Conv1d(in_channels=128, out_channels=256, kernel_size=3, stride=1, padding=1)
        self.pool = nn.MaxPool1d(kernel_size=2, stride=2)
        # 计算全连接层的输入大小
        output_length = input_length // (2 ** 3)  # 三次池化，每次池化长度减半
        self.fc1 = nn.Linear(256 * output_length, 128)
        self.fc2 = nn.Linear(128, num_classes)
        self.bn1 = nn.BatchNorm1d(64)
        self.bn2 = nn.BatchNorm1d(128)
        self.bn3 = nn.BatchNorm1d(256)
        self.dropout = nn.Dropout(0.5)

    def forward(self, x):
        x = x.permute(0, 2, 1)
        x = self.pool(F.relu(self.bn1(self.conv1(x))))
        x = self.pool(F.relu(self.bn2(self.conv2(x))))
        x = self.pool(F.relu(self.bn3(self.conv3(x))))
        x = x.view(x.size(0), -1)
        x = F.relu(self.fc1(x))
        x = self.dropout(x)
        x = self.fc2(x)
        return x


# 定义模型（优化后的模型结构）
class FiberMaterialCNNDeeper(nn.Module):
    def __init__(self, input_channels, num_classes, input_length=200):
        super(FiberMaterialCNNDeeper, self).__init__()

        # 原有卷积层保持不变
        self.conv1 = nn.Conv1d(in_channels=input_channels, out_channels=64, kernel_size=3, stride=1, padding=1)
        self.bn1 = nn.BatchNorm1d(64)
        self.pool1 = nn.MaxPool1d(kernel_size=2, stride=2)

        self.conv2 = nn.Conv1d(in_channels=64, out_channels=128, kernel_size=3, stride=1, padding=1)
        self.bn2 = nn.BatchNorm1d(128)
        self.pool2 = nn.MaxPool1d(kernel_size=2, stride=2)

        self.conv3 = nn.Conv1d(in_channels=128, out_channels=256, kernel_size=3, stride=1, padding=1)
        self.bn3 = nn.BatchNorm1d(256)
        self.pool3 = nn.MaxPool1d(kernel_size=2, stride=2)

        self.conv4 = nn.Conv1d(in_channels=256, out_channels=512, kernel_size=3, stride=1, padding=1)
        self.bn4 = nn.BatchNorm1d(512)
        self.pool4 = nn.MaxPool1d(kernel_size=2, stride=2)

        output_length = input_length // (2 ** 4)
        self.fc1 = nn.Linear(512 * output_length, 256)
        self.fc2 = nn.Linear(256, num_classes)

        # 增强的Dropout层
        self.dropout_conv = nn.Dropout(0.15)  # 卷积层后的轻量dropout
        self.dropout_fc1 = nn.Dropout(0.5)  # 第一个全连接层后的dropout
        self.dropout_fc2 = nn.Dropout(0.3)  # 第二个全连接层前的dropout

    def forward(self, x):
        x = x.permute(0, 2, 1)

        # 每个卷积块后添加dropout
        x = self.pool1(F.relu(self.bn1(self.conv1(x))))
        x = self.dropout_conv(x)

        x = self.pool2(F.relu(self.bn2(self.conv2(x))))
        x = self.dropout_conv(x)

        x = self.pool3(F.relu(self.bn3(self.conv3(x))))
        x = self.dropout_conv(x)

        x = self.pool4(F.relu(self.bn4(self.conv4(x))))
        x = self.dropout_conv(x)

        # 全连接层with enhanced dropout
        x = x.view(x.size(0), -1)
        x = F.relu(self.fc1(x))
        x = self.dropout_fc1(x)
        x = self.fc2(x)
        x = self.dropout_fc2(x)  # 最后一层前也加dropout

        return x


# 改进版本1：多尺度特征提取 + 注意力机制
class FiberMaterialCNNImproved(nn.Module):
    def __init__(self, input_channels, num_classes, input_length=200):
        super(FiberMaterialCNNImproved, self).__init__()

        # 多尺度卷积层，捕获不同尺度的"凹"特征
        self.conv1_3 = nn.Conv1d(input_channels, 32, kernel_size=3, padding=1)
        self.conv1_5 = nn.Conv1d(input_channels, 32, kernel_size=5, padding=2)
        self.conv1_7 = nn.Conv1d(input_channels, 32, kernel_size=7, padding=3)
        self.bn1 = nn.BatchNorm1d(96)  # 32*3 = 96
        self.pool1 = nn.MaxPool1d(kernel_size=2, stride=2)

        # 通道注意力机制
        self.channel_attention = nn.Sequential(
            nn.AdaptiveAvgPool1d(1),
            nn.Conv1d(96, 24, 1),
            nn.ReLU(),
            nn.Conv1d(24, 96, 1),
            nn.Sigmoid()
        )

        # 深度可分离卷积，减少参数量
        self.depthwise_conv2 = nn.Conv1d(96, 96, kernel_size=3, padding=1, groups=96)
        self.pointwise_conv2 = nn.Conv1d(96, 128, kernel_size=1)
        self.bn2 = nn.BatchNorm1d(128)
        self.pool2 = nn.MaxPool1d(kernel_size=2, stride=2)

        self.depthwise_conv3 = nn.Conv1d(128, 128, kernel_size=3, padding=1, groups=128)
        self.pointwise_conv3 = nn.Conv1d(128, 256, kernel_size=1)
        self.bn3 = nn.BatchNorm1d(256)
        self.pool3 = nn.MaxPool1d(kernel_size=2, stride=2)

        # 残差连接
        self.conv4 = nn.Conv1d(256, 512, kernel_size=3, padding=1)
        self.conv4_residual = nn.Conv1d(256, 512, kernel_size=1)  # 用于残差连接
        self.bn4 = nn.BatchNorm1d(512)
        self.pool4 = nn.MaxPool1d(kernel_size=2, stride=2)

        # 全局平均池化替代固定大小的全连接层
        self.global_avg_pool = nn.AdaptiveAvgPool1d(1)

        # 更深的分类器
        self.classifier = nn.Sequential(
            nn.Linear(512, 256),
            nn.ReLU(),
            nn.Dropout(0.5),
            nn.Linear(256, 128),
            nn.ReLU(),
            nn.Dropout(0.3),
            nn.Linear(128, num_classes)
        )

    def forward(self, x):
        x = x.permute(0, 2, 1)

        # 多尺度特征提取
        x1 = self.conv1_3(x)
        x2 = self.conv1_5(x)
        x3 = self.conv1_7(x)
        x = torch.cat([x1, x2, x3], dim=1)
        x = self.pool1(F.relu(self.bn1(x)))

        # 通道注意力
        attention = self.channel_attention(x)
        x = x * attention

        # 深度可分离卷积
        x = self.depthwise_conv2(x)
        x = self.pointwise_conv2(x)
        x = self.pool2(F.relu(self.bn2(x)))

        x = self.depthwise_conv3(x)
        x = self.pointwise_conv3(x)
        x = self.pool3(F.relu(self.bn3(x)))

        # 残差连接
        residual = self.conv4_residual(x)
        x = self.conv4(x)
        x = x + residual
        x = self.pool4(F.relu(self.bn4(x)))

        # 全局平均池化
        x = self.global_avg_pool(x)
        x = x.view(x.size(0), -1)

        # 分类器
        x = self.classifier(x)
        return x


# 改进版本2：专门针对曲线"凹"特征的模型
class CurvePatternCNN(nn.Module):
    def __init__(self, input_channels, num_classes, input_length=200):
        super(CurvePatternCNN, self).__init__()

        # 特征提取backbone
        self.backbone = nn.Sequential(
            # 第一层：捕获局部模式
            nn.Conv1d(input_channels, 64, kernel_size=3, padding=1),
            nn.BatchNorm1d(64),
            nn.ReLU(),
            nn.Conv1d(64, 64, kernel_size=3, padding=1),
            nn.BatchNorm1d(64),
            nn.ReLU(),
            nn.MaxPool1d(2),

            # 第二层：捕获中等尺度模式
            nn.Conv1d(64, 128, kernel_size=5, padding=2),
            nn.BatchNorm1d(128),
            nn.ReLU(),
            nn.Conv1d(128, 128, kernel_size=5, padding=2),
            nn.BatchNorm1d(128),
            nn.ReLU(),
            nn.MaxPool1d(2),

            # 第三层：捕获大尺度模式
            nn.Conv1d(128, 256, kernel_size=7, padding=3),
            nn.BatchNorm1d(256),
            nn.ReLU(),
            nn.Conv1d(256, 256, kernel_size=7, padding=3),
            nn.BatchNorm1d(256),
            nn.ReLU(),
            nn.MaxPool1d(2),
        )

        # 特征融合层
        self.feature_fusion = nn.Sequential(
            nn.Conv1d(256, 512, kernel_size=3, padding=1),
            nn.BatchNorm1d(512),
            nn.ReLU(),
            nn.AdaptiveAvgPool1d(1)
        )

        # 分类头
        self.classifier = nn.Sequential(
            nn.Linear(512, 256),
            nn.ReLU(),
            nn.Dropout(0.5),
            nn.Linear(256, 128),
            nn.ReLU(),
            nn.Dropout(0.3),
            nn.Linear(128, num_classes)
        )

    def forward(self, x):
        x = x.permute(0, 2, 1)

        # 特征提取
        features = self.backbone(x)

        # 特征融合
        fused_features = self.feature_fusion(features)
        fused_features = fused_features.view(fused_features.size(0), -1)

        # 分类
        output = self.classifier(fused_features)
        return output


# 改进版本3：带有跳跃连接的ResNet风格模型
class FiberMaterialResNet(nn.Module):
    def __init__(self, input_channels, num_classes, input_length=200):
        super(FiberMaterialResNet, self).__init__()

        # 初始卷积层
        self.initial_conv = nn.Sequential(
            nn.Conv1d(input_channels, 64, kernel_size=7, stride=2, padding=3),
            nn.BatchNorm1d(64),
            nn.ReLU(),
            nn.MaxPool1d(kernel_size=3, stride=2, padding=1)
        )

        # 残差块
        self.res_block1 = self._make_res_block(64, 64, 2)
        self.res_block2 = self._make_res_block(64, 128, 2, stride=2)
        self.res_block3 = self._make_res_block(128, 256, 2, stride=2)
        self.res_block4 = self._make_res_block(256, 512, 2, stride=2)

        # 全局平均池化
        self.global_avg_pool = nn.AdaptiveAvgPool1d(1)

        # 最终分类器
        self.fc = nn.Linear(512, num_classes)

    def _make_res_block(self, in_channels, out_channels, num_blocks, stride=1):
        layers = []
        # 第一个块可能需要调整维度
        layers.append(ResidualBlock(in_channels, out_channels, stride))
        # 后续块维度相同
        for _ in range(1, num_blocks):
            layers.append(ResidualBlock(out_channels, out_channels))
        return nn.Sequential(*layers)

    def forward(self, x):
        x = x.permute(0, 2, 1)

        x = self.initial_conv(x)
        x = self.res_block1(x)
        x = self.res_block2(x)
        x = self.res_block3(x)
        x = self.res_block4(x)

        x = self.global_avg_pool(x)
        x = x.view(x.size(0), -1)
        x = self.fc(x)
        return x


class ResidualBlock(nn.Module):
    def __init__(self, in_channels, out_channels, stride=1):
        super(ResidualBlock, self).__init__()

        self.conv1 = nn.Conv1d(in_channels, out_channels, kernel_size=3, stride=stride, padding=1)
        self.bn1 = nn.BatchNorm1d(out_channels)
        self.conv2 = nn.Conv1d(out_channels, out_channels, kernel_size=3, stride=1, padding=1)
        self.bn2 = nn.BatchNorm1d(out_channels)

        # 跳跃连接
        self.shortcut = nn.Sequential()
        if stride != 1 or in_channels != out_channels:
            self.shortcut = nn.Sequential(
                nn.Conv1d(in_channels, out_channels, kernel_size=1, stride=stride),
                nn.BatchNorm1d(out_channels)
            )

    def forward(self, x):
        residual = self.shortcut(x)

        out = F.relu(self.bn1(self.conv1(x)))
        out = self.bn2(self.conv2(out))
        out += residual
        out = F.relu(out)
        return out



# 定义测试数据集结构
class TestDataset(Dataset):
    def __init__(self, file_path):
        self.data = pd.read_csv(file_path, nrows=200).drop(columns=['Time (s)']).values

    def __len__(self):
        return 1  # 假设每个文件只包含一个样本

    def __getitem__(self, idx):
        return torch.tensor(self.data, dtype=torch.float32)


# 加载数据
def load_raw_data(data_path='data/raw'):
    """
    从 raw 文件夹加载数据，每个子文件夹的名称作为标签
    只读取每个 CSV 文件的前 200 行数据
    """
    data = []  # 用于存储所有数据
    labels = []  # 用于存储所有标签

    # 遍历 raw 文件夹下的每个子文件夹
    for folder_name in os.listdir(data_path):
        folder_path = os.path.join(data_path, folder_name)

        # 确保是文件夹
        if os.path.isdir(folder_path):
            # 遍历文件夹中的每个 CSV 文件
            for file_name in os.listdir(folder_path):
                if file_name.endswith('.csv'):
                    file_path = os.path.join(folder_path, file_name)
                    # 读取 CSV 文件的前 10 行
                    df = pd.read_csv(file_path, nrows=10)  # TODO 10不应该硬编码的。这里只是读取文件夹信息作为标签名，不涉及数据处理，所以其实怎么写都行
                    # TODO 这里改写为基于传入的模型所在目录，读取目录下的映射对应文件来实现标签获取。此外要改一改模型存储文件夹的格式，里面还要包含模型配置参数之类的
                    # 去掉时间戳列，只保留数值列
                    df = df.drop(columns=['Time (s)'])

                    # 将数据和标签添加到列表中
                    data.append(df.values)  # 将数据转换为 NumPy 数组
                    labels.append(folder_name)  # 文件夹名称作为标签
    return np.array(data), np.array(labels)

# 获取类别名称
def get_class_names(data_path='data/raw'):
    class_names = [name for name in os.listdir(data_path) if os.path.isdir(os.path.join(data_path, name))]
    return class_names


# 模型测试
def test_model(model, device, test_loader, label_encoder):
    model.eval()
    predictions = []
    confidences = []  # 新增一个列表来存储每个预测的置信度
    with torch.no_grad():
        for data in test_loader:
            data = data.to(device)
            output = model(data)
            # 计算置信度（概率分布）
            probabilities = torch.softmax(output, dim=1)
            # 获取每个样本的最大置信度及其对应的类别索引
            max_confidence, predicted = torch.max(probabilities, dim=1)
            predictions.append(predicted.item())
            confidences.append(max_confidence.item())
    # 将整数标签映射回类别名称
    predicted_classes = label_encoder.inverse_transform(predictions)
    # 返回预测的类别和对应的置信度
    return predicted_classes, confidences


if __name__ == "__main__":
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(("localhost", 65432))
        s.listen()
        data_path = 'data/raw'
        data, labels = load_raw_data(data_path)
        label_encoder = LabelEncoder()
        labels_encoded = label_encoder.fit_transform(labels)
        # 输出数据和标签的形状
        print("Data shape:", data.shape)  # (样本数量, 时间步长, 特征数量)
        print("Labels shape:", labels.shape)  # (样本数量,)
        print("Unique labels:", np.unique(labels))  # 打印所有唯一标签
        # 加载模型
        device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        model = FiberMaterialCNN(input_channels=4, num_classes=8, input_length=200).to(device)
        model.load_state_dict(torch.load("OldFiles/best_model_cnn.pth"))
        model.eval()  # 设置为评估模式
        print("Model loaded successfully.")

        while True:
            conn, addr = s.accept()
            with conn:
                csv_path = conn.recv(1024).decode()

                # 下面就是神经网络测试

                test_file_path = csv_path  # 替换为你的测试文件路径
                test_dataset = TestDataset(test_file_path)
                test_loader = DataLoader(test_dataset, batch_size=1, shuffle=False)
                predicted_classes = test_model(model, device, test_loader, label_encoder)
                print("Predicted class:", predicted_classes[0])