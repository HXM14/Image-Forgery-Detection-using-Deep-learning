from PyQt5.QtWidgets import QApplication  , QComboBox, QLabel, QWidget, QPushButton
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import *
from PyQt5 import QtCore
from PyQt5 import QtGui

from Test_window_Final import Test_window
from Training_window_Final import Training_window

import sys

class MainWindow(QWidget):
    def __init__(self, parent = None):
        """constructor to create a new window with charactersitis after create object from class window"""
        super().__init__()
        self.title = "IFD Application"
        self.top = 200
        self.left = 500
        self.width = 550
        self.height = 260
        self.file_path = ""
        self.init_window()

    def init_window(self):
        """initialize Main IFD window"""

        self.setWindowTitle(self.title)
        self.setWindowIcon(QtGui.QIcon("icons8-cbs-512.ico")) #icon Pic File name
        self.setGeometry(self.left , self.top , self.width , self.height)
        self.setFixedSize(self.width , self.height)

        label = QLabel(self)
        label.move(175,40)
        label.setText('Image')
        label.setFont(QtGui.QFont("Sanserif" , 24))



        label = QLabel(self)
        label.move(175, 70)
        label.setText('Forgery')
        label.setFont(QtGui.QFont("Sanserif", 24))

        label = QLabel(self)
        label.move(175, 100)
        label.setText('Detection')
        label.setFont(QtGui.QFont("Sanserif", 24))

        label = QLabel(self)
        label.move(20, 200)
        label.setText('Click training or testing to start the process:')
        label.setFont(QtGui.QFont("Sanserif", 8))

        pixmap = QPixmap("C:\\Users\\Mohamed-PC\\PycharmProjects\\graduation_project\\icons8-cbs-512.png")
        self.label = QLabel(self)
        self.label.setPixmap(pixmap)
        self.label.resize(190, 190)
        self.label.move(0, 10)
        self.label.setPixmap(pixmap.scaled(self.label.size(), Qt.IgnoreAspectRatio))
        self.label.show()


        self.combo = QComboBox(self)
        self.combo.addItem("Training")
        self.combo.addItem("Testing")
        self.combo.setGeometry(QRect(234, 198,300 , 20))


        self.button = QPushButton("Start", self)
        self.button.setGeometry(QRect(445, 230, 90, 20))
        self.button.setIcon(QtGui.QIcon("start.png")) #icon Pic File name
        self.button.setIconSize(QtCore.QSize(15, 15))  # to change icon Size
        self.button.setToolTip("<h5>Lunch Your choice either Training or Testing<h5>")
        self.button.clicked.connect(self.on_click)


        self.show()

    def on_click(self):
        if str(self.combo.currentText()) == "Training":
            self.training_window = Training_window()
            self.training_window.show()
            self.close()

        elif str(self.combo.currentText()) == "Testing":
            self.test_window= Test_window()
            self.test_window.show()
            self.close()


if __name__ == "__main__":
    App = QApplication(sys.argv)
    App.setStyle('Fusion')
    window = MainWindow()
    sys.exit(App.exec())
