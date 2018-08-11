import sys
from PyQt5.QtWidgets import QDialog, QApplication, QMainWindow, QMessageBox

from create_account_dialog import Ui_create_account_Dialog
from Login_Dialog import Ui_Login_Dialog
from main_window import Ui_MainWindow
from seat_selection_dialog import Ui_SeatSelection_Dialog

class Create_Account_Dialog(QDialog):
    def __init__(self):
        super(Create_Account_Dialog, self).__init__()

        self.ui = Ui_create_account_Dialog()
        self.ui.setupUi(self)  
        self.main()

    def main(self):
        self.ui.buttonBox.accepted.connect(self.next_action)

    def next_action(self):
        self.next_window = MainWindow()
        self.next_window.show()

class Login_Dialog(QDialog):
    def __init__(self):
        super(Login_Dialog, self).__init__()

        self.ui = Ui_Login_Dialog()
        self.ui.setupUi(self) 
        self.main() 

    def main(self):
        self.ui.buttonBox.accepted.connect(self.next_action)

    def next_action(self):
        self.next_dialog = Create_Account_Dialog()
        self.next_dialog.show()


class SeatSelection_Dialog(QDialog):
    def __init__(self):
        super(SeatSelection_Dialog, self).__init__()

        self.ui = Ui_SeatSelection_Dialog()
        self.ui.setupUi(self)  

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)  
        self.main()

    def main(self):
        QMessageBox.about(self, "Info", "Enter movie info.")
 


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Login_Dialog()
    window.show()

    sys.exit(app.exec_())