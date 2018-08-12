# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UpdateInfo_Dialog.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_UpdateInfo_Dialog(object):
    def setupUi(self, UpdateInfo_Dialog):
        UpdateInfo_Dialog.setObjectName("UpdateInfo_Dialog")
        UpdateInfo_Dialog.resize(454, 346)
        self.UpdateInfo_Label = QtWidgets.QLabel(UpdateInfo_Dialog)
        self.UpdateInfo_Label.setGeometry(QtCore.QRect(130, 20, 221, 16))
        self.UpdateInfo_Label.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";")
        self.UpdateInfo_Label.setObjectName("UpdateInfo_Label")
        self.gridLayoutWidget = QtWidgets.QWidget(UpdateInfo_Dialog)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(40, 50, 361, 221))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.UpdateFirstName_Label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.UpdateFirstName_Label.setObjectName("UpdateFirstName_Label")
        self.gridLayout.addWidget(self.UpdateFirstName_Label, 1, 0, 1, 1)
        self.UpdateUserName_Label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.UpdateUserName_Label.setObjectName("UpdateUserName_Label")
        self.gridLayout.addWidget(self.UpdateUserName_Label, 0, 0, 1, 1)
        self.UpdateEmail_Label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.UpdateEmail_Label.setObjectName("UpdateEmail_Label")
        self.gridLayout.addWidget(self.UpdateEmail_Label, 4, 0, 1, 1)
        self.UpdatePwd_Label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.UpdatePwd_Label.setObjectName("UpdatePwd_Label")
        self.gridLayout.addWidget(self.UpdatePwd_Label, 3, 0, 1, 1)
        self.UpdateHomePhone_Label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.UpdateHomePhone_Label.setObjectName("UpdateHomePhone_Label")
        self.gridLayout.addWidget(self.UpdateHomePhone_Label, 5, 0, 1, 1)
        self.UpdateUserName_LineEdit = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.UpdateUserName_LineEdit.setObjectName("UpdateUserName_LineEdit")
        self.gridLayout.addWidget(self.UpdateUserName_LineEdit, 0, 1, 1, 1)
        self.UpdatefirstName_LineEdit = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.UpdatefirstName_LineEdit.setObjectName("UpdatefirstName_LineEdit")
        self.gridLayout.addWidget(self.UpdatefirstName_LineEdit, 1, 1, 1, 1)
        self.UpdateLastName_LineEdit_2 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.UpdateLastName_LineEdit_2.setObjectName("UpdateLastName_LineEdit_2")
        self.gridLayout.addWidget(self.UpdateLastName_LineEdit_2, 2, 1, 1, 1)
        self.UpdatePwd_LineEdit = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.UpdatePwd_LineEdit.setObjectName("UpdatePwd_LineEdit")
        self.gridLayout.addWidget(self.UpdatePwd_LineEdit, 3, 1, 1, 1)
        self.UpdateEmail_LineEdit = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.UpdateEmail_LineEdit.setObjectName("UpdateEmail_LineEdit")
        self.gridLayout.addWidget(self.UpdateEmail_LineEdit, 4, 1, 1, 1)
        self.UpdateHomePhone_LineEdit = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.UpdateHomePhone_LineEdit.setObjectName("UpdateHomePhone_LineEdit")
        self.gridLayout.addWidget(self.UpdateHomePhone_LineEdit, 5, 1, 1, 1)
        self.UpdateLastName_Label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.UpdateLastName_Label.setObjectName("UpdateLastName_Label")
        self.gridLayout.addWidget(self.UpdateLastName_Label, 2, 0, 1, 1)
        self.Update_PushButton = QtWidgets.QPushButton(UpdateInfo_Dialog)
        self.Update_PushButton.setGeometry(QtCore.QRect(130, 290, 75, 23))
        self.Update_PushButton.setObjectName("Update_PushButton")
        self.Cancel_PushButton = QtWidgets.QPushButton(UpdateInfo_Dialog)
        self.Cancel_PushButton.setGeometry(QtCore.QRect(270, 290, 75, 23))
        self.Cancel_PushButton.setObjectName("Cancel_PushButton")

        self.retranslateUi(UpdateInfo_Dialog)
        QtCore.QMetaObject.connectSlotsByName(UpdateInfo_Dialog)

    def retranslateUi(self, UpdateInfo_Dialog):
        _translate = QtCore.QCoreApplication.translate
        UpdateInfo_Dialog.setWindowTitle(_translate("UpdateInfo_Dialog", "UpdateInfo"))
        self.UpdateInfo_Label.setText(_translate("UpdateInfo_Dialog", "Update Personal Infomation"))
        self.UpdateFirstName_Label.setText(_translate("UpdateInfo_Dialog", "First Name："))
        self.UpdateUserName_Label.setText(_translate("UpdateInfo_Dialog", "User Name:"))
        self.UpdateEmail_Label.setText(_translate("UpdateInfo_Dialog", "Email:"))
        self.UpdatePwd_Label.setText(_translate("UpdateInfo_Dialog", "Password:"))
        self.UpdateHomePhone_Label.setText(_translate("UpdateInfo_Dialog", "Home Phone:"))
        self.UpdateLastName_Label.setText(_translate("UpdateInfo_Dialog", "Last Name:"))
        self.Update_PushButton.setText(_translate("UpdateInfo_Dialog", "Update"))
        self.Cancel_PushButton.setText(_translate("UpdateInfo_Dialog", "Cancel"))

