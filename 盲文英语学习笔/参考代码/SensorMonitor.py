"""
SensorMonitor 13.4
传感器监视器 13.4
2025.8.21
"""

import sys
import pyqtgraph as pg
from PyQt5.QtCore import Qt
from pyqtgraph.Qt import QtCore
import serial
from PyQt5.QtWidgets import QApplication, QListWidget, QListWidgetItem, QAbstractItemView, QMainWindow, QPushButton, QVBoxLayout, QWidget, QMessageBox, QDialog, QFormLayout, QComboBox, QLineEdit, QLabel, QHBoxLayout, QSlider
from pyqtgraph import PlotWidget
import re
import time
import numpy as np
from datetime import datetime
from collections import deque
import cv2
import os
import socket
import json
from pathlib import Path
import multiprocessing
import queue
from data_generator import run_data_generator
from serial_interface import create_serial_interface


def load_config():
    """加载配置文件，不存在时返回空字典"""
    try:
        if CONFIG_PATH.exists():
            with open(CONFIG_PATH, 'r', encoding='utf-8') as f:
                return json.load(f)
        return {}
    except Exception as e:
        print(f"加载配置文件失败: {str(e)}")
        return {}

def save_config(config):
    """保存配置文件"""
    try:
        with open(CONFIG_PATH, 'w', encoding='utf-8') as f:
            json.dump(config, f, ensure_ascii=False, indent=2)
    except Exception as e:
        print(f"保存配置文件失败: {str(e)}")


# 这里定义的是滤波函数们
def mean_filter(data, kernel_size=3):
    """均值滤波"""
    filtered = np.convolve(data, np.ones(kernel_size)/kernel_size, mode='same')
    return filtered

def gaussian_filter(data, kernel_size=3, sigma=1):
    """高斯滤波"""
    x = np.linspace(-kernel_size//2, kernel_size//2, kernel_size)
    gauss = np.exp(-x**2 / (2 * sigma**2))
    gauss /= gauss.sum()
    filtered = np.convolve(data, gauss, mode='same')
    return filtered

def median_filter(data, kernel_size=3):
    """中值滤波"""
    filtered = np.zeros_like(data)
    pad = kernel_size // 2
    data_padded = np.pad(data, pad, mode='edge')
    for i in range(len(data)):
        filtered[i] = np.median(data_padded[i:i+kernel_size])
    return filtered


class SettingsDialog(QDialog):
    def __init__(self, current_settings=None, parent=None, is_first_run=False):
        super().__init__(parent)
        # 加载配置文件（仅在首次运行时合并）
        self.default_config = load_config()
        if is_first_run and not current_settings:
            current_settings = self.default_config

        self.setWindowTitle("设置")
        self.resize(400, 400)  # 调整窗口高度以适应新控件

        self.layout = QFormLayout(self)

        # 主文件名设置
        self.filename_label = QLabel("数据主文件名:")
        self.filename_edit = QLineEdit()
        self.default_file_name = f"test_data_{datetime.now().strftime('%Y%m%d%H%M%S')}"
        self.filename_edit.setText(self.default_file_name)

        # 首次运行时允许编辑，非首次运行时禁用
        if not is_first_run:
            self.filename_edit.setEnabled(False)
            if current_settings and 'main_filename' in current_settings:
                self.filename_edit.setText(current_settings['main_filename'])

        self.layout.addRow(self.filename_label, self.filename_edit)

        # 连接类型选择
        self.connection_type_label = QLabel("连接类型:")
        self.connection_type_combo = QComboBox()
        self.connection_type_combo.addItems(['标准串口', '蓝牙串口'])
        if current_settings and 'connection_type' in current_settings:
            connection_type_text = '蓝牙串口' if current_settings['connection_type'] == 'bluetooth' else '标准串口'
            self.connection_type_combo.setCurrentText(connection_type_text)
        else:
            self.connection_type_combo.setCurrentText('标准串口')
        self.layout.addRow(self.connection_type_label, self.connection_type_combo)

        # 串口号
        self.com_label = QLabel("串口号:")
        self.com_combo = QComboBox()
        self.com_combo.addItems(['COM1', 'COM2', 'COM3', 'COM4', 'COM5', 'COM6', 'COM7', 'COM8', 'COM9', 'COM10', 'COM11', 'COM12', 'COM13'])
        if current_settings and 'serial_port' in current_settings:
            self.com_combo.setCurrentText(current_settings['serial_port'])
        self.layout.addRow(self.com_label, self.com_combo)

        # 波特率
        self.baud_label = QLabel("波特率:")
        self.baud_combo = QComboBox()
        self.baud_combo.addItems(['9600', '115200', '19200', '38400'])

        # 蓝牙设备名
        self.ble_device_label = QLabel("蓝牙设备名:")
        self.ble_device_edit = QLineEdit()
        self.ble_device_edit.setText(current_settings.get('ble_device_name', 'ESP32C3-Data') if current_settings else 'ESP32C3-Data')
        self.layout.addRow(self.ble_device_label, self.ble_device_edit)

        # 根据连接类型显示/隐藏相关控件
        self.connection_type_combo.currentTextChanged.connect(self.update_connection_ui)  # type: ignore
        self.update_connection_ui()

        if current_settings and 'baudrate' in current_settings:
            self.baud_combo.setCurrentText(str(current_settings['baudrate']))
        else:
            self.baud_combo.setCurrentText('115200')
        self.layout.addRow(self.baud_label, self.baud_combo)

        # 曲线条数
        self.curves_label = QLabel("曲线组数量:")
        self.curves_combo = QComboBox()
        self.curves_combo.addItems(['1', '2', '3', '4', '5', '6', '7', '8'])
        if current_settings and 'num_curve_groups' in current_settings:
            self.curves_combo.setCurrentText(str(current_settings['num_curve_groups']))
        else:
            self.curves_combo.setCurrentText('4')
        self.layout.addRow(self.curves_label, self.curves_combo)

        # 是否使用模拟数据
        self.sim_label = QLabel("使用模拟数据:")
        self.sim_combo = QComboBox()
        self.sim_combo.addItems(['是', '否'])
        if current_settings and 'use_simulated_data' in current_settings:
            self.sim_combo.setCurrentText('是' if current_settings['use_simulated_data'] else '否')
        else:
            self.sim_combo.setCurrentText('是')
        self.layout.addRow(self.sim_label, self.sim_combo)

        # 滤波类型选择
        self.filter_label = QLabel("选择滤波类型:")
        self.filter_list = QListWidget()
        self.filter_list.setSelectionMode(QAbstractItemView.MultiSelection)
        filters = ['原数据', '均值滤波', '高斯滤波', '中值滤波']
        for filter_name in filters:
            item = QListWidgetItem(filter_name)
            item.setSelected(True if filter_name == '原数据' else False)
            self.filter_list.addItem(item)
        self.layout.addRow(self.filter_label, self.filter_list)

        # 新增神经网络交互选项
        self.nn_label = QLabel("启用神经网络交互:")
        self.nn_combo = QComboBox()
        self.nn_combo.addItems(['是', '否'])
        if current_settings and 'neural_net_enabled' in current_settings:
            self.nn_combo.setCurrentText('是' if current_settings['neural_net_enabled'] else '否')
        else:
            self.nn_combo.setCurrentText('否')
        self.layout.addRow(self.nn_label, self.nn_combo)

        # 校验功能选项
        self.calibration_label = QLabel("启用数据校验:")
        self.calibration_combo = QComboBox()
        self.calibration_combo.addItems(['关闭', '启用'])
        if current_settings and 'calibration_enabled' in current_settings:
            self.calibration_combo.setCurrentText('启用' if current_settings['calibration_enabled'] else '关闭')
        else:
            self.calibration_combo.setCurrentText('关闭')
        self.layout.addRow(self.calibration_label, self.calibration_combo)

        # 基准曲线选择
        self.reference_curve_label = QLabel("基准曲线:")
        self.reference_curve_combo = QComboBox()
        num_curves = int(self.curves_combo.currentText())
        self.reference_curve_combo.addItems([f'曲线{i+1}' for i in range(num_curves)])
        if current_settings and 'reference_curve_index' in current_settings:
            if current_settings['reference_curve_index'] < num_curves:
                self.reference_curve_combo.setCurrentIndex(current_settings['reference_curve_index'])
        self.layout.addRow(self.reference_curve_label, self.reference_curve_combo)

        # 标定精度设置
        self.tolerance_label = QLabel("标定精度(1-10):")
        self.tolerance_combo = QComboBox()
        self.tolerance_combo.addItems(['1', '2', '3', '4', '5'])  # 1最精细，5较粗糙
        if current_settings and 'calibration_tolerance' in current_settings:
            tolerance_str = str(current_settings['calibration_tolerance'])
            if tolerance_str in ['1', '2', '3', '4', '5']:
                self.tolerance_combo.setCurrentText(tolerance_str)
        else:
            self.tolerance_combo.setCurrentText('1')  # 默认最精细
        self.layout.addRow(self.tolerance_label, self.tolerance_combo)

        # 当曲线数量变化时更新基准曲线选项
        self.curves_combo.currentTextChanged.connect(self.update_reference_curve_options)  # type: ignore

        # 确定按钮
        self.ok_button = QPushButton("确定")
        self.ok_button.clicked.connect(self.accept)  # type: ignore
        self.layout.addRow(self.ok_button)

    def update_connection_ui(self):
        """根据连接类型显示/隐藏相关控件"""
        is_bluetooth = self.connection_type_combo.currentText() == '蓝牙串口'

        # 标准串口相关控件
        self.com_label.setVisible(not is_bluetooth)
        self.com_combo.setVisible(not is_bluetooth)
        self.baud_label.setVisible(not is_bluetooth)
        self.baud_combo.setVisible(not is_bluetooth)

        # 蓝牙相关控件
        self.ble_device_label.setVisible(is_bluetooth)
        self.ble_device_edit.setVisible(is_bluetooth)

    def update_reference_curve_options(self):
        """当曲线数量变化时更新基准曲线选项"""
        num_curves = int(self.curves_combo.currentText())
        self.reference_curve_combo.clear()
        self.reference_curve_combo.addItems([f'曲线{i+1}' for i in range(num_curves)])

    def get_settings(self):
        selected_filters = []
        for index in range(self.filter_list.count()):
            item = self.filter_list.item(index)
            if item.isSelected():
                selected_filters.append(item.text())

        # 确定连接类型
        connection_type = 'bluetooth' if self.connection_type_combo.currentText() == '蓝牙串口' else 'standard'

        return {
            'main_filename': self.filename_edit.text(),
            'connection_type': connection_type,
            'serial_port': self.com_combo.currentText(),
            'ble_device_name': self.ble_device_edit.text(),
            'baudrate': int(self.baud_combo.currentText()),
            'num_curve_groups': int(self.curves_combo.currentText()),
            'use_simulated_data': self.sim_combo.currentText() == '是',
            'selected_filters': selected_filters,
            'neural_net_enabled': self.nn_combo.currentText() == '是',
            'calibration_enabled': self.calibration_combo.currentText() == '启用',
            'reference_curve_index': self.reference_curve_combo.currentIndex(),
            'calibration_tolerance': int(self.tolerance_combo.currentText()),
        }

class RealTimePlot(QMainWindow):
    def __init__(self):
        super().__init__()

        # 加载配置文件
        self.config = load_config()

        # 初始化设置（优先使用配置，否则用默认值）
        self.settings = {
            'serial_port': self.config.get('serial_port', 'COM3'),
            'connection_type': self.config.get('connection_type', 'standard'),
            'ble_device_name': self.config.get('ble_device_name', 'ESP32C3-Data'),
            'baudrate': self.config.get('baudrate', 115200),
            'num_curve_groups': self.config.get('num_curve_groups', 4),
            'use_simulated_data': self.config.get('use_simulated_data', False),
            'selected_filters': self.config.get('selected_filters', ['原数据']),
            'neural_net_enabled': self.config.get('neural_net_enabled', False),
            'main_filename': self.config.get('main_filename', "default"),
            'calibration_enabled': self.config.get('calibration_enabled', False),
            'reference_curve_index': self.config.get('reference_curve_index', 0),
            'calibration_tolerance': self.config.get('calibration_tolerance', 1),
            'fake_csvs': self.config.get('fake_csvs', None),
        }

        # 更新校验功能设置
        self.calibration_enabled = self.settings['calibration_enabled']
        self.reference_curve_index = self.settings['reference_curve_index']
        self.calibration_tolerance = self.settings['calibration_tolerance']

        self.dynamic_y_enabled = self.config.get('dynamic_y_enabled', False)  # 动态Y轴
        self.stats_visible = False      # 统计线默认关闭

        # 添加Y轴范围控制参数
        self.min_y = 0
        self.max_y = 4096

        # 模拟数据计数器初始化
        self.simulated_data_counter = 0

        # 记录程序开始时间
        self.start_time = time.time()

        # 初始化主文件名
        self.main_filename = "default"

        # 默认窗口数据长度值
        self.max_window_time = self.config.get('max_window_time', 10)

        # 视频录制相关变量
        self.is_recording = False
        self.video_writer = None
        self.recording_frames = []
        self.recording_data = []
        self.recording_start_time = 0

        # 截图计数器
        self.screenshot_count = 0

        # 自动截取相关设置属性
        self.auto_capture_enabled = False
        # 默认截取时长（秒）
        self.capture_duration = self.config.get('capture_duration', self.max_window_time // 2)

        self.variance_threshold = self.config.get('variance_threshold', 200)  # 微观波动阈值（方差）
        self.detection_mode = self.config.get('detection_mode', "deviation")  # 波动检测模式，"variance" 或 "deviation"
        self.deviation_threshold = self.config.get('deviation_threshold', 500)  # 宏观波动阈值（离差）

        self.capture_left_margin = self.config.get('capture_left_margin', 0.5)  # 向左扩展时间（秒）
        self.capture_right_margin = self.config.get('capture_right_margin', 0.5)  # 向右扩展时间（秒）
        self.min_volatile_duration = self.config.get('min_volatile_duration', 1.0)  # 最小波动时长（秒）

        # 自动截取相关计算属性
        self.baseline_window_size = 10  # 宏观波动基线计算窗口大小（区块数）（我没懂这个参数是怎么运作的，但是设为10可以跑）
        self.time_blocks = []          # 存储时间区块的列表，格式：{"start": t1, "end": t2, "state": "volatile/stable"}
        self.block_interval = 0.2      # 区块时间间隔（秒）
        self.last_clean_time = 0       #  清理区块用


        self.last_detection_time = time.time()  # 注意 last_detection_time 这个参数用的是绝对时间


        # 模拟数据模式控制参数
        self.sim_amplitude = 128  # 默认振幅
        self.sim_noise_level = 16  # 默认噪声
        self.sim_volatile_mode = True  # 当前是否为波动模式
        self.fake_csvs = self.config.copy().get('fake_csvs', None)  # 模拟数据时使用的CSV路径们，运行时按一次换下一个
        self.use_fake_csvs = False

        # 多进程相关属性
        self.data_generator_process = None
        self.data_queue = None
        self.control_queue = None
        self.simulation_modes = ["stable", "volatile", "input"]  # 三种模式
        self.current_sim_mode_index = 2  # 默认从 input 开始

        # 校验功能相关属性
        self.calibration_enabled = False  # 是否启用校验功能
        self.reference_curve_index = 0    # 基准曲线索引（默认第0条）
        self.is_calibrating = False       # 标定进行中标志
        self.calibration_data = {         # 标定数据存储
            'baseline': [],               # 无压力时的基准值
            'mapping': {}                 # 基准值到其他曲线值的映射
        }
        self.baseline_values = []         # 无压力时的基准值

        # 标定精度控制参数
        self.calibration_tolerance = 1   # 标定容差（越小越精细）
        self.max_mapping_points = 2000   # 最大映射点数量（防止内存过载）
        self.last_calibration_ref = None # 上次记录的基准值
        self.calibration_sample_interval = 5  # 采样间隔（每5个数据点采样一次）
        self.calibration_sample_counter = 0   # 采样计数器

        # 首次显示设置对话框
        self.show_settings_dialog(first_run=True)

        # 更新校验功能设置（在设置对话框完成后）
        self.calibration_enabled = self.settings['calibration_enabled']
        self.reference_curve_index = self.settings['reference_curve_index']

        # 加载标定数据
        if self.calibration_enabled:
            self.load_calibration_data()

        # 初始化串口/蓝牙连接
        if not self.settings['use_simulated_data']:
            try:
                if self.settings['connection_type'] == 'bluetooth':
                    # 使用蓝牙连接
                    self.ser = create_serial_interface(
                        'bluetooth',
                        device_name=self.settings['ble_device_name']
                    )
                else:
                    # 使用标准串口连接
                    self.ser = create_serial_interface(
                        'standard',
                        port=self.settings['serial_port'],
                        baudrate=self.settings['baudrate']
                    )

                self.ser.open()

            except Exception as e:
                QMessageBox.critical(self, "连接错误", f"无法建立连接: {e}")
                sys.exit(1)


        colors = [
            (255, 0, 0),    # 红色
            (255, 165, 20),  # 橙色
            (255, 255, 0),  # 黄色
            (0, 255, 0),  # 绿色
            (0, 255, 255),  # 青色
            (0, 0, 255),  # 蓝色
            (255, 0, 255),  # 紫色
            (255, 255, 255),  # 白色
        ]

        # 帧率
        self.video_fps = 30  # 视频固定帧率
        self.slider_label = None  # 用于显示当前值的标签
        self.frame_interval = (1000 // self.video_fps) / 1000  # 33ms
        self.last_frame_time = 0  # 新增时间戳记录
        self.x_data = deque()
        self.curve_groups = []
        for _ in range(self.settings['num_curve_groups']):
            self.curve_groups.append({
                'source_data': deque(),
                'filtered_data': {filter_name: deque() for filter_name in self.settings['selected_filters']},
                'color': colors[_]
            })

        # 根据设置的文件名打开文件
        self.file = open(f'sensor_datas/{self.settings["main_filename"]}_all_data.csv', 'w')

        # 创建主窗口
        self.init_ui()

        # 在UI创建后，如果启用了校验功能，则添加校验按钮
        if self.calibration_enabled:
            self.add_calibration_buttons()

        # 新增统计线存储结构
        self.stat_lines = []
        for i in range(self.settings['num_curve_groups']):
            color = self.curve_groups[i]['color']
            # 创建三条统计线（最大值、最小值、平均值）
            stats = {
                'max': pg.InfiniteLine(angle=0, pen=pg.mkPen(color=color, width=1, style=QtCore.Qt.DashLine)),  # type: ignore
                'min': pg.InfiniteLine(angle=0, pen=pg.mkPen(color=color, width=1, style=QtCore.Qt.DashLine)),  # type: ignore
                'mean': pg.InfiniteLine(angle=0, pen=pg.mkPen(color=color, width=2, style=QtCore.Qt.DotLine))  # type: ignore
            }
            for line in stats.values():
                self.plot_widget.addItem(line)
                line.setVisible(False)
            self.stat_lines.append(stats)

        # 连接视图范围变化信号
        self.plot_widget.sigRangeChanged.connect(self.update_stat_lines)

        # 如果使用模拟数据，启动数据生成进程
        if self.settings['use_simulated_data']:
            self.start_data_generator_process()

        # 设置定时器
        self.timer = QtCore.QTimer(self)
        self.timer.timeout.connect(self.update_plot)  # type: ignore
        self.timer.start(0)  # 刷新时间间隔

        # 数据更新标志
        self.is_paused = False
        self.statusBar().showMessage(f"监视器初始化成功！", 2000)

    def init_ui(self):

        # 主容器使用水平布局
        main_container = QWidget()
        self.main_layout = QHBoxLayout(main_container)

        # 创建窗口
        self.setWindowTitle('AD over Time')

        # 设置窗口大小
        self.resize(2200, 800)  # 调整窗口宽度和高度

        # 创建图表和按钮的布局
        self.left_layout = QVBoxLayout()

        # 创建 PlotWidget
        self.plot_widget = PlotWidget()

        self.plot_widget = pg.PlotWidget(axisItems={'right': pg.AxisItem('right')})
        plot_item = self.plot_widget.getPlotItem()
        plot_item.showAxis('right')
        plot_item.vb.sigYRangeChanged.connect(
            lambda: plot_item.getAxis('right').setRange(*plot_item.vb.viewRange()[1]))

        if self.dynamic_y_enabled:
            pass
        else:
            self.plot_widget.setRange(yRange=(0, 4096), padding=0)
            self.plot_widget.getPlotItem().disableAutoRange(axis='y')  # 保持默认关闭
        self.left_layout.addWidget(self.plot_widget)

        # 初始化曲线
        self.curves = []
        for i in range(self.settings['num_curve_groups']):
            color = self.curve_groups[i]['color']
            # 源曲线
            source_curve = self.plot_widget.plot(pen=pg.mkPen(color=color, width=2, style=QtCore.Qt.SolidLine))  # type: ignore
            self.curves.append(source_curve)
            # 滤波曲线
            for j, filter_name in enumerate(self.settings['selected_filters']):
                if filter_name != '原数据':
                    filtered_curve = self.plot_widget.plot(pen=pg.mkPen(color=color, width=2, style=QtCore.Qt.DashLine))  # type: ignore
                    self.curves.append(filtered_curve)

        # 创建按钮
        self.create_buttons()

        slider_layout = QHBoxLayout()  # 创建水平布局对象
        # 窗口时间标签
        self.slider_label = QLabel(f"显示窗口: {self.max_window_time}秒")
        slider_layout.addWidget(self.slider_label)

        # 时间滑块
        self.time_slider = QSlider(QtCore.Qt.Horizontal)  # type: ignore
        self.time_slider.setMinimum(1)
        self.time_slider.setMaximum(300)
        self.time_slider.setValue(self.max_window_time)
        self.time_slider.setTickInterval(5)
        self.time_slider.valueChanged.connect(self.update_window_time)  # type: ignore
        slider_layout.addWidget(self.time_slider)

        # 将横向时间滑块布局添加到主布局最上方
        self.left_layout.insertLayout(0, slider_layout)

        # 右侧滑块布局
        right_slider_layout = QVBoxLayout()

        # 最大值滑块
        self.max_slider = QSlider(QtCore.Qt.Vertical)  # type: ignore
        self.max_slider.setRange(0, 4096)
        self.max_slider.setValue(self.max_y)
        self.max_slider.valueChanged.connect(self.update_y_range)  # type: ignore

        # 最小值滑块
        self.min_slider = QSlider(QtCore.Qt.Vertical)  # type: ignore
        self.min_slider.setRange(0, 4096)
        self.min_slider.setValue(self.min_y)
        self.min_slider.valueChanged.connect(self.update_y_range)  # type: ignore

        if self.dynamic_y_enabled:
            self.min_slider.setEnabled(False)
            self.max_slider.setEnabled(False)

        # 自动锁定y轴按钮
        self.auto_scale_btn = QPushButton("自动锁定y轴范围")
        self.auto_scale_btn.clicked.connect(self.auto_adjust_y_range)  # type: ignore
        right_slider_layout.addWidget(self.auto_scale_btn)

        self.auto_scale_btn.setStyleSheet("""
            QPushButton {
                background-color: #4682B4;
                color: white;
                border-radius: 3px;
                padding: 5px;
            }
            QPushButton:hover {
                background-color: #5F9EA0;
            }
        """)

        # 标签布局
        label_layout = QHBoxLayout()
        self.min_label = QLabel(f"Min: {self.min_y}")
        self.max_label = QLabel(f"Max: {self.max_y}")
        label_layout.addWidget(self.min_label)
        label_layout.addWidget(self.max_label)
        # 新增状态指示器（添加到右侧布局）
        self.status_panel = QLabel("状态：未监测")
        self.status_panel.setAlignment(QtCore.Qt.AlignCenter)  # type: ignore
        self.status_panel.setStyleSheet("""
            QLabel {
                font-size: 16px;
                font-weight: bold;
                color: #666666;
                border: 2px solid #AAAAAA;
                border-radius: 5px;
                padding: 10px;
            }
        """)


        # 阈值控制滑块（添加到状态面板上方）
        threshold_layout = QVBoxLayout()

        # 微观波动阈值标签
        self.variance_threshold_label = QLabel(f"微观阈值: {self.variance_threshold}")
        self.variance_threshold_label.setAlignment(QtCore.Qt.AlignCenter)  # type: ignore
        # 微观波动阈值滑块
        self.variance_threshold_slider = QSlider(QtCore.Qt.Horizontal)  # type: ignore
        self.variance_threshold_slider.setMinimum(10)  # 最小阈值
        self.variance_threshold_slider.setMaximum(1000)  # 最大阈值
        self.variance_threshold_slider.setValue(self.variance_threshold)
        self.variance_threshold_slider.valueChanged.connect(self.update_variance_threshold)  # type: ignore

        # 宏观波动阈值标签
        self.deviation_threshold_label = QLabel(f"宏观阈值: {self.deviation_threshold:.4f}")
        self.deviation_threshold_label.setAlignment(QtCore.Qt.AlignCenter)  # type: ignore
        # 宏观波动阈值滑块
        self.deviation_threshold_slider = QSlider(Qt.Horizontal)
        self.deviation_threshold_slider.setMinimum(1)  # 0.01
        self.deviation_threshold_slider.setMaximum(100000)  # 1000
        self.deviation_threshold_slider.setValue(int(self.deviation_threshold * 100))
        self.deviation_threshold_slider.valueChanged.connect(self.update_deviation_threshold)  # type: ignore

        # 检测模式切换按钮（宏观/微观）
        self.detection_mode_btn = QPushButton()
        self.update_detection_mode_button_text()
        self.detection_mode_btn.clicked.connect(self.toggle_detection_mode)  # type: ignore
        self.detection_mode_btn.setStyleSheet("""
            QPushButton {
                background-color: #4A90E2;
                color: black;
                border: none;
                padding: 8px 16px;
                border-radius: 6px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #357ABD;
            }
            QPushButton:pressed {
                background-color: #2E6DA4;
            }
        """)

        # 将组件添加到左侧布局中
        # self.left_layout.addWidget(self.variance_threshold_label)
        # self.left_layout.addWidget(self.variance_threshold_slider)
        # self.left_layout.addWidget(self.deviation_threshold_label)
        # self.left_layout.addWidget(self.deviation_threshold_slider)
        # self.left_layout.addWidget(self.detection_mode_btn)

        # 组件添加到右侧布局
        threshold_layout.addWidget(self.variance_threshold_label)
        threshold_layout.addWidget(self.variance_threshold_slider)
        threshold_layout.addWidget(self.deviation_threshold_label)
        threshold_layout.addWidget(self.deviation_threshold_slider)
        threshold_layout.addWidget(self.detection_mode_btn)
        right_slider_layout.insertLayout(-1, threshold_layout)  # 插入到状态面板前
        self.variance_threshold_slider.setEnabled(False)  # 禁用滑块
        self.deviation_threshold_slider.setEnabled(False)  # 禁用滑块


        # 初始化时更新UI显示
        self.update_threshold_labels_display()

        # 截图计数器（添加到状态面板下方）
        self.counter_layout = QVBoxLayout()

        # 计数器显示
        self.screenshot_counter = QLabel("0")  # type: ignore
        self.screenshot_counter.setAlignment(QtCore.Qt.AlignCenter)  # type: ignore
        self.screenshot_counter.setStyleSheet("""
            QLabel {
                font-size: 36px;
                font-weight: bold;
                color: #FF0000;
                margin: 10px;
            }
        """)

        # 清零按钮
        self.reset_counter_btn = QPushButton("清零计数器")
        self.reset_counter_btn.clicked.connect(self.reset_counter)  # type: ignore
        self.reset_counter_btn.setStyleSheet("""
            QPushButton {
                background-color: #F0F0F0;
                border: 1px solid #AAAAAA;
                padding: 5px;
            }
            QPushButton:hover {
                background-color: #E0E0E0;
            }
        """)

        self.counter_layout.addWidget(QLabel("截图计数"))
        self.counter_layout.addWidget(self.screenshot_counter)
        self.counter_layout.addWidget(self.reset_counter_btn)


        # 组装右侧布局
        right_slider_layout.addWidget(self.status_panel)
        right_slider_layout.addWidget(self.max_slider)
        right_slider_layout.addWidget(QLabel("Y轴"))
        right_slider_layout.addWidget(self.min_slider)
        right_slider_layout.addLayout(label_layout)
        right_slider_layout.addLayout(self.counter_layout)

        # 将左右布局加入主容器
        self.main_layout.addLayout(self.left_layout, 85)  # 左侧占85%宽度
        self.main_layout.addLayout(right_slider_layout, 15)  # 右侧占15%宽度

        # 创建三滑块的水平布局
        margin_sliders_layout = QHBoxLayout()

        # 左边距滑块组
        left_margin_group = QVBoxLayout()
        self.left_margin_label = QLabel(f"左边距: {self.capture_left_margin:.1f}s")
        self.left_margin_label.setAlignment(Qt.AlignCenter)
        self.left_margin_slider = QSlider(Qt.Horizontal)
        self.left_margin_slider.setMinimum(0)  # 0秒
        self.left_margin_slider.setMaximum(int((self.capture_duration * 10) / 2))
        self.left_margin_slider.setValue(int(self.capture_left_margin * 10))
        self.left_margin_slider.valueChanged.connect(self.update_left_margin)  # type: ignore
        left_margin_group.addWidget(self.left_margin_label)
        left_margin_group.addWidget(self.left_margin_slider)

        # 最小波动时长滑块组
        min_volatile_group = QVBoxLayout()
        self.min_volatile_label = QLabel(f"最小波动: {self.min_volatile_duration:.1f}s")
        self.min_volatile_label.setAlignment(Qt.AlignCenter)
        self.min_volatile_slider = QSlider(Qt.Horizontal)
        self.min_volatile_slider.setMinimum(1)  # 0.1秒
        self.min_volatile_slider.setMaximum(int(self.capture_duration) * 10)  # 3.0秒
        self.min_volatile_slider.setValue(int(self.min_volatile_duration * 10))
        self.min_volatile_slider.valueChanged.connect(self.update_min_volatile_duration)  # type: ignore
        min_volatile_group.addWidget(self.min_volatile_label)
        min_volatile_group.addWidget(self.min_volatile_slider)

        # 右边距滑块组
        right_margin_group = QVBoxLayout()
        self.right_margin_label = QLabel(f"右边距: {self.capture_right_margin:.1f}s")
        self.right_margin_label.setAlignment(Qt.AlignCenter)
        self.right_margin_slider = QSlider(Qt.Horizontal)
        self.right_margin_slider.setMinimum(0)  # 0秒
        self.right_margin_slider.setMaximum(int((self.capture_duration * 10) / 2))
        self.right_margin_slider.setValue(int(self.capture_right_margin * 10))
        self.right_margin_slider.valueChanged.connect(self.update_right_margin)  # type: ignore
        right_margin_group.addWidget(self.right_margin_label)
        right_margin_group.addWidget(self.right_margin_slider)

        # 将三个滑块组按顺序添加到水平布局
        margin_sliders_layout.addLayout(left_margin_group)
        margin_sliders_layout.addLayout(min_volatile_group)
        margin_sliders_layout.addLayout(right_margin_group)

        # 设置等宽分布
        margin_sliders_layout.setStretchFactor(left_margin_group, 1)
        margin_sliders_layout.setStretchFactor(min_volatile_group, 1)
        margin_sliders_layout.setStretchFactor(right_margin_group, 1)

        # 添加到左侧布局中
        self.left_layout.addLayout(margin_sliders_layout)

        self.update_margin_slider_ranges()  # 确保滑块范围正确

        self.setCentralWidget(main_container)

    # 创建底部的按钮们
    def create_buttons(self):
        # 按钮布局（保存为实例变量以便后续动态添加）
        self.button_layout = QHBoxLayout()

        # 新增初始化按钮
        self.init_button = QPushButton("清屏")
        self.init_button.clicked.connect(self.reset_system)  # type: ignore
        self.init_button.setStyleSheet("background-color: #FFA500; color: black;")
        self.button_layout.addWidget(self.init_button)

        # 暂停/继续按钮
        self.pause_button = QPushButton("暂停 ||")
        self.pause_button.clicked.connect(self.toggle_pause)  # type: ignore
        self.button_layout.addWidget(self.pause_button)

        # 截图按钮
        self.screenshot_button = QPushButton("截图")
        self.screenshot_button.clicked.connect(self.take_screenshot)  # type: ignore
        self.button_layout.addWidget(self.screenshot_button)

        # 设置按钮
        self.settings_button = QPushButton("设置 (⚙)")
        self.settings_button.clicked.connect(self.show_settings)  # type: ignore
        self.settings_button.setEnabled(False)
        self.button_layout.addWidget(self.settings_button)

        # 新增录制按钮
        self.record_button = QPushButton("开始录制 ●")
        self.record_button.clicked.connect(self.toggle_recording)  # type: ignore
        self.record_button.setStyleSheet("background-color: #ff0000; color: white;")
        self.button_layout.addWidget(self.record_button)

        # 新增：动态Y轴按钮
        self.dynamic_y_button = QPushButton()
        if self.dynamic_y_enabled:
            self.dynamic_y_button.setText("动态Y轴：开")
            self.dynamic_y_button.setStyleSheet("background-color: #90EE90;")
        else:
            self.dynamic_y_button.setText("动态Y轴：关")
            self.dynamic_y_button.setStyleSheet("")
        self.dynamic_y_button.clicked.connect(self.toggle_dynamic_y)  # type: ignore
        self.button_layout.addWidget(self.dynamic_y_button)

        # 新增：统计线按钮
        self.stats_button = QPushButton("统计线：关")
        self.stats_button.clicked.connect(self.toggle_stats_visibility)  # type: ignore
        self.button_layout.addWidget(self.stats_button)

        # 添加按钮布局到主布局
        self.left_layout.addLayout(self.button_layout)

        # 新增自动截取按钮
        self.auto_capture_btn = QPushButton("启动自动截取")
        self.auto_capture_btn.clicked.connect(self.toggle_auto_capture)  # type: ignore
        self.auto_capture_btn.setStyleSheet("background-color: #4CAF50; color: white;")
        self.button_layout.addWidget(self.auto_capture_btn)

        # 新增截取时间滑块
        self.capture_slider = QSlider(QtCore.Qt.Horizontal)  # type: ignore
        self.capture_slider.setMinimum(1)
        self.capture_slider.setMaximum(self.max_window_time // 2)
        self.capture_slider.setValue(self.capture_duration)
        self.capture_slider_label = QLabel(f"截取时间: {self.capture_duration}秒 (最大{self.max_window_time // 2}秒)")
        self.button_layout.addWidget(self.capture_slider_label)
        self.button_layout.addWidget(self.capture_slider)
        self.capture_slider.valueChanged.connect(self.update_capture_duration)  # type: ignore

        # 新增模拟数据模式切换按钮（仅在模拟数据模式下显示）
        self.sim_mode_btn = QPushButton("切换为稳定模式")
        self.sim_mode_btn.clicked.connect(self.toggle_sim_mode)  # type: ignore
        self.sim_mode_btn.setStyleSheet("background-color: #FFD700; color: black;")
        self.sim_mode_btn.setVisible(self.settings['use_simulated_data'])  # 初始可见性
        self.button_layout.addWidget(self.sim_mode_btn)

        # 校验功能按钮组（将在需要时动态创建）
        self.save_baseline_btn = None
        self.calibration_btn = None
        self.apply_calibration_btn = None
        self.calibration_status_label = None

    # 切换模拟数据模式（稳定/波动）
    def toggle_sim_mode(self):
        """切换模拟数据模式（稳定/波动/输入）"""
        # 循环切换三种模式
        self.current_sim_mode_index = (self.current_sim_mode_index + 1) % len(self.simulation_modes)
        new_mode = self.simulation_modes[self.current_sim_mode_index]

        # 更新按钮显示
        self.update_sim_mode_button(new_mode)

        # 如果使用模拟数据且进程正在运行，发送模式切换命令
        if self.settings['use_simulated_data'] and self.data_generator_process is not None:
            self.send_control_command('mode_change', {'mode': new_mode})

    def update_sim_mode_button(self, current_mode):
        """更新模拟模式按钮显示"""
        if current_mode == "stable":
            self.sim_mode_btn.setText("稳定模式 (点击→波动)")
            self.sim_mode_btn.setStyleSheet("background-color: #32CD32; color: black;")
        elif current_mode == "volatile":
            self.sim_mode_btn.setText("波动模式 (点击→输入)")
            self.sim_mode_btn.setStyleSheet("background-color: #FFD700; color: black;")
        elif current_mode == "input":
            self.sim_mode_btn.setText("输入模式 (点击→稳定)")
            self.sim_mode_btn.setStyleSheet("background-color: #87CEEB; color: black;")

    def start_data_generator_process(self):
        """启动数据生成进程"""
        try:
            # 创建进程间通信队列
            self.data_queue = multiprocessing.Queue(maxsize=200)
            self.control_queue = multiprocessing.Queue(maxsize=50)

            # 启动数据生成进程
            self.data_generator_process = multiprocessing.Process(
                target=run_data_generator,
                args=(self.data_queue, self.control_queue, self.settings['num_curve_groups'])
            )
            self.data_generator_process.start()

            # 发送初始模式
            initial_mode = self.simulation_modes[self.current_sim_mode_index]
            self.send_control_command('mode_change', {'mode': initial_mode})
            self.update_sim_mode_button(initial_mode)

            print(f"数据生成进程已启动，PID: {self.data_generator_process.pid}")

        except Exception as e:
            print(f"启动数据生成进程失败: {e}")
            QMessageBox.warning(self, "警告", f"启动数据生成进程失败: {e}")

    def stop_data_generator_process(self):
        """停止数据生成进程"""
        if self.data_generator_process is not None:
            try:
                print("正在停止数据生成进程...")

                # 发送关闭命令
                self.send_control_command('shutdown', {})

                # 等待进程结束（缩短等待时间）
                self.data_generator_process.join(timeout=1)

                # 如果进程还没结束，强制终止
                if self.data_generator_process.is_alive():
                    print("强制终止数据生成进程...")
                    self.data_generator_process.terminate()
                    self.data_generator_process.join(timeout=0.5)

                # 如果还是没停止，使用kill（仅限Windows）
                if self.data_generator_process.is_alive():
                    print("使用kill强制停止进程...")
                    import os
                    import signal
                    try:
                        if hasattr(signal, 'SIGTERM') and self.data_generator_process.pid:
                            os.kill(self.data_generator_process.pid, signal.SIGTERM)
                            time.sleep(0.1)
                        if self.data_generator_process.is_alive():
                            # Windows下直接使用terminate
                            self.data_generator_process.terminate()
                            time.sleep(0.1)
                    except:
                        pass

                print("数据生成进程已停止")

            except Exception as e:
                print(f"停止数据生成进程时出错: {e}")

            finally:
                self.data_generator_process = None
                # 清空队列
                if self.data_queue is not None:
                    try:
                        while not self.data_queue.empty():
                            self.data_queue.get_nowait()
                    except:
                        pass
                if self.control_queue is not None:
                    try:
                        while not self.control_queue.empty():
                            self.control_queue.get_nowait()
                    except:
                        pass
                self.data_queue = None
                self.control_queue = None

    def send_control_command(self, command_type, data):
        """向数据生成进程发送控制命令"""
        if self.control_queue is not None:
            try:
                command = {'type': command_type}
                command.update(data)
                self.control_queue.put_nowait(command)
            except Exception as e:
                print(f"发送控制命令失败: {e}")

    def receive_simulated_data(self):
        """从数据生成进程接收模拟数据"""
        if self.data_queue is None:
            return None

        try:
            # 非阻塞获取数据
            packet = self.data_queue.get_nowait()
            return packet['values']
        except queue.Empty:
            return None
        except Exception as e:
            print(f"接收模拟数据时出错: {e}")
            return None

    def add_calibration_buttons(self):
        """动态添加校验功能按钮"""
        if self.save_baseline_btn is not None:
            return  # 按钮已存在，避免重复创建

        # 创建校验功能按钮
        self.save_baseline_btn = QPushButton("保存基准值")
        self.save_baseline_btn.clicked.connect(self.save_baseline)  # type: ignore
        self.save_baseline_btn.setStyleSheet("background-color: #2196F3; color: white;")
        self.button_layout.addWidget(self.save_baseline_btn)

        self.calibration_btn = QPushButton("开始标定")
        self.calibration_btn.clicked.connect(self.start_calibration)  # type: ignore
        self.calibration_btn.setStyleSheet("background-color: #FF9800; color: white;")
        self.button_layout.addWidget(self.calibration_btn)

        self.apply_calibration_btn = QPushButton("应用校验")
        self.apply_calibration_btn.clicked.connect(self.toggle_calibration_application)  # type: ignore
        self.apply_calibration_btn.setStyleSheet("background-color: #4CAF50; color: white;")
        self.button_layout.addWidget(self.apply_calibration_btn)

        # 添加校验状态显示
        self.calibration_status_label = QLabel("校验状态：未启用")
        self.calibration_status_label.setStyleSheet("color: #666666; font-size: 12px;")
        self.button_layout.addWidget(self.calibration_status_label)

        # 状态栏提示
        self.statusBar().showMessage("校验功能按钮已添加", 2000)

    def remove_calibration_buttons(self):
        """移除校验功能按钮"""
        buttons = [self.save_baseline_btn, self.calibration_btn, self.apply_calibration_btn, self.calibration_status_label]
        for button in buttons:
            if button is not None:
                self.button_layout.removeWidget(button)
                button.deleteLater()

        self.save_baseline_btn = None
        self.calibration_btn = None
        self.apply_calibration_btn = None
        self.calibration_status_label = None

    # === 校验功能相关方法 ===
    def save_baseline(self):
        """保存当前无压力状态的基准值"""
        if not self.curve_groups or len(self.curve_groups[0]['source_data']) == 0:
            QMessageBox.warning(self, "警告", "当前没有数据可用！请确保传感器正在工作。")
            return

        self.baseline_values = []
        for i in range(self.settings['num_curve_groups']):
            # 取最近10个数据点的平均值作为基准，提高稳定性
            recent_data = list(self.curve_groups[i]['source_data'])[-10:]
            if len(recent_data) > 0:
                baseline = np.mean(recent_data)
                self.baseline_values.append(baseline)
            else:
                QMessageBox.warning(self, "警告", f"曲线{i+1}没有足够的数据！")
                return

        self.calibration_data['baseline'] = self.baseline_values.copy()
        self.statusBar().showMessage(f"基准值已保存：{[f'{v:.1f}' for v in self.baseline_values]}", 3000)

        # 保存到配置文件
        self.save_calibration_data()

    def start_calibration(self):
        """开始标定过程"""
        if not self.baseline_values:
            QMessageBox.warning(self, "警告", "请先保存基准值！")
            return

        if self.is_calibrating:
            self.stop_calibration()
            return

        self.is_calibrating = True
        self.calibration_data['mapping'] = {}
        # 重置标定相关计数器
        self.last_calibration_ref = None
        self.calibration_sample_counter = 0

        if self.calibration_btn is not None:
            self.calibration_btn.setText("停止标定")
            self.calibration_btn.setStyleSheet("background-color: #F44336; color: white;")

        self.statusBar().showMessage("标定中...请在平面上缓慢施加不同力度的压力", 0)

        # 禁用其他按钮防止误操作
        if self.save_baseline_btn is not None:
            self.save_baseline_btn.setEnabled(False)
        if self.apply_calibration_btn is not None:
            self.apply_calibration_btn.setEnabled(False)

    def stop_calibration(self):
        """停止标定过程"""
        self.is_calibrating = False

        if self.calibration_btn is not None:
            self.calibration_btn.setText("开始标定")
            self.calibration_btn.setStyleSheet("background-color: #FF9800; color: white;")

        # 重新启用按钮
        if self.save_baseline_btn is not None:
            self.save_baseline_btn.setEnabled(True)
        if self.apply_calibration_btn is not None:
            self.apply_calibration_btn.setEnabled(True)

        # 显示标定结果
        mapping_count = len(self.calibration_data['mapping'])
        self.statusBar().showMessage(f"标定完成！共收集{mapping_count}个标定点", 3000)

        # 保存标定数据
        self.save_calibration_data()

    def collect_calibration_data(self):
        """在update_plot中调用，收集标定数据 - 改进版：更精细的映射收集"""
        if not self.is_calibrating or len(self.curve_groups[0]['source_data']) < 5:
            return

        # 增加采样计数器，控制采样频率
        self.calibration_sample_counter += 1
        if self.calibration_sample_counter < self.calibration_sample_interval:
            return
        self.calibration_sample_counter = 0

        # 获取基准曲线当前值
        ref_idx = self.reference_curve_index
        if ref_idx >= len(self.curve_groups):
            return

        # 使用最近几个数据点的平均值，提高稳定性
        recent_ref_data = list(self.curve_groups[ref_idx]['source_data'])[-3:]
        ref_value = int(np.mean(recent_ref_data)) if len(recent_ref_data) > 0 else 0

        # 获取其他曲线当前值（同样使用平均值）
        # 重要：保存时需要记录每条曲线对应的索引关系
        other_values = []
        other_indices = []  # 记录非基准曲线的原始索引
        for i in range(self.settings['num_curve_groups']):
            if i != ref_idx:
                recent_data = list(self.curve_groups[i]['source_data'])[-3:]
                avg_value = int(np.mean(recent_data)) if len(recent_data) > 0 else 0
                other_values.append(avg_value)
                other_indices.append(i)  # 记录原始曲线索引

        # 动态容差策略：基于基准值变化率调整容差
        existing_refs = [float(k) for k in self.calibration_data['mapping'].keys()]

        # 如果映射点过多，增加容差
        if len(existing_refs) > self.max_mapping_points * 0.8:
            current_tolerance = self.calibration_tolerance * 2
        else:
            current_tolerance = self.calibration_tolerance

        # 智能重复检测：检查是否已有相近的基准值
        is_duplicate = False
        closest_existing = None

        if existing_refs:
            closest_existing = min(existing_refs, key=lambda x: abs(x - ref_value))
            is_duplicate = abs(closest_existing - ref_value) < current_tolerance

        # 高精度映射收集策略
        should_record = False

        if not existing_refs:
            # 第一个数据点，必须记录
            should_record = True
            record_reason = "首个数据点"
        elif not is_duplicate:
            # 基准值足够不同，记录
            should_record = True
            record_reason = f"新基准值(容差:{current_tolerance})"
        elif self.last_calibration_ref is not None:
            # 即使相近，但如果基准值变化趋势明显，也记录
            trend_change = abs(ref_value - self.last_calibration_ref)
            if trend_change >= current_tolerance * 0.5:
                should_record = True
                record_reason = f"趋势变化({trend_change})"

        # 防止内存过载
        if len(existing_refs) >= self.max_mapping_points:
            should_record = False
            record_reason = "达到最大映射点数"

        if should_record:
            # 使用更精确的键值（保留小数精度）
            precise_ref_key = f"{ref_value:.1f}"
            # 保存映射数据，包含索引关系
            self.calibration_data['mapping'][precise_ref_key] = {
                'values': other_values.copy(),
                'indices': other_indices.copy(),  # 保存对应的原始曲线索引
                'ref_index': ref_idx  # 保存基准曲线索引
            }
            self.last_calibration_ref = ref_value

            # 实时更新状态栏显示标定进度
            mapping_count = len(self.calibration_data['mapping'])
            coverage_range = f"{min(existing_refs + [ref_value])}-{max(existing_refs + [ref_value])}" if existing_refs else str(ref_value)
            self.statusBar().showMessage(
                f"标定中...已收集{mapping_count}个标定点 | 基准值: {ref_value} | 覆盖范围: {coverage_range} | 原因: {record_reason}", 0
            )

            # 每收集50个点提示一次
            if mapping_count % 50 == 0:
                print(f"[标定进度] 已收集 {mapping_count} 个映射点，当前覆盖范围: {coverage_range}")

        # 实时显示当前基准值（即使不记录）
        if hasattr(self, 'calibration_status_label') and self.calibration_status_label is not None:
            mapping_count = len(self.calibration_data['mapping'])
            self.calibration_status_label.setText(f"标定中: {mapping_count}点 | 当前基准: {ref_value}")
            self.calibration_status_label.setStyleSheet("color: #FF9800; font-size: 12px; font-weight: bold;")

    def toggle_calibration_application(self):
        """切换校验应用状态"""
        if not self.calibration_data.get('mapping'):
            QMessageBox.warning(self, "警告", "请先完成标定！")
            return

        self.calibration_enabled = not self.calibration_enabled

        if self.apply_calibration_btn is not None:
            if self.calibration_enabled:
                self.apply_calibration_btn.setText("停止校验")
                self.apply_calibration_btn.setStyleSheet("background-color: #F44336; color: white;")
                self.statusBar().showMessage("数据校验已启用", 2000)
                if hasattr(self, 'calibration_status_label') and self.calibration_status_label is not None:
                    self.calibration_status_label.setText("校验状态：已启用")
                    self.calibration_status_label.setStyleSheet("color: #4CAF50; font-size: 12px; font-weight: bold;")
            else:
                self.apply_calibration_btn.setText("应用校验")
                self.apply_calibration_btn.setStyleSheet("background-color: #4CAF50; color: white;")
                self.statusBar().showMessage("数据校验已停用", 2000)
                if hasattr(self, 'calibration_status_label') and self.calibration_status_label is not None:
                    self.calibration_status_label.setText("校验状态：未启用")
                    self.calibration_status_label.setStyleSheet("color: #666666; font-size: 12px;")

    def apply_calibration_correction(self, raw_data):
        """对原始数据应用校验校正"""
        if not self.calibration_enabled or not self.calibration_data.get('mapping') or not self.baseline_values:
            return raw_data

        corrected_data = raw_data.copy()
        ref_idx = self.reference_curve_index

        if ref_idx >= len(raw_data):
            return raw_data

        current_ref_value = int(raw_data[ref_idx])

        # 在映射表中找到最接近的基准值
        mapping = self.calibration_data['mapping']
        available_refs = [int(float(ref)) for ref in mapping.keys()]

        if not available_refs:
            return raw_data

        closest_ref = min(available_refs, key=lambda x: abs(x - current_ref_value))

        # 如果差距太大，使用插值
        if abs(closest_ref - current_ref_value) > 30:
            expected_data = self.interpolate_expected_values(current_ref_value)
        else:
            closest_ref_key = str(float(closest_ref))
            mapping_entry = mapping.get(closest_ref_key)
            if mapping_entry is None:
                return raw_data

            # 处理新格式和旧格式的兼容性
            if isinstance(mapping_entry, dict):
                expected_data = {
                    'values': mapping_entry['values'],
                    'indices': mapping_entry['indices'],
                    'ref_index': mapping_entry.get('ref_index', ref_idx)
                }
            else:
                # 旧格式兼容性：假设按顺序排列的非基准曲线
                other_indices = [i for i in range(len(raw_data)) if i != ref_idx]
                expected_data = {
                    'values': mapping_entry,
                    'indices': other_indices,
                    'ref_index': ref_idx
                }

        if expected_data is None:
            return raw_data

        # 计算校正
        baseline = self.calibration_data['baseline']
        expected_values = expected_data['values']
        expected_indices = expected_data['indices']

        # 基准曲线保持基准值
        corrected_data[ref_idx] = baseline[ref_idx]

        # 校正其他曲线
        for i, curve_idx in enumerate(expected_indices):
            if i < len(expected_values) and curve_idx < len(corrected_data):
                # 计算突起影响 = 实际变化 - 期望变化
                actual_change = baseline[curve_idx] - raw_data[curve_idx]
                expected_change = baseline[curve_idx] - expected_values[i]
                bump_effect = actual_change - expected_change

                # 校正后的值 = 基准值 - 突起影响
                corrected_data[curve_idx] = baseline[curve_idx] - bump_effect

        return corrected_data

    def interpolate_expected_values(self, ref_value):
        """插值计算期望值"""
        mapping = self.calibration_data['mapping']
        ref_keys = sorted([float(k) for k in mapping.keys()])

        if not ref_keys:
            return None

        # 找到两个邻近的基准值
        lower_keys = [k for k in ref_keys if k <= ref_value]
        upper_keys = [k for k in ref_keys if k >= ref_value]

        lower = max(lower_keys) if lower_keys else ref_keys[0]
        upper = min(upper_keys) if upper_keys else ref_keys[-1]

        if lower == upper:
            mapping_entry = mapping[str(lower)]
            # 处理新格式和旧格式的兼容性
            if isinstance(mapping_entry, dict):
                return mapping_entry
            else:
                # 旧格式：生成兼容的结构
                ref_idx = self.reference_curve_index
                other_indices = [i for i in range(len(self.baseline_values)) if i != ref_idx]
                return {
                    'values': mapping_entry,
                    'indices': other_indices,
                    'ref_index': ref_idx
                }

        # 线性插值
        ratio = (ref_value - lower) / (upper - lower)

        lower_entry = mapping[str(lower)]
        upper_entry = mapping[str(upper)]

        # 处理新格式和旧格式的兼容性
        if isinstance(lower_entry, dict) and isinstance(upper_entry, dict):
            lower_values = np.array(lower_entry['values'])
            upper_values = np.array(upper_entry['values'])
            interpolated_values = lower_values + ratio * (upper_values - lower_values)

            return {
                'values': interpolated_values.tolist(),
                'indices': lower_entry['indices'],  # 索引应该是一样的
                'ref_index': lower_entry['ref_index']
            }
        else:
            # 旧格式处理
            lower_values = np.array(lower_entry if isinstance(lower_entry, list) else [lower_entry])
            upper_values = np.array(upper_entry if isinstance(upper_entry, list) else [upper_entry])
            interpolated_values = lower_values + ratio * (upper_values - lower_values)

            ref_idx = self.reference_curve_index
            other_indices = [i for i in range(len(self.baseline_values)) if i != ref_idx]

            return {
                'values': interpolated_values.tolist(),
                'indices': other_indices,
                'ref_index': ref_idx
            }

    def save_calibration_data(self):
        """保存标定数据到文件"""
        try:
            calibration_file = f"calibration_test_datas/calibration_{self.main_filename}.json"
            with open(calibration_file, 'w') as f:
                json.dump(self.calibration_data, f, indent=2)
        except Exception as e:
            self.statusBar().showMessage(f"保存标定数据失败: {str(e)}", 3000)

    def load_calibration_data(self):
        """从文件加载标定数据"""
        try:
            calibration_file = f"calibration_test_datas/calibration_{self.main_filename}.json"
            if os.path.exists(calibration_file):
                with open(calibration_file, 'r') as f:
                    loaded_data = json.load(f)
                    self.calibration_data = loaded_data
                    if 'baseline' in loaded_data:
                        self.baseline_values = loaded_data['baseline']
                    self.statusBar().showMessage("标定数据已加载", 2000)
                    return True
        except Exception as e:
            self.statusBar().showMessage(f"加载标定数据失败: {str(e)}", 3000)
        return False

    def update_calibration_ui_visibility(self):
        """更新校验功能UI的可见性"""
        if self.calibration_enabled:
            # 如果启用校验但按钮不存在，则创建按钮
            if self.save_baseline_btn is None:
                self.add_calibration_buttons()
        else:
            # 如果禁用校验但按钮存在，则移除按钮
            if self.save_baseline_btn is not None:
                self.remove_calibration_buttons()

    # 暂停按钮切换
    def toggle_pause(self):
        self.is_paused = not self.is_paused
        if self.is_paused:
            self.pause_button.setText("继续 ▶")
            self.settings_button.setEnabled(True)
        else:
            self.pause_button.setText("暂停 ||")
            self.settings_button.setEnabled(False)
        if self.is_paused and self.is_recording:
            self.recording_frames.clear()
            self.recording_data.clear()

    # 截图函数
    def take_screenshot(self, time_range=None):
        # 修改截图文件名生成逻辑
        current_time = datetime.now().strftime('%Y%m%d_%H%M%S')
        # TODO 当截图太快的时候这里会出现截图覆盖的问题，但我懒得改
        # 保存指定时间范围内的数据
        highlight_region = None
        os.makedirs(f"screenshots/{self.main_filename}", exist_ok=True)
        if time_range:
            indices = [i for i, t in enumerate(self.x_data) if time_range[0] <= t <= time_range[1]]
            screenshot_filename = f"screenshots/{self.main_filename}/{self.main_filename}_auto_screenshot_{current_time}.png"
            csv_filename = f"screenshots/{self.main_filename}/{self.main_filename}_auto_screenshot_{current_time}_data.csv"
            # 创建半透明绿色区域
            highlight_region = pg.LinearRegionItem(
                values=[time_range[0], time_range[1]],
                brush=(0, 255, 0, 30),  # RGBA：绿色，30%透明度
                pen=pg.mkPen(color=(0, 200, 0),  # 边框颜色
                             movable=False  # 禁止用户拖动
                             ))
            self.plot_widget.addItem(highlight_region)
            QtCore.QCoreApplication.processEvents()  # 强制立即渲染
        else:
            indices = range(len(self.x_data))
            screenshot_filename = f"screenshots/{self.main_filename}/{self.main_filename}_manual_screenshot_{current_time}.png"
            csv_filename = f"screenshots/{self.main_filename}/{self.main_filename}_manual_screenshot_{current_time}_data.csv"

        if not indices:
            QMessageBox.warning(self, "警告", "未找到符合条件的数据")
            return

        # 保存截图
        self.plot_widget.grab().save(screenshot_filename, "PNG")
        # 移除高亮区域
        if highlight_region is not None:
            self.plot_widget.removeItem(highlight_region)

        # 保存当前显示的所有点的横纵坐标为CSV文件
        with open(csv_filename, 'w') as csv_file:
            # 写入表头
            header = "Time (s)"
            for i in range(self.settings['num_curve_groups']):
                header += f",Curve {i+1} (Original)"
                for filter_name in self.settings['selected_filters']:
                    if filter_name != '原数据':
                        header += f",Curve {i+1} ({filter_name})"
            csv_file.write(header + "\n")

            # 写入数据
            for i in indices:
                time_str = str(self.x_data[i])
                row = time_str
                for curve_group in self.curve_groups:
                    row += f",{curve_group['source_data'][i]}"
                    for filter_name in self.settings['selected_filters']:
                        if filter_name != '原数据':
                            row += f",{curve_group['filtered_data'][filter_name][i]}"
                csv_file.write(row + "\n")

        # 视觉反馈，按钮变绿
        self.screenshot_button.setStyleSheet("background-color: #00FF00;")
        #　TODO 截图数量指示
        QtCore.QTimer.singleShot(500, lambda: self.screenshot_button.setStyleSheet(""))
        # 成功保存后增加计数
        self.screenshot_count += 1
        self.update_counter_display()
        # 发送CSV路径
        if self.settings['neural_net_enabled']:
            try:
                with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                    s.connect(("localhost", 65432))
                    if self.use_fake_csvs:  # todo 如果是模拟数据，使用预设的CSV路径
                        for fake_csv in self.fake_csvs:
                            if os.path.exists(fake_csv["path"]):
                                if not fake_csv["is_used"]:
                                    csv_filename = fake_csv["path"]
                                    fake_csv["is_used"] = True
                                    print(f"使用模拟数据CSV: {csv_filename}")
                                    break
                    s.sendall(csv_filename.encode())
                    self.statusBar().showMessage(f"数据已成功发送到端口：65432。请前往对应程序查看结果", 2000)
            except Exception as e:
                self.statusBar().showMessage(f"数据发送失败: {str(e)}", 2000)

    # 清零截图计数器
    def reset_counter(self):
        """清零计数器"""
        self.screenshot_count = 0
        self.update_counter_display()
        self.statusBar().showMessage("截图计数器已清零", 2000)

    # 更新截图计数器显示
    def update_counter_display(self):
        """更新计数器显示"""
        self.screenshot_counter.setText(str(self.screenshot_count))
        # 数字跳动动画效果（可选）
        self.screenshot_counter.setStyleSheet("""
            QLabel {
                font-size: 38px;
                font-weight: bold;
                color: #FF0000;
                margin: 10px;
            }
        """)
        QtCore.QTimer.singleShot(100, lambda:
        self.screenshot_counter.setStyleSheet("""
                QLabel {
                    font-size: 36px;
                    font-weight: bold;
                    color: #FF0000;
                    margin: 10px;
                }
            """)
                                 )

    # 视频录制函数
    def toggle_recording(self):
        if not self.is_recording:
            # 开始录制
            self.start_recording()
        else:
            # 停止录制
            self.stop_recording()

    # 视频录制函数-开始
    def start_recording(self):
        # 生成文件名
        current_time = datetime.now().strftime("%Y%m%d_%H%M%S")
        self.video_filename = f"recordings/{self.main_filename}_recording_{current_time}.avi"
        self.recording_data_filename = f"recordings/{self.main_filename}_recording_{current_time}_data.csv"

        # 创建目录
        os.makedirs("recordings", exist_ok=True)

        # 初始化视频写入器
        fps = 30
        frame_size = (self.plot_widget.width(), self.plot_widget.height())
        fourcc = cv2.VideoWriter_fourcc(*'XVID')  # type: ignore
        self.video_writer = cv2.VideoWriter(self.video_filename, fourcc, fps, frame_size)

        # 初始化记录数据
        self.recording_start_time = time.time()
        self.recording_data = []

        # 更新按钮状态
        self.is_recording = True
        self.record_button.setText("停止录制 ■")
        self.record_button.setStyleSheet("background-color: #00ff00; color: black;")
        QMessageBox.information(self, "录制开始", "视频录制已开始！")

    # 视频录制函数-结束
    def stop_recording(self):
        if self.video_writer is not None:

            # 关闭视频写入器
            self.video_writer.release()
            self.video_writer = None

            # 保存数据文件
            with open(self.recording_data_filename, 'w') as f:
                f.write("FrameTime,Data\n")
                for t, data in zip(np.linspace(0, time.time() - self.recording_start_time, len(self.recording_data)),
                                   self.recording_data):
                    f.write(f"{t:.3f},{','.join(map(str, data))}\n")

            # 重置状态
            self.is_recording = False
            self.record_button.setText("开始录制 ●")
            self.record_button.setStyleSheet("background-color: #ff0000; color: white;")
            QMessageBox.information(self, "录制完成",
                                    f"视频已保存为：{self.video_filename}\n"
                                    f"同步数据已保存为：{self.recording_data_filename}")

    # 自动截图函数
    # 自动截图-按钮和控件状态切换
    def toggle_auto_capture(self):
        self.auto_capture_enabled = not self.auto_capture_enabled
        self.last_clean_time = time.time()
        if self.auto_capture_enabled:
            # 检查截取时间是否合法
            max_capture = self.max_window_time * 0.5
            if self.capture_duration > max_capture:
                QMessageBox.warning(self, "错误", f"截取时间不能超过窗口的50%（当前最大{max_capture}秒）")
                self.auto_capture_enabled = False
                return
            # # 新增：检查是否有足够历史数据
            # if len(self.time_blocks) < 10:  # 至少1秒数据（0.1*10）
            #     QMessageBox.warning(self, "提示", "初始化成功！请再次点击开始自动截取")
            #     self.auto_capture_enabled = False
            #     return
            # 禁用相关控件
            self.time_slider.setEnabled(False)
            self.capture_slider.setEnabled(False)
            self.auto_capture_btn.setText("停止自动截取")
            self.auto_capture_btn.setStyleSheet("background-color: #F44336; color: white;")
            # 初始状态显示
            self.status_panel.setStyleSheet("border-color: #FFA500;")  # 橙色边框
            self.update_status_display("stable", 0)  # 默认显示稳定
            self.variance_threshold_slider.setEnabled(True)  # 启用微观阈值滑块
            self.deviation_threshold_slider.setEnabled(True)  # 启用宏观阈值滑块
        else:
            # 启用相关控件
            self.time_slider.setEnabled(True)
            self.capture_slider.setEnabled(True)
            self.auto_capture_btn.setText("启动自动截取")
            self.auto_capture_btn.setStyleSheet("background-color: #4CAF50; color: white;")
            # 重置状态显示
            self.status_panel.setText("状态：未监测")
            self.status_panel.setStyleSheet("color: #666666; border-color: #AAAAAA;")
            self.variance_threshold_slider.setEnabled(False)  # 禁用微观阈值滑块
            self.deviation_threshold_slider.setEnabled(False)  # 禁用宏观阈值滑块

    # 自动截图控件 - 更新宏观波动阈值
    def update_deviation_threshold(self):
        """更新宏观波动阈值"""
        self.deviation_threshold = self.deviation_threshold_slider.value() / 100.0
        # 固定格式显示，防止数字跳动
        threshold_text = f"宏观阈值: {self.deviation_threshold:6.2f}"
        self.deviation_threshold_label.setText(threshold_text)

    # 自动截图控件 - 更新方差阈值并刷新界面
    def update_variance_threshold(self, value):
        """更新方差阈值并刷新界面"""
        self.variance_threshold = value
        self.variance_threshold_label.setText(f"微观阈值: {value}")

        self.detect_volatility()
        # 立即更新状态面板显示
        current_state = "volatile" if (self.time_blocks[-1]["state"] == "volatile") else "stable"
        self.update_status_display(current_state, 0)  # 重绘时显示新阈值

    # 自动截图控件 - 根据最大窗口时间更新截取时间设定值
    def update_capture_duration(self, value):
        """更新截取时间设定值"""
        self.capture_duration = value
        # 动态更新标签显示
        max_capture = int(self.max_window_time * 0.5)
        self.capture_slider_label.setText(f"截取时间: {value}秒 (最大{max_capture}秒)")
        # 动态更新边界滑块的最大值
        self.update_margin_slider_ranges()

    # 自动截图控件 - 根据截取时间设定值动态更新左右边界和最小波动时长滑块的范围
    def update_margin_slider_ranges(self):
        """动态更新左右边界和最小波动时长滑块的范围"""
        # 计算新的最大值（截图时长的一半）
        max_margin = self.capture_duration / 2.0
        max_margin_slider_value = int(max_margin * 10)

        # 计算最小波动时长的最大值（等于截图时长）
        max_volatile_slider_value = int(self.capture_duration * 10)

        # 更新左边界滑块范围
        current_left_value = self.left_margin_slider.value()
        self.left_margin_slider.setMaximum(max_margin_slider_value)
        # 如果当前值超过新的最大值，调整到最大值
        if current_left_value > max_margin_slider_value:
            self.left_margin_slider.setValue(max_margin_slider_value)
            self.capture_left_margin = max_margin
            self.left_margin_label.setText(f"左边距: {self.capture_left_margin:.1f}s")

        # 更新右边界滑块范围
        current_right_value = self.right_margin_slider.value()
        self.right_margin_slider.setMaximum(max_margin_slider_value)
        # 如果当前值超过新的最大值，调整到最大值
        if current_right_value > max_margin_slider_value:
            self.right_margin_slider.setValue(max_margin_slider_value)
            self.capture_right_margin = max_margin
            self.right_margin_label.setText(f"右边距: {self.capture_right_margin:.1f}s")

        # 更新最小波动时长滑块范围
        current_volatile_value = self.min_volatile_slider.value()
        self.min_volatile_slider.setMaximum(max_volatile_slider_value)
        # 如果当前值超过新的最大值，调整到最大值
        if current_volatile_value > max_volatile_slider_value:
            self.min_volatile_slider.setValue(max_volatile_slider_value)
            self.min_volatile_duration = self.capture_duration
            self.min_volatile_label.setText(f"最小波动: {self.min_volatile_duration:.1f}s")

    # 自动截图 - 切换检测模式
    def toggle_detection_mode(self):
        """切换检测模式：微观(方差) ↔ 宏观(偏差)"""
        if self.detection_mode == "variance":
            self.detection_mode = "deviation"
        else:
            self.detection_mode = "variance"

        # 更新按钮文本和样式
        self.update_detection_mode_button_text()

        # 更新阈值标签显示
        self.update_threshold_labels_display()

        # print(f"检测模式切换为: {self.detection_mode}")

    # 自动截图 - 更新检测模式按钮的文本和样式
    def update_detection_mode_button_text(self):
        """更新检测模式按钮的文本和样式"""
        if self.detection_mode == "variance":
            self.detection_mode_btn.setText(" 微观模式")
            self.detection_mode_btn.setToolTip("当前：微观波动检测（方差）\n点击切换到宏观模式")
            button_color = "#E74C3C"  # 红色
        else:
            self.detection_mode_btn.setText(" 宏观模式")
            self.detection_mode_btn.setToolTip("当前：宏观波动检测（偏差）\n点击切换到微观模式")
            button_color = "#27AE60"  # 绿色

        # 更新按钮样式
        self.detection_mode_btn.setStyleSheet(f"""
            QPushButton {{
                background-color: {button_color};
                color: white;
                border: none;
                padding: 8px 16px;
                border-radius: 6px;
                font-weight: bold;
                font-size: 14px;
            }}
            QPushButton:hover {{
                background-color: {button_color}CC;
            }}
            QPushButton:pressed {{
                background-color: {button_color}AA;
            }}
        """)

    # 自动截图 - 根据当前模式更新阈值标签显示
    def update_threshold_labels_display(self):
        """根据当前模式更新阈值标签显示"""
        if self.detection_mode == "variance":
            # 微观模式：突出显示微观阈值，淡化宏观阈值
            self.variance_threshold_label.setText(f"微观阈值: {self.variance_threshold:6.4f} [当前]")
            self.variance_threshold_label.setStyleSheet("color: #FF0000; font-weight: bold;")

            self.deviation_threshold_label.setText(f"宏观阈值: {self.deviation_threshold:6.2f}")
            self.deviation_threshold_label.setStyleSheet("color: #888888;")

        else:
            # 宏观模式：突出显示宏观阈值，淡化微观阈值
            self.variance_threshold_label.setText(f"微观阈值: {self.variance_threshold:6.4f}")
            self.variance_threshold_label.setStyleSheet("color: #888888;")

            self.deviation_threshold_label.setText(f"宏观阈值: {self.deviation_threshold:6.2f} [当前]")
            self.deviation_threshold_label.setStyleSheet("color: #FF0000; font-weight: bold;")

    # 自动截图控件 - 更新右侧状态面板显示
    def update_status_display(self, state, detection_value=None):
        """更新右侧状态面板显示"""

        # 确定状态图标和颜色
        if state == "volatile":
            status_icon = "🔴"
            status_color = "#FF4444"
            status_text = "波动"
        else:
            status_icon = "🟢"
            status_color = "#44FF44"
            status_text = "稳定"

        # 格式化检测模式信息（固定宽度）
        if self.detection_mode == "variance":
            detection_val_str = f"{detection_value:8.4f}" if detection_value is not None else "    N/A "
            threshold_str = f"{self.variance_threshold:8.4f}"
            mode_detail = f"微观(方差): {detection_val_str}"
            threshold_detail = f"阈值: {threshold_str}"

        elif self.detection_mode == "deviation":
            # 显示宏观检测的详细信息
            if isinstance(detection_value, dict):
                volatile_curves = [idx for idx, result in detection_value.items()
                                   if result['state'] == 'volatile']
                if volatile_curves:
                    max_deviation = max(result['deviation'] for result in detection_value.values())
                    # 格式化曲线列表，最多显示前3个
                    if len(volatile_curves) <= 3:
                        curves_str = str(volatile_curves).replace(' ', '')
                    else:
                        curves_str = f"[{','.join(map(str, volatile_curves[:3]))}...]"
                    mode_detail = f"宏观(偏差): {curves_str:<12} 最大: {max_deviation:6.3f}"
                else:
                    mode_detail = f"宏观(偏差): 全部稳定              "
            else:
                detection_val_str = f"{detection_value:8.4f}" if detection_value is not None else "    N/A "
                mode_detail = f"宏观(偏差): {detection_val_str}"

            threshold_str = f"{self.deviation_threshold:8.4f}"
            threshold_detail = f"阈值: {threshold_str}"

        else:
            detection_val_str = f"{detection_value:8.4f}" if detection_value is not None else "    N/A "
            mode_detail = f"未知模式: {detection_val_str}"
            threshold_detail = "阈值: N/A     "

        # 使用富文本格式显示，包含状态图标
        if hasattr(self, 'status_panel'):
            self.status_panel.setText(f"""
                <div style='font-family: monospace;'>
                    <div style='color: {status_color}; font-size: 18px; font-weight: bold;'>
                        {status_text} {status_icon}
                    </div>
                    <div style='font-size: 12px; color: #CCCCCC; margin-top: 5px;'>
                        {mode_detail}
                    </div>
                    <div style='font-size: 12px; color: #AAAAAA; margin-top: 2px;'>
                        {threshold_detail}
                    </div>
                </div>
            """)

    # 左边距更新方法
    def update_left_margin(self):
        """更新左边距时间"""
        self.capture_left_margin = self.left_margin_slider.value() / 10.0
        self.left_margin_label.setText(f"左边距: {self.capture_left_margin:.1f}s")
        self.validate_parameters()

    # 最小波动时长更新方法
    def update_min_volatile_duration(self):
        """更新最小波动时长"""
        self.min_volatile_duration = self.min_volatile_slider.value() / 10.0
        self.min_volatile_label.setText(f"最小波动时长: {self.min_volatile_duration:.1f}s")

        # 验证参数合理性
        min_total = self.capture_left_margin + self.min_volatile_duration + self.capture_right_margin
        if min_total > self.capture_duration:
            self.statusBar().showMessage(
                f"警告：参数不合理！最小总时长({min_total:.1f}s) >= 设定截图时长({self.capture_duration:.1f}s)", 2000)

    # 右边距更新方法
    def update_right_margin(self):
        """更新右边距时间"""
        self.capture_right_margin = self.right_margin_slider.value() / 10.0
        self.right_margin_label.setText(f"右边距: {self.capture_right_margin:.1f}s")
        self.validate_parameters()

    # 验证参数合理性并给出提示
    def validate_parameters(self):
        """验证参数合理性并给出提示"""
        min_total = self.capture_left_margin + self.min_volatile_duration + self.capture_right_margin

        if min_total > self.capture_duration:
            # 参数不合理时，在状态栏显示警告
            self.statusBar().showMessage(
                f"警告：参数不合理！最小总时长({min_total:.1f}s) > 截图时长({self.capture_duration:.1f}s)",
                3000
            )
            return False
        else:
            # 参数合理时，清除警告信息
            remaining = self.capture_duration - min_total
            if remaining > 0:
                self.statusBar().showMessage(
                    f"参数正常，剩余缓冲时间: {remaining:.1f}s",
                    2000
                )
            return True

    # 生成检测区块，分析其是否为波动
    def detect_volatility(self):
        # 每0.1秒生成一个新区块
        current_time = time.time() - self.start_time

        # 生成新区块（仅保留最近N秒的区块）
        window_start = current_time - self.max_window_time
        self.time_blocks = [b for b in self.time_blocks if b["end"] > window_start]

        recent_indices = [i for i, t in enumerate(self.x_data) if t >= current_time - self.block_interval]

        if len(recent_indices) == 0:
            return

        # 为每条曲线收集数据和计算平均值
        curves_data = {}
        curves_means = {}

        for i, group in enumerate(self.curve_groups):
            if 'source_data' in group and len(group['source_data']) > 0:
                # 获取当前区块的数据
                block_data = [group['source_data'][idx] for idx in recent_indices if idx < len(group['source_data'])]
                if len(block_data) > 0:
                    curves_data[i] = block_data
                    curves_means[i] = np.mean(block_data)

        if not curves_data:
            return

        # 根据检测模式计算状态
        if self.detection_mode == "variance":
            # 原有的微观波动检测（方差模式）- 使用第4条曲线（索引3）
            if 3 in curves_data:  # TODO 这个 3
                variance = np.var(curves_data[3]) if len(curves_data[3]) > 1 else 0
                state = "volatile" if variance > self.variance_threshold else "stable"
                detection_value = variance
            else:
                QMessageBox.warning(self, "警告", "当前使用第4条曲线（索引3）作为检测微观波动的依据，但第四条曲线不存在！")
                state = "stable"
                detection_value = 0.0

        elif self.detection_mode == "deviation":
            # 新的宏观波动检测（偏差模式）- 检查所有曲线
            state, detection_results = self.detect_macro_volatility(curves_means)
            detection_value = detection_results

        else:
            # 默认使用方差模式
            if 3 in curves_data:
                variance = np.var(curves_data[3]) if len(curves_data[3]) > 1 else 0
                state = "volatile" if variance > self.variance_threshold else "stable"
                detection_value = variance
            else:
                state = "stable"
                detection_value = 0.0

        # 更新状态显示
        self.update_status_display(state, detection_value)

        # 在生成区块时初始化标记状态
        new_block = {
            "start": current_time - self.block_interval,
            "end": current_time,
            "state": state,
            "marked": False,
            "curves_means": curves_means.copy(),  # 保存所有曲线的平均值
            "detection_value": detection_value  # 保存检测值用于调试
        }

        self.time_blocks.append(new_block)

        # 触发连续波动检测
        self.check_continuous_volatility()

    # 检测宏观波动 - 分别检查每条曲线与其基线的偏差
    # 微观波动的代码直接写在 detect_volatility 中了
    def detect_macro_volatility(self, current_curves_means):
        """检测宏观波动 - 分别检查每条曲线与其基线的偏差"""

        # 需要足够的历史区块来计算基线
        if len(self.time_blocks) < self.baseline_window_size:
            return "stable", {}

        # 获取基线计算所需的历史区块
        baseline_blocks = self.time_blocks[-self.baseline_window_size:]

        # 为每条曲线计算基线和检测偏差
        curves_results = {}
        any_volatile = False

        for curve_idx, current_mean in current_curves_means.items():
            # 收集该曲线的历史平均值
            curve_baseline_means = []
            for block in baseline_blocks:
                if ('curves_means' in block) and (curve_idx in block['curves_means']) and (not block['marked']) and (block['state'] == 'stable'):
                    curve_baseline_means.append(block['curves_means'][curve_idx])

            if len(curve_baseline_means) == 0:
                # 没有足够的历史数据
                curves_results[curve_idx] = {
                    'baseline': 0.0,
                    'current': current_mean,
                    'deviation': 0.0,
                    'state': 'stable'
                }
                continue

            # 计算该曲线的基线平均值
            baseline_average = np.mean(curve_baseline_means)

            # 计算当前值与基线的偏差
            deviation = abs(current_mean - baseline_average)

            # 判断该曲线是否为宏观波动
            curve_state = "volatile" if deviation > self.deviation_threshold else "stable"

            # 记录结果
            curves_results[curve_idx] = {
                'baseline': baseline_average,
                'current': current_mean,
                'deviation': deviation,
                'state': curve_state
            }

            # 如果任意一条曲线波动，整体就标记为波动
            if curve_state == "volatile":
                any_volatile = True

        # 确定整体状态
        overall_state = "volatile" if any_volatile else "stable"

        # # 调试信息
        # if any_volatile:
        #     print(f"宏观波动检测:")
        #     for curve_idx, result in curves_results.items():
        #         if result['state'] == 'volatile':
        #             print(f"  曲线{curve_idx}: 当前={result['current']:.3f}, "
        #                   f"基线={result['baseline']:.3f}, 偏差={result['deviation']:.3f} [波动]")

        return overall_state, curves_results

    # 连续波动检测：检查灵活的稳定-波动-稳定模式
    def check_continuous_volatility(self):
        """检查灵活的稳定-波动-稳定模式"""
        # current_time = time.time()

        # # 如果距离上次检测时间太近，跳过
        # if current_time - self.last_detection_time < 3.0:
        #     print("距离上次检测时间太近")
        #     return

        # 验证参数合理性
        min_total = self.capture_left_margin + self.min_volatile_duration + self.capture_right_margin
        if min_total > self.capture_duration:
            self.statusBar().showMessage(f"参数错误：最小总时长({min_total:.1f}s) >= 截图时长({self.capture_duration:.1f}s)", 2000)
            return

        # 计算需要的总区块数（固定截图时长）
        total_capture_blocks = int(self.capture_duration / self.block_interval)
        # print("total_capture_blocks: ", total_capture_blocks)

        # 如果区块数量不够，退出
        if len(self.time_blocks) < total_capture_blocks:
            # print("区块数量不够")
            return

        # print(
        #     f"搜索模式: 总时长{self.capture_duration}s, 左边界≥{self.capture_left_margin}s, 右边界≥{self.capture_right_margin}s, 最小波动≥{self.min_volatile_duration}s")

        # 从后往前遍历，寻找符合条件的区间
        for i in range(len(self.time_blocks) - total_capture_blocks, -1, -1):
            # 提取固定长度的候选区间
            candidate_blocks = self.time_blocks[i:i + total_capture_blocks]
            # print(f"{len(candidate_blocks)=}")

            # 检查这个区间是否符合灵活模式
            pattern_result = self.find_flexible_pattern(candidate_blocks)

            if pattern_result:
                # 找到匹配的模式
                start_time = candidate_blocks[0]['start']
                end_time = candidate_blocks[-1]['end']

                # stable_left_duration = pattern_result['stable_left_duration']
                # volatile_duration = pattern_result['volatile_duration']
                # stable_right_duration = pattern_result['stable_right_duration']

                # print(f"找到灵活模式！总范围: {start_time:.2f}s - {end_time:.2f}s")
                # print(f"  前稳定期: {stable_left_duration:.2f}s (需要≥{self.capture_left_margin:.2f}s)")
                # print(f"  波动期: {volatile_duration:.2f}s (需要≥{self.min_volatile_duration:.2f}s)")
                # print(f"  后稳定期: {stable_right_duration:.2f}s (需要≥{self.capture_right_margin:.2f}s)")

                # 标记这些区块
                for block in candidate_blocks:
                    block['marked'] = True

                # 直接调用截图函数
                self.take_screenshot(time_range=[start_time, end_time])

                return
            else:
                # print("找不到")
                continue

    # 辅助函数，在固定长度的区块序列中寻找灵活的稳定-波动-稳定模式
    def find_flexible_pattern(self, blocks):
        """在固定长度的区块序列中寻找灵活的稳定-波动-稳定模式"""

        # 最小区块数要求
        min_left_blocks = int(self.capture_left_margin / self.block_interval)
        min_volatile_blocks = int(self.min_volatile_duration / self.block_interval)
        min_right_blocks = int(self.capture_right_margin / self.block_interval)
        self.statusBar().showMessage(
            f"最小区块数要求: 左{min_left_blocks}, 波动{min_volatile_blocks}, 右{min_right_blocks}",
            2000
        )

        # 确保最小区块数不会超过总区块数
        total_min_blocks = min_left_blocks + min_volatile_blocks + min_right_blocks
        if total_min_blocks > len(blocks):
            self.statusBar().showMessage(
                f"区块数不足: 需要{total_min_blocks}, 实际{len(blocks)}",
                2000
            )
            return None

        # 尝试不同的分割点
        # left_end 的范围：从 min_left_blocks 到 允许后续区域有足够空间
        max_left_end = len(blocks) - min_volatile_blocks - min_right_blocks

        for left_end in range(min_left_blocks, max_left_end + 1):
            # volatile_end 的范围：从 left_end + min_volatile_blocks 到 允许右侧区域有足够空间
            min_volatile_end = left_end + min_volatile_blocks
            max_volatile_end = len(blocks) - min_right_blocks

            for volatile_end in range(min_volatile_end, max_volatile_end + 1):

                # 分割三个区域
                left_stable = blocks[0:left_end] if left_end > 0 else []
                volatile_region = blocks[left_end:volatile_end]
                right_stable = blocks[volatile_end:] if volatile_end < len(blocks) else []

                # 检查每个区域的状态
                if (self.check_region_state(left_stable, 'stable') >= min_left_blocks and
                        self.check_region_state(volatile_region, 'volatile')>= min_volatile_blocks and
                        self.check_region_state(right_stable, 'stable') >= min_right_blocks):

                    # 安全计算实际时长
                    stable_left_duration = self.calculate_region_duration(left_stable)
                    volatile_duration = self.calculate_region_duration(volatile_region)
                    stable_right_duration = self.calculate_region_duration(right_stable)

                    # 验证时长要求
                    if (stable_left_duration >= self.capture_left_margin and
                            volatile_duration >= self.min_volatile_duration and
                            stable_right_duration >= self.capture_right_margin):
                        return {
                            'stable_left_duration': stable_left_duration,
                            'volatile_duration': volatile_duration,
                            'stable_right_duration': stable_right_duration,
                            'left_blocks': len(left_stable),
                            'volatile_blocks': len(volatile_region),
                            'right_blocks': len(right_stable)
                        }

        return None

    # 辅助函数，安全计算区域时长
    def calculate_region_duration(self, region_blocks):
        """安全计算区域时长"""
        if not region_blocks:  # 空区域
            return 0.0
        if len(region_blocks) == 1:  # 单个区块
            return region_blocks[0]['end'] - region_blocks[0]['start']
        else:  # 多个区块
            return region_blocks[-1]['end'] - region_blocks[0]['start']

    # 辅助函数，检查区域中的区块，返回所有区块中匹配需要状态的数量
    def check_region_state(self, region_blocks, required_state):
        """检查区域中的区块，返回所有区块中匹配需要状态的数量"""
        if not region_blocks:
            return False

        # 计算指定状态的区块数量
        matching_blocks = sum(1 for block in region_blocks if ((block['state'] == required_state) and (not block['marked'])))

        return matching_blocks

    # (已弃用）
    # 这个可以胜任，比如要截取一长段波动的中的一小块波动，上面那个实现的是截取加载两端平静中间的波动
    #  根据最佳波动段触发截取
    def trigger_auto_capture(self, segment):
        """
        (已弃用）
        这个可以胜任，比如要截取一长段波动的中的一小块波动，上面那个实现的是截取加载两端平静中间的波动

        根据最佳波动段触发截取
        """
        t_center = (segment[0] + segment[1]) / 2
        # print(f"t_center: {t_center}")
        t_min = max(0, t_center - self.capture_duration / 2)
        t_max = t_center + self.capture_duration / 2


        # 边界保护
        if t_max - t_min < self.capture_duration:
            t_max = t_min + self.capture_duration

        # 调用截图
        self.take_screenshot(time_range=(t_min, t_max))

        # 标记已处理区块
        for block in self.time_blocks:
            # 判断区块是否与截取时间段有重叠
            if not (block["end"] < t_min or block["start"] > t_max):
                block["state"] = "stable"
                block["marked"] = True  # 新增标记

    # 清理早于当前窗口的已标记区块
    def clean_marked_blocks(self):
        """清理早于当前窗口的已标记区块"""
        window_start = time.time() - self.start_time - self.max_window_time
        self.time_blocks = [
            b for b in self.time_blocks
            if b["end"] > window_start or not b["marked"]
        ]

    # 更新最大的那个显示窗口时间
    def update_window_time(self, value):
        """更新显示窗口时间"""
        self.max_window_time = value
        self.slider_label.setText(f"显示窗口: {value}秒")

        # 立即修剪现有数据
        current_time = time.time() - self.start_time
        if value > 30:
            self.slider_label.setStyleSheet("color: #FF4500;")  # 长时间显示橙色
        else:
            self.slider_label.setStyleSheet("")  # 恢复默认颜色
        while len(self.x_data) > 0 and self.x_data[0] < current_time - self.max_window_time:
            self.x_data.popleft()
            for group in self.curve_groups:
                group['source_data'].popleft()
                for filt in group['filtered_data'].values():
                    filt.popleft()

        # 动态限制截取时间最大值（窗口的50%）
        max_capture = max(1, int(value * 0.5))
        self.capture_slider.setMaximum(max_capture)
        self.capture_slider_label.setText(f"截取时间: {self.capture_duration}秒 (最大{max_capture}秒)")

    # 更新y轴上下限
    def update_y_range(self):
        # 获取当前值
        new_min = self.min_slider.value()
        new_max = self.max_slider.value()

        # 强制约束关系
        if new_min >= new_max:
            if self.sender() == self.min_slider:
                new_max = new_min + 1
                self.max_slider.setValue(new_max)
            else:
                new_min = new_max - 1
                self.min_slider.setValue(new_min)

        # 更新存储值
        self.min_y = new_min
        self.max_y = new_max

        # 更新标签
        self.min_label.setText(f"Min: {self.min_y}")
        self.max_label.setText(f"Max: {self.max_y}")

        # 更新绘图范围
        if not self.dynamic_y_enabled:  # 仅在非动态模式下生效
            self.plot_widget.setYRange(self.min_y, self.max_y, padding=0)

        # 同步到动态范围按钮状态
        if self.dynamic_y_enabled:
            self.toggle_dynamic_y()  # 关闭动态模式

    # 自动y轴控件
    def toggle_dynamic_y(self):
        self.dynamic_y_enabled = not self.dynamic_y_enabled
        if self.dynamic_y_enabled:
            # 禁用滑块
            self.min_slider.setEnabled(False)
            self.max_slider.setEnabled(False)
            self.plot_widget.enableAutoRange(axis='y')
            self.dynamic_y_button.setText("动态Y轴：开")
            self.dynamic_y_button.setStyleSheet("background-color: #90EE90;")
        else:
            # 启用滑块并应用当前值
            self.min_slider.setEnabled(True)
            self.max_slider.setEnabled(True)
            self.plot_widget.disableAutoRange(axis='y')
            self.plot_widget.setYRange(self.min_y, self.max_y, padding=0)
            self.dynamic_y_button.setText("动态Y轴：关")
            self.dynamic_y_button.setStyleSheet("")

    # 最大最小平均值统计线的开关
    def toggle_stats_visibility(self):
        """切换统计线显示"""
        self.stats_visible = not self.stats_visible
        # 更新所有统计线可见性
        for stats in self.stat_lines:
            for line in stats.values():
                line.setVisible(self.stats_visible)
        # 更新按钮状态
        if self.stats_visible:
            self.stats_button.setText("统计线：开")
            self.stats_button.setStyleSheet("background-color: #90EE90;")
        else:
            self.stats_button.setText("统计线：关")
            self.stats_button.setStyleSheet("")

    # 自动设置Y轴范围到最大差异曲线范围
    def auto_adjust_y_range(self):
        """自动设置Y轴范围到最大差异曲线范围"""
        if not self.x_data:
            QMessageBox.warning(self, "警告", "当前没有可用数据")
            return

        # 获取当前时间窗口范围
        current_time = time.time() - self.start_time
        window_start = current_time - self.max_window_time
        valid_indices = [i for i, t in enumerate(self.x_data) if t >= window_start]

        if not valid_indices:
            return

        # 遍历所有曲线组找最大差异
        max_range = 0
        target_min = 4096
        target_max = 0

        for group in self.curve_groups:
            # 获取窗口内数据
            window_data = [group['source_data'][i] for i in valid_indices]
            if not window_data:
                continue

            # 计算当前曲线范围
            curr_min = min(window_data)
            curr_max = max(window_data)
            curr_range = curr_max - curr_min

            # 更新最大范围
            if curr_range > max_range:
                max_range = curr_range
                target_min = curr_min
                target_max = curr_max

        if max_range == 0:
            return

        # 添加10%余量
        margin = (target_max - target_min) * 0.1
        new_min = max(0, target_min - margin)
        new_max = min(4096, target_max + margin)

        # 关闭动态Y轴（如果开启）
        if self.dynamic_y_enabled:
            self.toggle_dynamic_y()

        # 更新Y轴范围和滑块
        self.min_y = new_min
        self.max_y = new_max
        self.plot_widget.setYRange(new_min, new_max, padding=0)

        # 更新滑块位置（带数值限制）
        self.min_slider.setValue(int(new_min))
        self.max_slider.setValue(int(new_max))

    # 清屏
    def reset_system(self):
        """执行系统初始化重置"""
        # 确认对话框
        # reply = QMessageBox.question(
        #     self, '确认重置',
        #     "确定要清空所有数据并恢复默认设置吗？",
        #     QMessageBox.Yes | QMessageBox.No, QMessageBox.No
        # )
        # if reply == QMessageBox.No:
        #     return

        # 清空数据缓存
        self.x_data.clear()
        for group in self.curve_groups:
            group['source_data'].clear()
            for filt in group['filtered_data'].values():
                filt.clear()

        # 重置图表显示
        for curve in self.curves:
            curve.setData([], [])

        # 恢复默认设置
        self.min_y = 0
        self.max_y = 4096
        self.max_window_time = 10

        # 重置控件状态
        # self.time_slider.setValue(10)
        self.min_slider.setValue(0)
        self.max_slider.setValue(4096)
        self.dynamic_y_enabled = False
        self.stats_visible = False

        # 更新UI显示
        self.plot_widget.setYRange(0, 4096, padding=0)
        self.dynamic_y_button.setText("动态Y轴：关")
        self.dynamic_y_button.setStyleSheet("")
        self.stats_button.setText("统计线：关")

        # 隐藏统计线
        for stats in self.stat_lines:
            for line in stats.values():
                line.setVisible(False)


        # 取消自动截取状态
        if self.auto_capture_enabled:
            self.toggle_auto_capture()

        if self.is_recording:
            self.stop_recording()

    # 打开设置界面（运行中，暂停状态下可用）
    def show_settings(self):
        settings_dialog = SettingsDialog(current_settings=self.settings, parent=self)
        if settings_dialog.exec_():
            new_settings = settings_dialog.get_settings()
            # 更新模拟数据按钮可见性
            self.sim_mode_btn.setVisible(new_settings['use_simulated_data'])

            # 检查是否切换了数据源类型
            data_source_changed = (new_settings['use_simulated_data'] != self.settings['use_simulated_data'])

            if new_settings != self.settings:
                self.settings = new_settings
                # 更新校验设置
                self.calibration_enabled = new_settings['calibration_enabled']
                self.reference_curve_index = new_settings['reference_curve_index']
                self.calibration_tolerance = new_settings.get('calibration_tolerance', 1)

                # 重新创建UI以反映校验设置变化
                self.update_calibration_ui_visibility()

                # 处理数据源切换
                if data_source_changed:
                    if new_settings['use_simulated_data']:
                        # 切换到模拟数据：关闭串口，启动进程
                        if hasattr(self, 'ser') and self.ser.is_open:
                            self.ser.close()
                        self.start_data_generator_process()
                    else:
                        # 切换到串口数据：停止进程，打开串口
                        self.stop_data_generator_process()
                        try:
                            self.ser = serial.Serial(self.settings['serial_port'], self.settings['baudrate'],
                                                     timeout=0.5)
                        except serial.serialutil.SerialException as e:
                            QMessageBox.critical(self, "串口错误", f"无法打开串口: {e}")
                            return
                else:
                    # 同一数据源类型，但参数可能变化
                    if not self.settings['use_simulated_data']:
                        try:
                            # 关闭现有连接
                            if hasattr(self, 'ser') and self.ser:
                                self.ser.close()

                            # 创建新连接
                            if new_settings['connection_type'] == 'bluetooth':
                                self.ser = create_serial_interface(
                                    'bluetooth',
                                    device_name=new_settings['ble_device_name']
                                )
                            else:
                                self.ser = create_serial_interface(
                                    'standard',
                                    port=new_settings['serial_port'],
                                    baudrate=new_settings['baudrate']
                                )

                            self.ser.open()

                        except Exception as e:
                            QMessageBox.critical(self, "连接错误", f"无法建立连接: {e}")
                            return
                    else:
                        # 模拟数据参数变化，发送配置更新命令
                        self.send_control_command('config_update', {})

                self.reinitialize_curves()
                self.is_paused = False
                self.pause_button.setText("暂停 ||")
                self.settings_button.setEnabled(False)

    # 绘图用
    def reinitialize_curves(self):
        # 清除现有曲线
        self.plot_widget.clear()

        # 重新创建曲线
        self.curves = []
        for i in range(self.settings['num_curve_groups']):
            color = self.curve_groups[i]['color']
            # 源曲线
            source_curve = self.plot_widget.plot(pen=pg.mkPen(color=color, width=2, style=QtCore.Qt.SolidLine))  # type: ignore
            self.curves.append(source_curve)
            # 滤波曲线
            for j, filter_name in enumerate(self.settings['selected_filters']):
                if filter_name != '原数据':
                    filtered_curve = self.plot_widget.plot(pen=pg.mkPen(color=color, width=2, style=QtCore.Qt.DashLine))  # type: ignore
                    self.curves.append(filtered_curve)

        # 重置数据
        self.x_data = deque()
        self.curve_groups = []
        colors = [
            (255, 0, 0),    # 红色
            (255, 165, 20),  # 橙色
            (255, 255, 0),  # 黄色
            (0, 255, 0),  # 绿色
            (0, 255, 255),  # 青色
            (0, 0, 255),  # 蓝色
            (255, 0, 255),  # 紫色
            (255, 255, 255),  # 白色
        ]
        for _ in range(self.settings['num_curve_groups']):
            self.curve_groups.append({
                'source_data': deque(),
                'filtered_data': {filter_name: deque() for filter_name in self.settings['selected_filters']},
                'color': colors[_]
            })

    # 绘图用
    def update_plot(self):
        # 计算当前时间与程序开始时间的差值
        current_time = time.time()
        time_diff = current_time - self.start_time



        # 模拟数据生成：从数据生成进程接收数据
        if self.settings['use_simulated_data']:
            simulated_values = self.receive_simulated_data()
            if simulated_values is not None:
                # 格式化为字符串，保持与原有串口数据格式一致
                line = ' '.join(map(str, simulated_values))
            else:
                line = ''
        else:
            if self.ser.in_waiting() > 0:
                # TODO 这里每次读完数据都清空缓冲区，“负反馈自动控制”，如果有延迟就只显示第一行的数据，删掉累积的。当然这很暴力，期待更新
                line = self.ser.readline().decode('utf-8').strip()
                self.ser.reset_input_buffer()

            else:
                line = ''

        # 处理缓冲区中的数据
        if line:

            matches = re.findall(r'\d+', line)

            if len(matches) >= self.settings['num_curve_groups']:
                number = [int(match) for match in matches]

                # 应用校验校正
                if self.calibration_enabled and hasattr(self, 'apply_calibration_correction'):
                    number = self.apply_calibration_correction(number)

                # 保存数据到文件
                data_line = f"{time_diff}," + ",".join(map(str, number)) + "\n"
                self.file.write(data_line)
                self.file.flush()

                # 标定数据收集
                if self.is_calibrating:
                    self.collect_calibration_data()


                # 记录当前时间戳
                current_time = time.time()
                time_diff = current_time - self.start_time

                # 添加时间戳到x_data
                self.x_data.append(time_diff)

                # 移除超过设置时间的数据点
                while self.x_data and self.x_data[0] < time_diff - self.max_window_time:
                    self.x_data.popleft()
                    for i in range(self.settings['num_curve_groups']):
                        if self.curve_groups[i]['source_data']:
                            self.curve_groups[i]['source_data'].popleft()
                        for filter_name in self.settings['selected_filters']:
                            if self.curve_groups[i]['filtered_data'][filter_name]:
                                self.curve_groups[i]['filtered_data'][filter_name].popleft()

                for i in range(self.settings['num_curve_groups']):
                    self.curve_groups[i]['source_data'].append((4096 - number[i]))

                    # 应用滤波
                    for filter_name in self.settings['selected_filters']:
                        if filter_name == '原数据':
                            self.curve_groups[i]['filtered_data'][filter_name].append(self.curve_groups[i]['source_data'][-1])
                        elif filter_name == '均值滤波':
                            kernel_size = 3
                            if len(self.curve_groups[i]['source_data']) >= kernel_size:
                                filtered = mean_filter(np.array(self.curve_groups[i]['source_data']), kernel_size)
                                self.curve_groups[i]['filtered_data'][filter_name].append(filtered[-1])
                            else:
                                self.curve_groups[i]['filtered_data'][filter_name].append(self.curve_groups[i]['source_data'][-1])
                        elif filter_name == '高斯滤波':
                            kernel_size = 3
                            sigma = 1
                            if len(self.curve_groups[i]['source_data']) >= kernel_size:
                                filtered = gaussian_filter(np.array(self.curve_groups[i]['source_data']), kernel_size, sigma)
                                self.curve_groups[i]['filtered_data'][filter_name].append(filtered[-1])
                            else:
                                self.curve_groups[i]['filtered_data'][filter_name].append(self.curve_groups[i]['source_data'][-1])
                        elif filter_name == '中值滤波':
                            kernel_size = 3
                            if len(self.curve_groups[i]['source_data']) >= kernel_size:
                                filtered = median_filter(np.array(self.curve_groups[i]['source_data']), kernel_size)
                                self.curve_groups[i]['filtered_data'][filter_name].append(filtered[-1])
                            else:
                                self.curve_groups[i]['filtered_data'][filter_name].append(self.curve_groups[i]['source_data'][-1])

            else:
                # QMessageBox.critical(self, "数据错误",
                #                      f"接收到的数据条数不匹配！\n设置的曲线组数量: {self.settings['num_curve_groups']}\n接收到的数据条数: {len(matches)}\n接收到的数据: {line}")
                print(
                    f"接收到的数据条数不匹配！设置的曲线组数量: {self.settings['num_curve_groups']}，接收到的数据条数: {len(matches)}，数据: {line}")
                return

        current_time = time.time()
        if self.auto_capture_enabled and not self.is_paused:
            if current_time - self.last_detection_time >= self.block_interval:
                self.detect_volatility()
                self.last_detection_time = current_time

        if self.auto_capture_enabled and current_time - self.last_clean_time > self.max_window_time:
            # TODO 这里会导致卡顿一下，貌似。我想能不能直接 pop 那些 block ，平均化这个卡顿
            self.clean_marked_blocks()
            self.last_clean_time = current_time

        if self.is_paused:
            return

        # 更新曲线
        for i in range(self.settings['num_curve_groups']):
            # 源曲线
            self.curves[i].setData(list(self.x_data), list(self.curve_groups[i]['source_data']))
            # 滤波曲线
            for j, filter_name in enumerate(self.settings['selected_filters']):
                if filter_name != '原数据':
                    index = i + j * self.settings['num_curve_groups']
                    if index < len(self.curves):
                        self.curves[index].setData(list(self.x_data), list(self.curve_groups[i]['filtered_data'][filter_name]))

        # 更新统计线
        self.update_stat_lines()


        # 控制视频帧率
        if self.is_recording and not self.is_paused:
            # 如果正在录制，捕获当前帧和数据
            if current_time - self.last_frame_time >= self.frame_interval:
                # 捕获当前图表为QImage
                img = self.plot_widget.grab().toImage()

                # 转换为OpenCV格式
                ptr = img.bits()
                ptr.setsize(img.byteCount())
                arr = np.array(ptr).reshape(img.height(), img.width(), 4)  # RGBA
                frame = cv2.cvtColor(arr, cv2.COLOR_RGBA2BGR)

                # 保存帧和数据
                self.video_writer.write(frame)  # 直接写入
                current_data = [d['source_data'][-1] for d in self.curve_groups]
                self.recording_data.append(current_data)

                # 实时写入视频（或批量写入）
                if self.video_writer is not None:
                    self.video_writer.write(frame)
                self.last_frame_time = current_time  # 更新时间戳

    # 绘图-统计线
    def update_stat_lines(self):

        # 只在统计线可见时更新
        if not self.stats_visible:
            return

        # 获取当前视图范围
        view_range = self.plot_widget.viewRange()
        x_range = view_range[0]

        # 转换为数组索引
        x_data = np.array(self.x_data)
        if len(x_data) == 0:
            return

        # 找出在可视范围内的数据索引
        start_idx = np.searchsorted(x_data, x_range[0], side='left')
        end_idx = np.searchsorted(x_data, x_range[1], side='right')
        visible_indices = slice(max(0, start_idx - 1), min(len(x_data), end_idx + 1))  # type: ignore

        # 对每条曲线更新统计线
        for i, stats in enumerate(self.stat_lines):
            if len(self.curve_groups[i]['source_data']) < 2:
                continue

            # 获取可见范围内的数据
            visible_data = np.array(list(self.curve_groups[i]['source_data']))[visible_indices]

            if len(visible_data) > 0:
                # 计算统计值
                max_val = np.max(visible_data)
                min_val = np.min(visible_data)
                mean_val = np.mean(visible_data)

                # 更新线位置
                stats['max'].setPos(max_val)
                stats['min'].setPos(min_val)
                stats['mean'].setPos(mean_val)

                # 设置可见性
                stats['max'].setVisible(True)
                stats['min'].setVisible(True)
                stats['mean'].setVisible(True)
            else:
                stats['max'].setVisible(False)
                stats['min'].setVisible(False)
                stats['mean'].setVisible(False)

    # 关闭
    def closeEvent(self, event):
        if self.is_recording:
            self.stop_recording()

        # 停止数据生成进程
        if self.settings['use_simulated_data']:
            self.stop_data_generator_process()
        else:
            if hasattr(self, 'ser') and self.ser.is_open:
                self.ser.close()

        self.file.close()
        for i in range(len(self.fake_csvs)):
            self.fake_csvs[i]["is_used"] = False
        self.config.update({
            'max_window_time': self.max_window_time,
            'capture_duration': self.capture_duration,
            'detection_mode': self.detection_mode,
            'variance_threshold': self.variance_threshold,
            'deviation_threshold': self.deviation_threshold,
            'capture_left_margin': self.capture_left_margin,
            'capture_right_margin': self.capture_right_margin,
            'min_volatile_duration': self.min_volatile_duration,
            'dynamic_y_enabled': self.dynamic_y_enabled,
            'calibration_enabled': getattr(self, 'calibration_enabled', False),
            'reference_curve_index': getattr(self, 'reference_curve_index', 0),
            'calibration_tolerance': getattr(self, 'calibration_tolerance', 1),
            'connection_type': getattr(self.settings, 'connection_type', 'standard'),
            'ble_device_name': getattr(self.settings, 'ble_device_name', 'ESP32C3-Data'),
            'fake_csvs': self.fake_csvs,
        })
        save_config(self.config)
        event.accept()

    # 打开设置界面
    def show_settings_dialog(self, first_run=False):
        settings_dialog = SettingsDialog(
            current_settings=self.settings,
            parent=self,
            is_first_run=first_run  # 传递是否是首次运行的标志
        )
        if settings_dialog.exec_():
            new_settings = settings_dialog.get_settings()
            # 合并到配置
            self.config.update({
                'serial_port': new_settings['serial_port'],
                'connection_type': new_settings['connection_type'],
                'ble_device_name': new_settings['ble_device_name'],
                'baudrate': new_settings['baudrate'],
                'num_curve_groups': new_settings['num_curve_groups'],
                'use_simulated_data': new_settings['use_simulated_data'],
                'selected_filters': new_settings['selected_filters'],
                'neural_net_enabled': new_settings['neural_net_enabled'],
                'calibration_enabled': new_settings['calibration_enabled'],
                'reference_curve_index': new_settings['reference_curve_index'],
                'calibration_tolerance': new_settings.get('calibration_tolerance', 1),
                'max_window_time': self.max_window_time,
                'capture_duration': self.capture_duration,
                'detection_mode': self.detection_mode,
                'variance_threshold': self.variance_threshold,
                'deviation_threshold': self.deviation_threshold,
                'capture_left_margin': self.capture_left_margin,
                'capture_right_margin': self.capture_right_margin,
                'min_volatile_duration': self.min_volatile_duration,
                'dynamic_y_enabled': self.dynamic_y_enabled,
            })
            # 保存到文件
            save_config(self.config)
            # 首次运行时设置主文件名
            if first_run:
                self.main_filename = new_settings['main_filename']
            self.settings.update(new_settings)


def sensor_monitor():
    app = QApplication(sys.argv)
    mainWindow = RealTimePlot()
    mainWindow.show()
    sys.exit(app.exec_())


CONFIG_PATH = Path("sensor_monitor_config.json")

if __name__ == '__main__':
    sensor_monitor()

# TODO 加一个按按钮直接生成按压形状的功能
# TODO 加一个