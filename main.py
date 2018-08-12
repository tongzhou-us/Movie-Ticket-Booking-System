import sys

from PyQt5.QtWidgets import QDialog, QApplication, QMainWindow, QMessageBox
from PyQt5 import QtGui

from UI.Search_MainWindow import Ui_Search_MainWindow
from UI.Signup_Dialog import Ui_Signup_Dialog
from UI.UpdateInfo_Dialog import Ui_UpdateInfo_Dialog
from UI.Login_Dialog import Ui_Login_Dialog

class Login_Dialog(QDialog):
    def __init__(self):
        super(Login_Dialog, self).__init__()

        self.ui = Ui_Login_Dialog()
        self.ui.setupUi(self) 
        self.main() 

    def main(self):
        self.ui.Signup_PushButton.clicked.connect(self.signup)
        self.ui.Login_PushButton.clicked.connect(self.login)
        self.ui.Cancel_PushButton.clicked.connect(self.close)

    def login(self):
        username = self.ui.UserName_LineEdit.text()
        passwrd = self.ui.Pwd_LineEdit.text()
        if self.ui.Login_PushButton.clicked:
            print("username: " + username + " passwrd: " + passwrd)
            if self.account_check(username, passrd):
                self.next_window = MainWindow()
                self.next_window.show()
                self.close
                self.search_main
            else:
                QMessageBox.about("Error", "Username/Password incorrect!")

    def account_check(self, username, passwrd):
        # TODO: check DB for existing username + passwrd

        print("account_check for username: " + username + " password: " + passwrd)

    def signup(self):
        self.next_dialog = Signup_Dialog()
        self.next_dialog.show()

    def search_main(self):
        self.next_window = Search_MainWindow()
        self.next_window.show()


class Signup_Dialog(QDialog):
    def __init__(self):
        super(Signup_Dialog, self).__init__()
        self.ui = Ui_Signup_Dialog()
        self.ui.setupUi(self)
        self.main()

    def main(self):
        self.ui.Create_PushButton.clicked.connect(self.signup)

    def signup(self): 
        name = self.ui.YourName_LineEdit.text()
        email = self.ui.Email_LineEdit.text()
        passwrd = self.ui.CreatPass_LineEdit.text()
        re_passwrd = self.ui.Reenterpwd_LineEdit.text()

        if passwrd != re_passwrd:
            QMessageBox.about(self, "Error", "Passwords must match!")
        elif name and email and passwrd and re_passwrd:
                self.updateDB(name, email, passwrd)
                self.close
                self.return_login()
        else:
            QMessageBox.about(self,"Error", "All fields must be filled!")

    def updateDB(self, name, email, passwrd):
        # TODO: update DB with user info
        print("updating DB...")

    def return_login(self):
        self.return_dialog = Login_Dialog()
        self.return_dialog.show()

class Search_MainWindow(QMainWindow):
    def __init__(self):
        super(Search_MainWindow, self).__init__()
        self.ui = Ui_Search_MainWindow()
        self.ui.setupUi(self)
        self.main()

    def main(self):
        #set up new QStandardItemModel item to store data 
        self.tablemodel = QtGui.QStandardItemModel(self)
        self.tablemodel = self.tablemodel
        self.tablemodel.setHorizontalHeaderLabels(
            ["Name", "Cinema", "Data Location", "Screen", "Showtime", "Build Path"])
       
        self.ui.Search_PushButton.clicked.connect(self.searchContent)

    def searchContent(self):
        type = self.ui.NameType_comboBox.currentText()
        search_content = self.ui.Search_LineEdit.text()
        if type == 'Name':
            # TODO; search by name and return entry
        if type == 'Type':
            # TODO: searcg by type and show on TableView

        # self.displayContent()
        # self.ui.DisplayTable.setModel(self.tablemodel)
        # for i in range(5):
        #     self.ui.DisplayTable.horizontalHeader().setSectionResizeMode(
        #         i, QHeaderView.ResizeToContents)

if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = Login_Dialog()
    window.show()

    sys.exit(app.exec_())