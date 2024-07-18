# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(794, 767)
        MainWindow.setStyleSheet("background:#333;\n"
"color:white;")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(270, 70, 211, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(40, 160, 151, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(600, 190, 161, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("background:crimson;\n"
"color:white;\n"
"border-radius:10px;\n"
"border:none;")
        self.pushButton_2.setObjectName("pushButton_2")
        self.changeDirectoryButton = QtWidgets.QPushButton(self.centralwidget)
        self.changeDirectoryButton.setGeometry(QtCore.QRect(600, 670, 161, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.changeDirectoryButton.setFont(font)
        self.changeDirectoryButton.setStyleSheet("background:crimson;\n"
"color:white;\n"
"border-radius:10px;\n"
"border:none;")
        self.changeDirectoryButton.setObjectName("changeDirectoryButton")
        self.URLInput = QtWidgets.QLineEdit(self.centralwidget)
        self.URLInput.setGeometry(QtCore.QRect(40, 190, 541, 51))
        self.URLInput.setStyleSheet("padding:5px;\n"
"border-radius:10px;\n"
"border:2px solid white;")
        self.URLInput.setObjectName("URLInput")
        self.fileSaveLocation = QtWidgets.QLineEdit(self.centralwidget)
        self.fileSaveLocation.setGeometry(QtCore.QRect(40, 670, 541, 51))
        self.fileSaveLocation.setStyleSheet("border-radius:10px;\n"
"border:2px solid white;")
        self.fileSaveLocation.setObjectName("fileSaveLocation")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(40, 640, 151, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.MessageLabel = QtWidgets.QLabel(self.centralwidget)
        self.MessageLabel.setGeometry(QtCore.QRect(80, 300, 631, 231))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.MessageLabel.setFont(font)
        self.MessageLabel.setObjectName("MessageLabel")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Data Scrapper"))
        self.label_2.setText(_translate("MainWindow", "Paste URL Here:"))
        self.pushButton_2.setText(_translate("MainWindow", "Start Scraping"))
        self.changeDirectoryButton.setText(_translate("MainWindow", "Change Directory"))
        self.label_3.setText(_translate("MainWindow", "File Location"))
        self.MessageLabel.setText(_translate("MainWindow", "Messages"))