# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MovieInfo_Dialog.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MovieInfo_Dialog(object):
    def setupUi(self, MovieInfo_Dialog):
        MovieInfo_Dialog.setObjectName("MovieInfo_Dialog")
        MovieInfo_Dialog.resize(432, 186)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MovieInfo_Dialog.sizePolicy().hasHeightForWidth())
        MovieInfo_Dialog.setSizePolicy(sizePolicy)
        self.MovieInfoDis_tableView = QtWidgets.QTableView(MovieInfo_Dialog)
        self.MovieInfoDis_tableView.setGeometry(QtCore.QRect(0, 0, 431, 131))
        self.MovieInfoDis_tableView.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.MovieInfoDis_tableView.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.MovieInfoDis_tableView.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.MovieInfoDis_tableView.setObjectName("MovieInfoDis_tableView")
        self.MovieInfoDis_tableView.verticalHeader().setVisible(False)
        self.Continue_PushButton = QtWidgets.QPushButton(MovieInfo_Dialog)
        self.Continue_PushButton.setGeometry(QtCore.QRect(80, 140, 91, 31))
        self.Continue_PushButton.setObjectName("Continue_PushButton")
        self.Cancel_PushButton = QtWidgets.QPushButton(MovieInfo_Dialog)
        self.Cancel_PushButton.setGeometry(QtCore.QRect(250, 140, 91, 31))
        self.Cancel_PushButton.setAutoDefault(False)
        self.Cancel_PushButton.setObjectName("Cancel_PushButton")

        self.retranslateUi(MovieInfo_Dialog)
        QtCore.QMetaObject.connectSlotsByName(MovieInfo_Dialog)

    def retranslateUi(self, MovieInfo_Dialog):
        _translate = QtCore.QCoreApplication.translate
        MovieInfo_Dialog.setWindowTitle(_translate("MovieInfo_Dialog", "MovieInfo"))
        self.Continue_PushButton.setText(_translate("MovieInfo_Dialog", "Continue"))
        self.Cancel_PushButton.setText(_translate("MovieInfo_Dialog", "Cancel"))

