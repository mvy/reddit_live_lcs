# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'view/ui/live.ui'
#
# Created: Fri Jan 23 16:20:07 2015
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(825, 635)
        self.groupBox = QtGui.QGroupBox(Form)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 801, 511))
        self.groupBox.setObjectName("groupBox")
        self.groupBox_2 = QtGui.QGroupBox(self.groupBox)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 20, 461, 401))
        self.groupBox_2.setObjectName("groupBox_2")
        self.blue_top = QtGui.QPushButton(self.groupBox_2)
        self.blue_top.setGeometry(QtCore.QRect(160, 20, 91, 51))
        self.blue_top.setStyleSheet("background-color: rgb(170, 170, 255);")
        self.blue_top.setCheckable(True)
        self.blue_top.setFlat(False)
        self.blue_top.setObjectName("blue_top")
        self.blue_mid = QtGui.QPushButton(self.groupBox_2)
        self.blue_mid.setGeometry(QtCore.QRect(160, 140, 91, 51))
        self.blue_mid.setStyleSheet("background-color: rgb(170, 170, 255);")
        self.blue_mid.setCheckable(True)
        self.blue_mid.setObjectName("blue_mid")
        self.blue_jungle = QtGui.QPushButton(self.groupBox_2)
        self.blue_jungle.setGeometry(QtCore.QRect(160, 80, 91, 51))
        self.blue_jungle.setStyleSheet("background-color: rgb(170, 170, 255);")
        self.blue_jungle.setCheckable(True)
        self.blue_jungle.setObjectName("blue_jungle")
        self.blue_adc = QtGui.QPushButton(self.groupBox_2)
        self.blue_adc.setGeometry(QtCore.QRect(160, 200, 91, 51))
        self.blue_adc.setStyleSheet("background-color: rgb(170, 170, 255);")
        self.blue_adc.setCheckable(True)
        self.blue_adc.setObjectName("blue_adc")
        self.blue_support = QtGui.QPushButton(self.groupBox_2)
        self.blue_support.setGeometry(QtCore.QRect(160, 260, 91, 51))
        self.blue_support.setStyleSheet("background-color: rgb(170, 170, 255);")
        self.blue_support.setCheckable(True)
        self.blue_support.setObjectName("blue_support")
        self.purple_jungle = QtGui.QPushButton(self.groupBox_2)
        self.purple_jungle.setGeometry(QtCore.QRect(310, 80, 91, 51))
        self.purple_jungle.setStyleSheet("background-color: rgb(255, 170, 255)")
        self.purple_jungle.setCheckable(True)
        self.purple_jungle.setObjectName("purple_jungle")
        self.purple_support = QtGui.QPushButton(self.groupBox_2)
        self.purple_support.setGeometry(QtCore.QRect(310, 260, 91, 51))
        self.purple_support.setStyleSheet("background-color: rgb(255, 170, 255)")
        self.purple_support.setCheckable(True)
        self.purple_support.setObjectName("purple_support")
        self.purple_mid = QtGui.QPushButton(self.groupBox_2)
        self.purple_mid.setGeometry(QtCore.QRect(310, 140, 91, 51))
        self.purple_mid.setStyleSheet("background-color: rgb(255, 170, 255)")
        self.purple_mid.setCheckable(True)
        self.purple_mid.setObjectName("purple_mid")
        self.purple_adc = QtGui.QPushButton(self.groupBox_2)
        self.purple_adc.setGeometry(QtCore.QRect(310, 200, 91, 51))
        self.purple_adc.setStyleSheet("background-color: rgb(255, 170, 255)")
        self.purple_adc.setCheckable(True)
        self.purple_adc.setObjectName("purple_adc")
        self.purple_top = QtGui.QPushButton(self.groupBox_2)
        self.purple_top.setGeometry(QtCore.QRect(310, 20, 91, 51))
        self.purple_top.setStyleSheet("background-color: rgb(255, 170, 255)")
        self.purple_top.setCheckable(True)
        self.purple_top.setFlat(False)
        self.purple_top.setObjectName("purple_top")
        self.action_none_button = QtGui.QPushButton(self.groupBox_2)
        self.action_none_button.setGeometry(QtCore.QRect(10, 20, 91, 51))
        self.action_none_button.setStyleSheet("background-color: rgb(209, 209, 209);")
        self.action_none_button.setCheckable(True)
        self.action_none_button.setChecked(True)
        self.action_none_button.setObjectName("action_none_button")
        self.action_kill_button = QtGui.QPushButton(self.groupBox_2)
        self.action_kill_button.setGeometry(QtCore.QRect(10, 80, 91, 51))
        self.action_kill_button.setStyleSheet("background-color: rgb(209, 209, 209);")
        self.action_kill_button.setCheckable(True)
        self.action_kill_button.setObjectName("action_kill_button")
        self.blue_dragon = QtGui.QPushButton(self.groupBox_2)
        self.blue_dragon.setGeometry(QtCore.QRect(160, 340, 91, 23))
        self.blue_dragon.setStyleSheet("background-color: rgb(170, 170, 255);")
        self.blue_dragon.setObjectName("blue_dragon")
        self.purple_dragon = QtGui.QPushButton(self.groupBox_2)
        self.purple_dragon.setGeometry(QtCore.QRect(310, 340, 91, 23))
        self.purple_dragon.setStyleSheet("background-color: rgb(255, 170, 255)")
        self.purple_dragon.setObjectName("purple_dragon")
        self.spinBox = QtGui.QSpinBox(self.groupBox_2)
        self.spinBox.setGeometry(QtCore.QRect(260, 340, 42, 22))
        self.spinBox.setObjectName("spinBox")
        self.spinBox_2 = QtGui.QSpinBox(self.groupBox_2)
        self.spinBox_2.setGeometry(QtCore.QRect(410, 340, 42, 22))
        self.spinBox_2.setObjectName("spinBox_2")
        self.blue_baron = QtGui.QPushButton(self.groupBox_2)
        self.blue_baron.setGeometry(QtCore.QRect(160, 370, 91, 23))
        self.blue_baron.setStyleSheet("background-color: rgb(170, 170, 255);")
        self.blue_baron.setObjectName("blue_baron")
        self.purple_baron = QtGui.QPushButton(self.groupBox_2)
        self.purple_baron.setGeometry(QtCore.QRect(310, 370, 91, 23))
        self.purple_baron.setStyleSheet("background-color: rgb(255, 170, 255)")
        self.purple_baron.setObjectName("purple_baron")
        self.label = QtGui.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(20, 420, 321, 61))
        self.label.setObjectName("label")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        Form.setTabOrder(self.action_none_button, self.action_kill_button)
        Form.setTabOrder(self.action_kill_button, self.blue_top)
        Form.setTabOrder(self.blue_top, self.blue_jungle)
        Form.setTabOrder(self.blue_jungle, self.blue_mid)
        Form.setTabOrder(self.blue_mid, self.blue_adc)
        Form.setTabOrder(self.blue_adc, self.blue_support)
        Form.setTabOrder(self.blue_support, self.blue_dragon)
        Form.setTabOrder(self.blue_dragon, self.blue_baron)
        Form.setTabOrder(self.blue_baron, self.purple_top)
        Form.setTabOrder(self.purple_top, self.purple_jungle)
        Form.setTabOrder(self.purple_jungle, self.purple_mid)
        Form.setTabOrder(self.purple_mid, self.purple_adc)
        Form.setTabOrder(self.purple_adc, self.purple_support)
        Form.setTabOrder(self.purple_support, self.purple_dragon)
        Form.setTabOrder(self.purple_dragon, self.purple_baron)
        Form.setTabOrder(self.purple_baron, self.spinBox)
        Form.setTabOrder(self.spinBox, self.spinBox_2)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "Live", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("Form", "Single copy", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_2.setTitle(QtGui.QApplication.translate("Form", "Players", None, QtGui.QApplication.UnicodeUTF8))
        self.blue_top.setText(QtGui.QApplication.translate("Form", "Top\n"
"Champion\n"
"Name", None, QtGui.QApplication.UnicodeUTF8))
        self.blue_mid.setText(QtGui.QApplication.translate("Form", "Mid\n"
"Champion\n"
"Name", None, QtGui.QApplication.UnicodeUTF8))
        self.blue_jungle.setText(QtGui.QApplication.translate("Form", "Jungle\n"
"Champion\n"
"Name", None, QtGui.QApplication.UnicodeUTF8))
        self.blue_adc.setText(QtGui.QApplication.translate("Form", "ADC\n"
"Champion\n"
"Name", None, QtGui.QApplication.UnicodeUTF8))
        self.blue_support.setText(QtGui.QApplication.translate("Form", "Support\n"
"Champion\n"
"Name", None, QtGui.QApplication.UnicodeUTF8))
        self.purple_jungle.setText(QtGui.QApplication.translate("Form", "Jungle\n"
"Champion\n"
"Name", None, QtGui.QApplication.UnicodeUTF8))
        self.purple_support.setText(QtGui.QApplication.translate("Form", "Support\n"
"Champion\n"
"Name", None, QtGui.QApplication.UnicodeUTF8))
        self.purple_mid.setText(QtGui.QApplication.translate("Form", "Mid\n"
"Champion\n"
"Name", None, QtGui.QApplication.UnicodeUTF8))
        self.purple_adc.setText(QtGui.QApplication.translate("Form", "ADC\n"
"Champion\n"
"Name", None, QtGui.QApplication.UnicodeUTF8))
        self.purple_top.setText(QtGui.QApplication.translate("Form", "Top\n"
"Champion\n"
"Name", None, QtGui.QApplication.UnicodeUTF8))
        self.action_none_button.setText(QtGui.QApplication.translate("Form", "None", None, QtGui.QApplication.UnicodeUTF8))
        self.action_kill_button.setText(QtGui.QApplication.translate("Form", "Kill", None, QtGui.QApplication.UnicodeUTF8))
        self.blue_dragon.setText(QtGui.QApplication.translate("Form", "Dragon", None, QtGui.QApplication.UnicodeUTF8))
        self.purple_dragon.setText(QtGui.QApplication.translate("Form", "Dragon", None, QtGui.QApplication.UnicodeUTF8))
        self.blue_baron.setText(QtGui.QApplication.translate("Form", "Baron", None, QtGui.QApplication.UnicodeUTF8))
        self.purple_baron.setText(QtGui.QApplication.translate("Form", "Baron", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Form", "Current Output", None, QtGui.QApplication.UnicodeUTF8))

