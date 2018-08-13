# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Search_MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Search_MainWindow(object):
    def setupUi(self, Search_MainWindow):
        Search_MainWindow.setObjectName("Search_MainWindow")
        Search_MainWindow.resize(592, 372)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Search_MainWindow.sizePolicy().hasHeightForWidth())
        Search_MainWindow.setSizePolicy(sizePolicy)
        Search_MainWindow.setMaximumSize(QtCore.QSize(600, 750))
        self.centralwidget = QtWidgets.QWidget(Search_MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(20, -20, 551, 80))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.NameType_comboBox = QtWidgets.QComboBox(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.NameType_comboBox.setFont(font)
        self.NameType_comboBox.setObjectName("NameType_comboBox")
        self.NameType_comboBox.addItem("")
        self.NameType_comboBox.addItem("")
        self.gridLayout.addWidget(self.NameType_comboBox, 0, 2, 1, 1)
        self.Search_LineEdit = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.Search_LineEdit.setObjectName("Search_LineEdit")
        self.gridLayout.addWidget(self.Search_LineEdit, 0, 1, 1, 1)
        self.Search_PushButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.Search_PushButton.setFont(font)
        self.Search_PushButton.setStyleSheet("")
        self.Search_PushButton.setObjectName("Search_PushButton")
        self.gridLayout.addWidget(self.Search_PushButton, 0, 3, 1, 1)
        self.SearchDis_TableView = QtWidgets.QTableView(self.centralwidget)
        self.SearchDis_TableView.setGeometry(QtCore.QRect(20, 40, 551, 301))
        self.SearchDis_TableView.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.SearchDis_TableView.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.SearchDis_TableView.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.SearchDis_TableView.setSortingEnabled(True)
        self.SearchDis_TableView.setObjectName("SearchDis_TableView")
        self.SearchDis_TableView.horizontalHeader().setSortIndicatorShown(True)
        self.SearchDis_TableView.verticalHeader().setVisible(True)
        Search_MainWindow.setCentralWidget(self.centralwidget)
        self.menuBar = QtWidgets.QMenuBar(Search_MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 592, 22))
        self.menuBar.setDefaultUp(True)
        self.menuBar.setObjectName("menuBar")
        self.Account_Menu = QtWidgets.QMenu(self.menuBar)
        self.Account_Menu.setObjectName("Account_Menu")
        Search_MainWindow.setMenuBar(self.menuBar)
        self.UpdateInfo_Action = QtWidgets.QAction(Search_MainWindow)
        self.UpdateInfo_Action.setObjectName("UpdateInfo_Action")
        self.Account_Menu.addAction(self.UpdateInfo_Action)
        self.menuBar.addAction(self.Account_Menu.menuAction())

        self.retranslateUi(Search_MainWindow)
        QtCore.QMetaObject.connectSlotsByName(Search_MainWindow)

    def retranslateUi(self, Search_MainWindow):
        _translate = QtCore.QCoreApplication.translate
        Search_MainWindow.setWindowTitle(_translate("Search_MainWindow", "Search"))
        self.NameType_comboBox.setItemText(0, _translate("Search_MainWindow", "Name"))
        self.NameType_comboBox.setItemText(1, _translate("Search_MainWindow", "Type"))
        self.Search_PushButton.setText(_translate("Search_MainWindow", "Search"))
        self.Account_Menu.setTitle(_translate("Search_MainWindow", "Account"))
        self.UpdateInfo_Action.setText(_translate("Search_MainWindow", "UpdateInfo"))

