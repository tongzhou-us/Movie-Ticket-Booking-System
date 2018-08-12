# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ReservationInfo_Dialog.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ReservationInfo_Dialog(object):
    def setupUi(self, ReservationInfo_Dialog):
        ReservationInfo_Dialog.setObjectName("ReservationInfo_Dialog")
        ReservationInfo_Dialog.resize(445, 267)
        self.gridLayoutWidget = QtWidgets.QWidget(ReservationInfo_Dialog)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 10, 421, 241))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.Reservation_Label = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Reservation_Label.setFont(font)
        self.Reservation_Label.setAlignment(QtCore.Qt.AlignCenter)
        self.Reservation_Label.setObjectName("Reservation_Label")
        self.gridLayout.addWidget(self.Reservation_Label, 0, 0, 1, 1)
        self.Continue_PushButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.Continue_PushButton.setObjectName("Continue_PushButton")
        self.gridLayout.addWidget(self.Continue_PushButton, 2, 0, 1, 1)
        self.ReservationInfo_tableView = QtWidgets.QTableView(self.gridLayoutWidget)
        self.ReservationInfo_tableView.setObjectName("ReservationInfo_tableView")
        self.gridLayout.addWidget(self.ReservationInfo_tableView, 1, 0, 1, 1)

        self.retranslateUi(ReservationInfo_Dialog)
        QtCore.QMetaObject.connectSlotsByName(ReservationInfo_Dialog)

    def retranslateUi(self, ReservationInfo_Dialog):
        _translate = QtCore.QCoreApplication.translate
        ReservationInfo_Dialog.setWindowTitle(_translate("ReservationInfo_Dialog", "Reservation Information"))
        self.Reservation_Label.setText(_translate("ReservationInfo_Dialog", "Reservation Infomation"))
        self.Continue_PushButton.setText(_translate("ReservationInfo_Dialog", "Continue"))

