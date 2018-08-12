# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SelectPaymentMethod_Dialog.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_SelectPaymentMethod_Dialog(object):
    def setupUi(self, SelectPaymentMethod_Dialog):
        SelectPaymentMethod_Dialog.setObjectName("SelectPaymentMethod_Dialog")
        SelectPaymentMethod_Dialog.resize(511, 236)
        self.Visa_PushButton = QtWidgets.QPushButton(SelectPaymentMethod_Dialog)
        self.Visa_PushButton.setGeometry(QtCore.QRect(20, 60, 151, 81))
        self.Visa_PushButton.setStyleSheet("border-image: url(:/pay/Visa.PNG);")
        self.Visa_PushButton.setText("")
        self.Visa_PushButton.setObjectName("Visa_PushButton")
        self.Alipay_PushButton = QtWidgets.QPushButton(SelectPaymentMethod_Dialog)
        self.Alipay_PushButton.setGeometry(QtCore.QRect(180, 60, 151, 81))
        self.Alipay_PushButton.setStyleSheet("border-image: url(:/pay/Ali.PNG);")
        self.Alipay_PushButton.setText("")
        self.Alipay_PushButton.setObjectName("Alipay_PushButton")
        self.Paypal_PushButton = QtWidgets.QPushButton(SelectPaymentMethod_Dialog)
        self.Paypal_PushButton.setGeometry(QtCore.QRect(340, 60, 151, 81))
        self.Paypal_PushButton.setStyleSheet("border-image: url(:/pay/Payal.PNG);")
        self.Paypal_PushButton.setText("")
        self.Paypal_PushButton.setObjectName("Paypal_PushButton")
        self.PaymentMethod_Label = QtWidgets.QLabel(SelectPaymentMethod_Dialog)
        self.PaymentMethod_Label.setGeometry(QtCore.QRect(20, 0, 161, 61))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.PaymentMethod_Label.setFont(font)
        self.PaymentMethod_Label.setObjectName("PaymentMethod_Label")
        self.Continue_PushButton = QtWidgets.QPushButton(SelectPaymentMethod_Dialog)
        self.Continue_PushButton.setGeometry(QtCore.QRect(160, 180, 75, 23))
        self.Continue_PushButton.setObjectName("Continue_PushButton")
        self.Cancel_PushButton = QtWidgets.QPushButton(SelectPaymentMethod_Dialog)
        self.Cancel_PushButton.setGeometry(QtCore.QRect(270, 180, 75, 23))
        self.Cancel_PushButton.setObjectName("Cancel_PushButton")

        self.retranslateUi(SelectPaymentMethod_Dialog)
        QtCore.QMetaObject.connectSlotsByName(SelectPaymentMethod_Dialog)

    def retranslateUi(self, SelectPaymentMethod_Dialog):
        _translate = QtCore.QCoreApplication.translate
        SelectPaymentMethod_Dialog.setWindowTitle(_translate("SelectPaymentMethod_Dialog", "Payment Method"))
        self.PaymentMethod_Label.setText(_translate("SelectPaymentMethod_Dialog", "Select Payment Method:"))
        self.Continue_PushButton.setText(_translate("SelectPaymentMethod_Dialog", "Continue"))
        self.Cancel_PushButton.setText(_translate("SelectPaymentMethod_Dialog", "Cancel"))
