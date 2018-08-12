# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Signup_Dialog.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Signup_Dialog(object):
    def setupUi(self, Signup_Dialog):
        Signup_Dialog.setObjectName("Signup_Dialog")
        Signup_Dialog.resize(230, 320)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Signup_Dialog.sizePolicy().hasHeightForWidth())
        Signup_Dialog.setSizePolicy(sizePolicy)
        Signup_Dialog.setMaximumSize(QtCore.QSize(230, 320))
        self.CreatName_Label = QtWidgets.QLabel(Signup_Dialog)
        self.CreatName_Label.setGeometry(QtCore.QRect(32, 62, 91, 16))
        self.CreatName_Label.setObjectName("CreatName_Label")
        self.YourName_LineEdit = QtWidgets.QLineEdit(Signup_Dialog)
        self.YourName_LineEdit.setGeometry(QtCore.QRect(32, 81, 171, 20))
        self.YourName_LineEdit.setObjectName("YourName_LineEdit")
        self.CreateAccount_Label = QtWidgets.QLabel(Signup_Dialog)
        self.CreateAccount_Label.setGeometry(QtCore.QRect(30, 30, 121, 20))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.CreateAccount_Label.sizePolicy().hasHeightForWidth())
        self.CreateAccount_Label.setSizePolicy(sizePolicy)
        self.CreateAccount_Label.setMaximumSize(QtCore.QSize(230, 320))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.CreateAccount_Label.setFont(font)
        self.CreateAccount_Label.setStyleSheet("\n"
"\n"
"\n"
"font: 12pt \"MS Shell Dlg 2\";")
        self.CreateAccount_Label.setObjectName("CreateAccount_Label")
        self.CreatEmail_Label = QtWidgets.QLabel(Signup_Dialog)
        self.CreatEmail_Label.setGeometry(QtCore.QRect(32, 107, 51, 16))
        self.CreatEmail_Label.setObjectName("CreatEmail_Label")
        self.Email_LineEdit = QtWidgets.QLineEdit(Signup_Dialog)
        self.Email_LineEdit.setGeometry(QtCore.QRect(32, 126, 171, 20))
        self.Email_LineEdit.setObjectName("Email_LineEdit")
        self.Creatpwd_Label = QtWidgets.QLabel(Signup_Dialog)
        self.Creatpwd_Label.setGeometry(QtCore.QRect(32, 152, 81, 16))
        self.Creatpwd_Label.setObjectName("Creatpwd_Label")
        self.CreatPass_LineEdit = QtWidgets.QLineEdit(Signup_Dialog)
        self.CreatPass_LineEdit.setGeometry(QtCore.QRect(32, 171, 171, 20))
        self.CreatPass_LineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.CreatPass_LineEdit.setObjectName("CreatPass_LineEdit")
        self.Reenterpwd_Label = QtWidgets.QLabel(Signup_Dialog)
        self.Reenterpwd_Label.setGeometry(QtCore.QRect(32, 197, 121, 16))
        self.Reenterpwd_Label.setObjectName("Reenterpwd_Label")
        self.Reenterpwd_LineEdit = QtWidgets.QLineEdit(Signup_Dialog)
        self.Reenterpwd_LineEdit.setGeometry(QtCore.QRect(32, 216, 171, 20))
        self.Reenterpwd_LineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.Reenterpwd_LineEdit.setObjectName("Reenterpwd_LineEdit")
        self.Create_PushButton = QtWidgets.QPushButton(Signup_Dialog)
        self.Create_PushButton.setGeometry(QtCore.QRect(30, 252, 171, 31))
        self.Create_PushButton.setObjectName("Create_PushButton")

        self.retranslateUi(Signup_Dialog)
        QtCore.QMetaObject.connectSlotsByName(Signup_Dialog)

    def retranslateUi(self, Signup_Dialog):
        _translate = QtCore.QCoreApplication.translate
        Signup_Dialog.setWindowTitle(_translate("Signup_Dialog", "Sign Up"))
        self.CreatName_Label.setText(_translate("Signup_Dialog", "Full Name"))
        self.CreateAccount_Label.setToolTip(_translate("Signup_Dialog", "<html><head/><body><p><span style=\" font-size:12pt;\">Account Information</span></p></body></html>"))
        self.CreateAccount_Label.setWhatsThis(_translate("Signup_Dialog", "<html><head/><body><p><span style=\" font-size:12pt;\">Account Information</span></p></body></html>"))
        self.CreateAccount_Label.setText(_translate("Signup_Dialog", "Create Account"))
        self.CreatEmail_Label.setText(_translate("Signup_Dialog", "Email"))
        self.Creatpwd_Label.setText(_translate("Signup_Dialog", "Password"))
        self.Reenterpwd_Label.setText(_translate("Signup_Dialog", "Re-enter password"))
        self.Create_PushButton.setText(_translate("Signup_Dialog", "Create Your Account"))

