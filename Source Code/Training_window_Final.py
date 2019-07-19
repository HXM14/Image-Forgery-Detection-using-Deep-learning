from PyQt5.QtWidgets import QApplication , QFileDialog  , QFrame,QComboBox,  QLineEdit , QLabel, QAction, QMessageBox, QWidget, QPushButton
from PyQt5.QtCore import *
from PyQt5 import QtGui
from PyQt5 import QtCore
from PyQt5.QtGui import QPixmap

from pylab import *

import sys
import shutil
import random
import os
import csv

import ELA_Training_Module_Final
import VGG16_Training_Module_Final
import VGG19_Training_Module_Final

#import Test_with_Retraind_Modules

from help_Window import HelpWindow


class thread(QThread):
    def __init__(self):
        QThread.__init__(self)
    def __del__(self):
        self.wait()

    def train_model(self , CSV_file , lr , ep, flag = ""):
        if flag == "ELA":
            plot , model = ELA_Training_Module_Final.train_Ela_Model(CSV_file , lr , ep)
            return plot , model
        elif flag == "VGG16":
            plot, model = VGG16_Training_Module_Final.train_VGG16_Model(CSV_file , lr , ep)
            return plot, model
        elif flag == "VGG19":
            plot, model = VGG19_Training_Module_Final.train_VGG19_Model(CSV_file , lr , ep)
            return plot, model


class Training_window(QWidget):
    def __init__(self, parent = None):
        """constructor to create a new window with charactersitis after create object from class window"""
        super().__init__()
        self.title = "IFD Application"
        self.top = 200
        self.left = 500
        self.width = 550
        self.height = 390
        self.file_path_Authentic = ""
        self.file_path_Tampered = ""
        self.csv_file = ""
        self.plot = ""
        self.model = ""
        self.current = os.getcwd()
        self.Dataset = "\CSV_files"
        self.figures = "\Figures"
        self.Models = "\Re_Traind_Models"
        try:
            # Create target Directory
            os.mkdir(self.current + self.Dataset)
        except FileExistsError:
            pass
        try:
            # Create target Directory
            os.mkdir(self.current + self.figures)
        except FileExistsError:
            pass
        try:
            # Create target Directory
            os.mkdir(self.current + self.Models)
        except FileExistsError:
            pass

        self.init_window()

    def init_window(self):
        """initialize window"""
        self.setWindowTitle(self.title)
        self.setWindowIcon(QtGui.QIcon("icons8-cbs-512.ico")) #icon Pic File name
        self.setGeometry(self.left , self.top , self.width , self.height)
        self.setFixedSize(self.width , self.height)
        self.label = QLabel(self)
        self.label2 = QLabel(self)
        self.label3 = QLabel(self)
        self.label4 = QLabel(self)
        self.label_1 = QLabel(self)
        self.label_2 = QLabel(self)

        quit = QAction("Quit", self)
        quit.triggered.connect(self.closex)

        #Label
        label = QLabel(self)
        label.move(10,44)
        label.setText('Tampered')
        label.setFont(QtGui.QFont("Sanserif" ,8))

        #Label
        label = QLabel(self)
        label.move(10,68)
        label.setText('Authentic')
        label.setFont(QtGui.QFont("Sanserif" , 8))

        #label
        label = QLabel(self)
        label.setText('learning Rate ')
        label.setFont(QtGui.QFont("Sanserif", 8))
        label.move(368, 144)

        #label
        label = QLabel(self)
        label.setText('epochs')
        label.setFont(QtGui.QFont("Sanserif", 8))
        label.move(368, 165)

        #label
        label = QLabel(self)
        label.setText('Training Parameters')
        label.setFont(QtGui.QFont("Sanserif", 8))
        label.move(365, 110)

        #label
        label = QLabel(self)
        label.setText('Training Result')
        label.setFont(QtGui.QFont("Sanserif", 8))
        label.move(10, 90)

        #text Box
        self.line_edit_1 = QLineEdit(self)
        self.line_edit_1.setReadOnly(True)
        self.line_edit_1.setFont(QtGui.QFont("Sanserif", 8))
        self.line_edit_1.setGeometry(QRect(80, 40, 365, 20))
        self.line_edit_1.setPlaceholderText("Browse Tampered images Directory")

        #text Box
        self.line_edit_2 = QLineEdit(self)
        self.line_edit_2.setReadOnly(True)
        self.line_edit_2.setFont(QtGui.QFont("Sanserif", 8))
        self.line_edit_2.setGeometry(QRect(80, 64, 365, 20))
        self.line_edit_2.setPlaceholderText("Browse ِAuthentic images Directory")

        #text Box
        self.lr = QLineEdit(self)
        self.lr.setFont(QtGui.QFont("Sanserif", 8))
        self.lr.setGeometry(QRect(436, 140, 70, 20))
        self.lr.setPlaceholderText("learning Rate")

        #text Box
        self.ep= QLineEdit(self)
        self.ep.setFont(QtGui.QFont("Sanserif", 8))
        self.ep.setGeometry(QRect(436, 165, 70, 20))
        self.ep.setPlaceholderText("epochs")



        #Button
        self.button_1 = QPushButton("Browse", self)
        self.button_1.setGeometry(QRect(450, 40, 90, 20))
        self.button_1.setToolTip("<h5>Browse image from your computer to start test!<h5>")  # Notice using h2 tags From Html
        self.button_1.setIcon(QtGui.QIcon("698831-icon-105-folder-add-512.png")) #icon Pic File name
        self.button_1.setIconSize(QtCore.QSize(15, 15))  # to change icon Size
        self.button_1.clicked.connect(self.getfiles_Tampered)

        # Button
        self.button_2 = QPushButton("Browse", self)
        self.button_2.setGeometry(QRect(450, 64, 90, 20))
        self.button_2.setToolTip(
            "<h5>Browse image from your computer to start test!<h5>")  # Notice using h2 tags From Html
        self.button_2.setIcon(QtGui.QIcon("698831-icon-105-folder-add-512.png"))  # icon Pic File name
        self.button_2.setIconSize(QtCore.QSize(15, 15))  # to change icon Size
        self.button_2.clicked.connect(self.getfiles_Authentic )

        # Button
        self.button_3 = QPushButton("Create CSV file", self)
        self.button_3.setGeometry(QRect(440, 88, 100, 20))
        self.button_3.setToolTip("<h5>Browse image from your computer to start test!<h5>")  # Notice using h2 tags From Html
        self.button_3.setIcon(QtGui.QIcon("create.png"))  # icon Pic File name
        self.button_3.setIconSize(QtCore.QSize(15, 15))  # to change icon Size
        self.button_3.clicked.connect(self.Make_CSV_file )

        #Button
        self.button = QPushButton("test", self)
        self.button.setGeometry(QRect(90, 360, 90, 20))
        self.button.setToolTip("<h5>test image either Forged or Not Forged!<h5>")  # Notice using h2 tags From Html
        self.button.setIcon(QtGui.QIcon("698827-icon-101-folder-search-512.png")) #icon Pic File name
        self.button.setIconSize(QtCore.QSize(15, 15))  # to change icon Size
        self.button.clicked.connect(self.go_to_test_window)

        #Button
        self.button = QPushButton("Back", self)
        self.button.setGeometry(QRect(180, 360, 90, 20))
        self.button.setToolTip("<h5>test image either Forged or Not Forged!<h5>")  # Notice using h2 tags From Html
        self.button.setIcon(QtGui.QIcon("repeat-pngrepo-com.png")) #icon Pic File name
        self.button.setIconSize(QtCore.QSize(15, 15))  # to change icon Size
        self.button.clicked.connect(self.back_to_Main)

        #Button
        self.button_4 = QPushButton("Train", self)
        self.button_4.setGeometry(QRect(270, 360, 90, 20))
        self.button_4.setToolTip("<h5>test image either Forged or Not Forged!<h5>")  # Notice using h2 tags From Html
        self.button_4.setIcon(QtGui.QIcon("Rocket-icon-blue.png")) #icon Pic File name
        self.button_4.setIconSize(QtCore.QSize(15, 15))  # to change icon Size
        self.button_4.clicked.connect(self.on_click)

        #Button
        self.button = QPushButton(" Quit", self)
        self.button.setGeometry(QRect(360, 360, 90, 20))
        self.button.setToolTip("<h5>Close the program!<h5>")  # Notice using h2 tags From Html
        self.button.setIcon(QtGui.QIcon("cancel-symbol-transparent-9.png")) #icon Pic File name
        self.button.setIconSize(QtCore.QSize(15, 15))  # to change icon Size
        self.button.clicked.connect(self.close_main_window)

        #Button
        #self.button = QPushButton("Help", self)
        #self.button.setGeometry(QRect(450, 360, 90, 20))
        #self.button.setToolTip("<h5>Help!<h5>")  # Notice using h2 tags From Html
        #self.button.setIcon(QtGui.QIcon("icons8-faq-100 (1).png")) #icon Pic File name
        #self.button.setIconSize(QtCore.QSize(15, 15))  # to change icon Size
        #self.button.clicked.connect(self.on_click_help)


        label = QLabel(self)
        label.setText('Model ')
        label.setFont(QtGui.QFont("Sanserif", 8))
        label.move(10, 20)


        self.combo = QComboBox(self)
        self.combo.addItem("Error Level Analysis")
        self.combo.setToolTip("<h5>ELA<h5>")
        self.combo.addItem("VGG16")
        self.combo.setToolTip("<h5>VGG16<h5>")
        self.combo.addItem("VGG19")
        self.combo.setToolTip("<h5>VGG19<h5>")

        self.combo.setGeometry(QRect(80, 15,460 , 20))



        #topright = QFrame(self)
        #topright.setFrameShape(QFrame.StyledPanel)
        #topright.setGeometry(QRect(365, 125,150 , 230))


        topleft = QFrame(self)
        topleft.setFrameShape(QFrame.StyledPanel)
        topleft.setGeometry(QRect(10, 105,350 , 250))
        self.show()

    @pyqtSlot()
    def go_to_test_window(self):
        from Test_with_Retraind_Modules import Test_window
        head, tail = os.path.split(self.model)
        print("*"*50)
        print("Training_Window_Final ")
        print(tail)
        print(self.model)
        print("*"*50)
        self.Test_window = Test_window(self ,model_path= self.model , model_name=tail)
        self.Test_window.show()
        self.close()

    @pyqtSlot()
    def back_to_Main(self):
        from Main_window_Final import MainWindow
        self.Main_window = MainWindow()
        self.Main_window.show()
        self.close()

    @pyqtSlot()
    def getfiles_Authentic(self):
        fileName = QFileDialog.getExistingDirectory(self, 'Files', 'C:\'')
        self.file_path_Authentic = fileName
        self.line_edit_2.setText(fileName)

    @pyqtSlot()
    def getfiles_Tampered(self):
        fileName = QFileDialog.getExistingDirectory(self, 'Files', 'C:\'')
        self.file_path_Tampered = fileName
        self.line_edit_1.setText(fileName)

    @pyqtSlot()
    def Make_CSV_file(self):
        if self.file_path_Tampered == "" or  self.file_path_Authentic == "":
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Browse Another Authentic or Tampered Directory")
            msg.setWindowTitle("Error")
            msg.setWindowIcon(QtGui.QIcon("icons8-cbs-512.ico"))
            msg.exec_()
        else:
            forged_images_path =  self.file_path_Tampered
            Not_forged_images_path =  self.file_path_Authentic
            forged = os.listdir(forged_images_path)
            Not_forged = os.listdir(Not_forged_images_path)
            file_number =random.randint(1, 1000000)
            CSV_file_name = self.combo.currentText()+"_"+str(file_number)+".csv"
            with open(CSV_file_name, "w", encoding="utf-8", newline='') as new_file:
                csv_writer = csv.writer(new_file)
                for (i, file) in enumerate(forged):
                    csv_writer.writerow([ forged_images_path+"/" + file, 1])
                for (i, file) in enumerate(Not_forged):
                    csv_writer.writerow([Not_forged_images_path+"/" + file, 0])
            new_file.close()
            shutil.move(self.current+"\\"+CSV_file_name, self.current + self.Dataset)
            self.csv_file = self.current+ self.Dataset+"\\"+CSV_file_name
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Question)
            msg.setText("Dataset prepared click Train to train the Model")
            msg.setWindowTitle("Done")
            msg.setWindowIcon(QtGui.QIcon("icons8-cbs-512.ico"))
            msg.exec_()

    def on_click(self):
        if self.file_path_Authentic == "" or self.file_path_Tampered == "" or   self.csv_file == "":
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Broswe Authentic Directory or Tampered Directory and Create Csv File")
            msg.setWindowTitle("Error")
            msg.setWindowIcon(QtGui.QIcon("icons8-cbs-512.ico"))
            msg.exec_()
        else:
            if str(self.combo.currentText()) == "Error Level Analysis" :
                self.button_1.setEnabled(False)
                self.button_2.setEnabled(False)
                self.button_3.setEnabled(False)
                self.button_4.setEnabled(False)
                lr = float(self.lr.text())
                ep = int(self.ep.text())
                self.myThread = thread()
                plot , model = self.myThread.train_model(self.csv_file , lr , ep , "ELA")
                self.myThread.start()
                self.model = model

                pixmap = QPixmap(plot)
                self.label.setPixmap(pixmap)
                self.label.resize(320, 240)
                self.label.move(10, 110)
                self.label.setPixmap(pixmap.scaled(self.label.size(), Qt.IgnoreAspectRatio))
                self.label.show()

            elif str(self.combo.currentText()) == "VGG16":
                self.button_1.setEnabled(False)
                self.button_2.setEnabled(False)
                self.button_3.setEnabled(False)
                self.button_4.setEnabled(False)
                lr = float(self.lr.text())
                ep = int(self.ep.text())
                self.myThread = thread()
                plot , model = self.myThread.train_model(self.csv_file, lr , ep , "VGG16")
                self.myThread.start()
                self.model = model

                pixmap = QPixmap(plot)
                self.label.setPixmap(pixmap)
                self.label.resize(320, 240)
                self.label.move(10, 110)
                self.label.setPixmap(pixmap.scaled(self.label.size(), Qt.IgnoreAspectRatio))
                self.label.show()

            elif str(self.combo.currentText()) == "VGG19":
                self.button_1.setEnabled(False)
                self.button_2.setEnabled(False)
                self.button_3.setEnabled(False)
                self.button_4.setEnabled(False)
                lr = float(self.lr.text())
                ep = int(self.ep.text())
                self.myThread = thread()
                plot , model = self.myThread.train_model(self.csv_file, lr , ep , "VGG19")
                self.myThread.start()
                self.model = model

                pixmap = QPixmap(plot)
                self.label.setPixmap(pixmap)
                self.label.resize(320, 240)
                self.label.move(10, 110)
                self.label.setPixmap(pixmap.scaled(self.label.size(), Qt.IgnoreAspectRatio))
                self.label.show()

    @pyqtSlot()
    def on_click_help(self):
        self.help_window = HelpWindow()
        self.help_window .show()
        self.showMinimized()


    @pyqtSlot()
    def closex(self):
        reply = QMessageBox.question(self, "Quit", "Are you sure you want to quit?",
                                     QMessageBox.Cancel | QMessageBox.Close)
        if reply== QMessageBox.Yes:
            self.close()


    @pyqtSlot()
    def keyPressEvent(self, event):
        """Close application from escape key.

        results in QMessageBox dialog from closeEvent, good but how/why?
        """
        if event.key() == Qt.Key_Escape:
            reply = QMessageBox.question(
                self, "Message",
                "Are you sure you want to quit?",
                 QMessageBox.Close | QMessageBox.Cancel)

            if reply == QMessageBox.Close:
               self.close()

    @pyqtSlot()
    def close_main_window(self):
        """
           Generate 'question' dialog on clicking 'X' button in title bar.
           Reimplement the closeEvent() event handler to include a 'Question'
           dialog with options on how to proceed - Save, Close, Cancel buttons
        """
        reply = QMessageBox.question(self, "Quit", "Are you sure you want to quit?",
                                     QMessageBox.Cancel | QMessageBox.Close)

        if reply == QMessageBox.Close:
            self.close()




if __name__ == "__main__":
    App = QApplication(sys.argv)
    App.setStyle('Fusion')
    window = Training_window()
    sys.exit(App.exec())