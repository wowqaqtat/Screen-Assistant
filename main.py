
"""
生成ui
pyuic5 -o ui.py ui.ui

一键安装依赖包
pip install -r requirements.txt

打包命令
pyinstaller -F -i icon.ico main.py --noconsole
"""

import sys
import os
import random
from ui import Ui_MainWindow
from PyQt5.QtWidgets import QApplication, QMainWindow  # 主窗口类
from PyQt5.QtGui import QIcon # 图标
from PyQt5.QtWidgets import QShortcut  # 创建快捷键
from PyQt5.QtGui import QKeySequence  # 快捷键的序列
from PyQt5.QtWidgets import QLabel, QWidget, QVBoxLayout  # 标签、窗口部件
from PyQt5.QtGui import QPixmap  # 图像
from PyQt5.QtCore import Qt


class MainWindow(QMainWindow, Ui_MainWindow):
    """主窗口类"""

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle('友好的屏保')  # 窗口标题
        self.setWindowIcon(QIcon("icon.png")) # 窗口图标
        self.setGeometry(0, 0, 1920, 1080)  # 窗口大小
        self.bind()
        ImageDisplay.set_image(self)

    def bind(self):
        """按键事件"""
        shortcut = QShortcut(QKeySequence('esc'), self)
        shortcut.activated.connect(lambda: self.screen_size())

    def screen_size(self):
        """设置屏幕大小"""
        # 用户可以按 Esc 或 win+D 最小化
        self.showMinimized()  # 最小化窗口


class ImageDisplay():
    """加载图片"""

    def __init__(self):
        self.set_image()

    def set_image(self):
        """设置图片"""
        image_folder_path = ImageDisplay.get_config(self)
        # image_folder_path = './image'  # 也可以直接设置文件夹路径
        image_files = ImageDisplay.set_random_image(self, image_folder_path)
        self.pixmap = QPixmap(image_files)
        # self.pixmap = QPixmap('./image/image.png') # 也可以直接设置图片
        self.label = QLabel(self)
        self.label.setPixmap(self.pixmap)
        layout = QVBoxLayout()
        layout.addWidget(self.label)
        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)
        self.label.setScaledContents(True)  # 缩放
        self.label.setAlignment(Qt.AlignCenter)  # 居中
        self.setFixedSize(self.pixmap.width(), self.pixmap.height())  # 全屏

    def create_config(self, path):
        """写入配置文件"""
        import configparser
        config = configparser.ConfigParser()
        config['settings'] = {'path': path}
        with open('config.ini', 'w') as configfile:
            config.write(configfile)

    def get_config(self):
        """获取配置文件"""
        import configparser
        config = configparser.ConfigParser()
        try:
            config.read('config.ini')
            settings = config['settings']
            path = settings.get('path')
            image_folder_path = path
            return image_folder_path
        except (configparser.Error, KeyError, FileNotFoundError) as e:
            print(f'Error:配置文件未获取{e}')
            ImageDisplay.create_config(self, './image')  # 写入配置文件
        return './image'

    def select_folder(self):
        """选择文件夹"""
        import tkinter as tk
        from tkinter import filedialog
        root = tk.Tk()
        root.withdraw()
        return filedialog.askdirectory()

    def set_random_image(self, image_folder_path):
        """设置随机图片"""
        # 无效的文件夹路径
        if not os.path.isdir(image_folder_path):
            print('Error:文件夹路径错误')
            image_folder_path = ImageDisplay.select_folder(self)

        # 有效的文件夹路径
        if os.path.isdir(image_folder_path):
            ImageDisplay.create_config(self, image_folder_path)  # 写入配置文件
            try:
                image_files = [os.path.join(image_folder_path, f) for f in os.listdir(
                    image_folder_path) if f.endswith('.jpg') or f.endswith('.jpeg') or f.endswith('.png')]
                if image_files:
                    return QPixmap(random.choice(image_files))
                else:
                    print('Error:文件夹中无图片')
                    image_folder_path = ImageDisplay.select_folder(self)
                    ImageDisplay.set_random_image(self, image_folder_path)
            except Exception as e:
                print(f'Error:{e}')
        else:
            print('Error:未选择文件夹路径')
            sys.exit(0)
        return 0


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    # mainWindow.show() # 普通显示
    mainWindow.showFullScreen()  # 全屏
    sys.exit(app.exec_())
