# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\ulian\OneDrive\Рабочий стол\ВИЗУАЛКА ПИТОНА 03\калькулятор2.0.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(415, 435)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("background-color: rgb(255, 255, 255)")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.num0 = QtWidgets.QPushButton(self.centralwidget)
        self.num0.setGeometry(QtCore.QRect(0, 320, 170, 71))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.num0.setFont(font)
        self.num0.setStyleSheet("background-color: rgb(170, 255, 255)")
        self.num0.setObjectName("num0")
        self.button_result = QtWidgets.QPushButton(self.centralwidget)
        self.button_result.setGeometry(QtCore.QRect(175, 320, 165, 71))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.button_result.setFont(font)
        self.button_result.setStyleSheet("background-color: rgb(0, 170, 255)")
        self.button_result.setObjectName("button_result")
        self.num7 = QtWidgets.QPushButton(self.centralwidget)
        self.num7.setGeometry(QtCore.QRect(0, 240, 111, 71))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.num7.setFont(font)
        self.num7.setStyleSheet("background-color: rgb(170, 255, 255)")
        self.num7.setObjectName("num7")
        self.num8 = QtWidgets.QPushButton(self.centralwidget)
        self.num8.setGeometry(QtCore.QRect(115, 240, 111, 71))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.num8.setFont(font)
        self.num8.setStyleSheet("background-color: rgb(170, 255, 255)")
        self.num8.setObjectName("num8")
        self.num9 = QtWidgets.QPushButton(self.centralwidget)
        self.num9.setGeometry(QtCore.QRect(230, 240, 111, 71))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.num9.setFont(font)
        self.num9.setStyleSheet("background-color: rgb(170, 255, 255)")
        self.num9.setObjectName("num9")
        self.num5 = QtWidgets.QPushButton(self.centralwidget)
        self.num5.setGeometry(QtCore.QRect(115, 160, 111, 71))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.num5.setFont(font)
        self.num5.setStyleSheet("background-color: rgb(170, 255, 255)")
        self.num5.setObjectName("num5")
        self.num4 = QtWidgets.QPushButton(self.centralwidget)
        self.num4.setGeometry(QtCore.QRect(0, 160, 111, 71))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.num4.setFont(font)
        self.num4.setStyleSheet("background-color: rgb(170, 255, 255)")
        self.num4.setObjectName("num4")
        self.num6 = QtWidgets.QPushButton(self.centralwidget)
        self.num6.setGeometry(QtCore.QRect(230, 160, 111, 71))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.num6.setFont(font)
        self.num6.setStyleSheet("background-color: rgb(170, 255, 255)")
        self.num6.setObjectName("num6")
        self.num2 = QtWidgets.QPushButton(self.centralwidget)
        self.num2.setGeometry(QtCore.QRect(115, 80, 111, 71))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.num2.setFont(font)
        self.num2.setStyleSheet("background-color: rgb(170, 255, 255)")
        self.num2.setObjectName("num2")
        self.num1 = QtWidgets.QPushButton(self.centralwidget)
        self.num1.setGeometry(QtCore.QRect(0, 80, 111, 71))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.num1.setFont(font)
        self.num1.setStyleSheet("background-color: rgb(170, 255, 255)")
        self.num1.setObjectName("num1")
        self.num3 = QtWidgets.QPushButton(self.centralwidget)
        self.num3.setGeometry(QtCore.QRect(230, 80, 111, 71))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.num3.setFont(font)
        self.num3.setStyleSheet("background-color: rgb(170, 255, 255)")
        self.num3.setObjectName("num3")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 401, 45))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setStyleSheet("background color: rgb(239, 255, 255)")
        self.label.setObjectName("label")
        self.num3_2 = QtWidgets.QPushButton(self.centralwidget)
        self.num3_2.setGeometry(QtCore.QRect(345, 80, 71, 71))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.num3_2.setFont(font)
        self.num3_2.setStyleSheet("background-color: rgb(170, 255, 255)")
        self.num3_2.setObjectName("num3_2")
        self.num3_3 = QtWidgets.QPushButton(self.centralwidget)
        self.num3_3.setGeometry(QtCore.QRect(345, 160, 71, 71))
        font = QtGui.QFont()
        font.setPointSize(23)
        self.num3_3.setFont(font)
        self.num3_3.setStyleSheet("background-color: rgb(170, 255, 255)")
        self.num3_3.setObjectName("num3_3")
        self.num3_4 = QtWidgets.QPushButton(self.centralwidget)
        self.num3_4.setGeometry(QtCore.QRect(345, 240, 71, 71))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.num3_4.setFont(font)
        self.num3_4.setStyleSheet("background-color: rgb(170, 255, 255)")
        self.num3_4.setObjectName("num3_4")
        self.num3_5 = QtWidgets.QPushButton(self.centralwidget)
        self.num3_5.setGeometry(QtCore.QRect(345, 320, 71, 71))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.num3_5.setFont(font)
        self.num3_5.setStyleSheet("background-color: rgb(170, 255, 255)")
        self.num3_5.setObjectName("num3_5")
        self.label.raise_()
        self.num0.raise_()
        self.button_result.raise_()
        self.num7.raise_()
        self.num8.raise_()
        self.num9.raise_()
        self.num5.raise_()
        self.num4.raise_()
        self.num6.raise_()
        self.num2.raise_()
        self.num1.raise_()
        self.num3.raise_()
        self.num3_2.raise_()
        self.num3_3.raise_()
        self.num3_4.raise_()
        self.num3_5.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 415, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.num0.setText(_translate("MainWindow", "0"))
        self.button_result.setText(_translate("MainWindow", "="))
        self.num7.setText(_translate("MainWindow", "7"))
        self.num8.setText(_translate("MainWindow", "8"))
        self.num9.setText(_translate("MainWindow", "9"))
        self.num5.setText(_translate("MainWindow", "5"))
        self.num4.setText(_translate("MainWindow", "4"))
        self.num6.setText(_translate("MainWindow", "6"))
        self.num2.setText(_translate("MainWindow", "2"))
        self.num1.setText(_translate("MainWindow", "1"))
        self.num3.setText(_translate("MainWindow", "3"))
        self.label.setText(_translate("MainWindow", "0"))
        self.num3_2.setText(_translate("MainWindow", "+"))
        self.num3_3.setText(_translate("MainWindow", "-"))
        self.num3_4.setText(_translate("MainWindow", "x"))
        self.num3_5.setText(_translate("MainWindow", ":"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
