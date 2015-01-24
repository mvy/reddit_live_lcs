# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'view/ui/live.ui'
#
# Created: Sat Jan 24 02:16:34 2015
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(479, 417)
        self.groupBox_2 = QtGui.QGroupBox(Form)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 10, 461, 401))
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
        self.blue_dragon_spin = QtGui.QSpinBox(self.groupBox_2)
        self.blue_dragon_spin.setGeometry(QtCore.QRect(260, 340, 42, 22))
        self.blue_dragon_spin.setObjectName("blue_dragon_spin")
        self.purple_dragon_spin = QtGui.QSpinBox(self.groupBox_2)
        self.purple_dragon_spin.setGeometry(QtCore.QRect(410, 340, 42, 22))
        self.purple_dragon_spin.setObjectName("purple_dragon_spin")
        self.blue_baron = QtGui.QPushButton(self.groupBox_2)
        self.blue_baron.setGeometry(QtCore.QRect(160, 370, 91, 23))
        self.blue_baron.setStyleSheet("background-color: rgb(170, 170, 255);")
        self.blue_baron.setObjectName("blue_baron")
        self.purple_baron = QtGui.QPushButton(self.groupBox_2)
        self.purple_baron.setGeometry(QtCore.QRect(310, 370, 91, 23))
        self.purple_baron.setStyleSheet("background-color: rgb(255, 170, 255)")
        self.purple_baron.setObjectName("purple_baron")
        self.clear_button = QtGui.QPushButton(self.groupBox_2)
        self.clear_button.setGeometry(QtCore.QRect(10, 370, 91, 23))
        self.clear_button.setObjectName("clear_button")
        self.blue_baron_spin = QtGui.QSpinBox(self.groupBox_2)
        self.blue_baron_spin.setGeometry(QtCore.QRect(260, 370, 42, 22))
        self.blue_baron_spin.setObjectName("blue_baron_spin")
        self.purple_baron_spin = QtGui.QSpinBox(self.groupBox_2)
        self.purple_baron_spin.setGeometry(QtCore.QRect(410, 370, 42, 22))
        self.purple_baron_spin.setObjectName("purple_baron_spin")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "Live", None, QtGui.QApplication.UnicodeUTF8))
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
        self.clear_button.setText(QtGui.QApplication.translate("Form", "Clear Clipboard", None, QtGui.QApplication.UnicodeUTF8))

