# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Login_Dialog.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Login_Dialog(object):
    def setupUi(self, Login_Dialog):
        Login_Dialog.setObjectName("Login_Dialog")
        Login_Dialog.resize(280, 150)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Login_Dialog.sizePolicy().hasHeightForWidth())
        Login_Dialog.setSizePolicy(sizePolicy)
        Login_Dialog.setMinimumSize(QtCore.QSize(280, 150))
        self.gridLayoutWidget = QtWidgets.QWidget(Login_Dialog)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(20, 20, 249, 106))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.Signup_PushButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.Signup_PushButton.setObjectName("Signup_PushButton")
        self.gridLayout.addWidget(self.Signup_PushButton, 3, 0, 1, 1)
        self.Username_Label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.Username_Label.setObjectName("Username_Label")
        self.gridLayout.addWidget(self.Username_Label, 0, 0, 1, 1)
        self.Password_Label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.Password_Label.setObjectName("Password_Label")
        self.gridLayout.addWidget(self.Password_Label, 1, 0, 1, 1)
        self.Cancel_PushButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.Cancel_PushButton.setObjectName("Cancel_PushButton")
        self.gridLayout.addWidget(self.Cancel_PushButton, 3, 2, 1, 1)
        self.Login_PushButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.Login_PushButton.setObjectName("Login_PushButton")
        self.gridLayout.addWidget(self.Login_PushButton, 3, 1, 1, 1)
        self.Pwd_LineEdit = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.Pwd_LineEdit.setObjectName("Pwd_LineEdit")
        self.gridLayout.addWidget(self.Pwd_LineEdit, 1, 1, 1, 2)
        self.UserName_LineEdit = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.UserName_LineEdit.setObjectName("UserName_LineEdit")
        self.gridLayout.addWidget(self.UserName_LineEdit, 0, 1, 1, 2)

        self.retranslateUi(Login_Dialog)
        QtCore.QMetaObject.connectSlotsByName(Login_Dialog)

    def retranslateUi(self, Login_Dialog):
        _translate = QtCore.QCoreApplication.translate
        Login_Dialog.setWindowTitle(_translate("Login_Dialog", "Login"))
        self.Signup_PushButton.setText(_translate("Login_Dialog", "Signup"))
        self.Username_Label.setText(_translate("Login_Dialog", " User Name:"))
        self.Password_Label.setText(_translate("Login_Dialog", " Password:"))
        self.Cancel_PushButton.setText(_translate("Login_Dialog", "Cancel"))
        self.Login_PushButton.setText(_translate("Login_Dialog", "Login"))

