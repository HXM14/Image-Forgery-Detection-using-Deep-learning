from PyQt5.QtWidgets import QApplication , QFileDialog  , QFrame,QComboBox,  QLineEdit , QLabel, QHBoxLayout, QAction,QRadioButton , QMainWindow, QMenu, QVBoxLayout, QSizePolicy, QMessageBox, QWidget, QPushButton
from PyQt5.QtCore import *
from PyQt5 import QtGui
from PyQt5 import QtCore
from PyQt5.QtGui import QPixmap

from PIL import Image

import numpy as np
import sys
import os

from Result_Window_Final import ResultWindow
"""
import ELA_Module
import VGG16_Module
import VGG19_Module
import SVM_Module
"""
class HelpWindow(QWidget):
    def __init__(self, parent = None):
        """constructor to create a new window with charactersitis after create object from class window"""

        super().__init__()
        self.title = "IFD Application"
        self.top = 200
        self.left = 500
        self.width = 1086
        self.height = 680
        self.init_window()

    def init_window(self):
        """initialize window"""

        self.setWindowTitle(self.title)
        self.setWindowIcon(QtGui.QIcon("icons8-cbs-512.ico"))  # icon Pic File name
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.setFixedSize(self.width, self.height)

        pixmap = QPixmap("C:\\Users\\Mohamed-PC\\PycharmProjects\\graduation_project\\Final.png")
        self.label = QLabel(self)
        self.label.setPixmap(pixmap)
        self.label.resize(1086, 680)
        self.label.setPixmap(pixmap.scaled(self.label.size(), Qt.IgnoreAspectRatio))

        self.show()

if __name__ == "__main__":
    App = QApplication(sys.argv)
    App.setStyle('Fusion')
    window = HelpWindow()
    sys.exit(App.exec())