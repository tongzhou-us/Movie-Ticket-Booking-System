# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MovieInfo_Dialog.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MovieInfo_Dialog(object):
    def setupUi(self, MovieInfo_Dialog):
        MovieInfo_Dialog.setObjectName("MovieInfo_Dialog")
        MovieInfo_Dialog.resize(432, 350)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MovieInfo_Dialog.sizePolicy().hasHeightForWidth())
        MovieInfo_Dialog.setSizePolicy(sizePolicy)
        MovieInfo_Dialog.setMinimumSize(QtCore.QSize(430, 350))
        self.MovieInfoDis_tableView = QtWidgets.QTableView(MovieInfo_Dialog)
        self.MovieInfoDis_tableView.setGeometry(QtCore.QRect(0, 0, 431, 301))
        self.MovieInfoDis_tableView.setObjectName("MovieInfoDis_tableView")
        self.Continue_PushButton = QtWidgets.QPushButton(MovieInfo_Dialog)
        self.Continue_PushButton.setGeometry(QtCore.QRect(120, 310, 75, 23))
        self.Continue_PushButton.setObjectName("Continue_PushButton")
        self.Cancel_PushButton = QtWidgets.QPushButton(MovieInfo_Dialog)
        self.Cancel_PushButton.setGeometry(QtCore.QRect(230, 310, 75, 23))
        self.Cancel_PushButton.setObjectName("Cancel_PushButton")

        self.retranslateUi(MovieInfo_Dialog)
        QtCore.QMetaObject.connectSlotsByName(MovieInfo_Dialog)

    def retranslateUi(self, MovieInfo_Dialog):
        _translate = QtCore.QCoreApplication.translate
        MovieInfo_Dialog.setWindowTitle(_translate("MovieInfo_Dialog", "MovieInfo"))
        self.Continue_PushButton.setText(_translate("MovieInfo_Dialog", "Continue"))
        self.Cancel_PushButton.setText(_translate("MovieInfo_Dialog", "Cancel"))

