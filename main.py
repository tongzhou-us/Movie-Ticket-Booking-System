import functions
import sys
import socket 

from PyQt5.QtWidgets import QDialog, QApplication, QMainWindow, QMessageBox, QHeaderView
from PyQt5 import QtGui

from UI.Search_MainWindow import Ui_Search_MainWindow
from UI.Signup_Dialog import Ui_Signup_Dialog
from UI.UpdateInfo_Dialog import Ui_UpdateInfo_Dialog
from UI.Login_Dialog import Ui_Login_Dialog
from UI.MovieInfo_Dialog import Ui_MovieInfo_Dialog
from UI.SeatMap_Dialog import Ui_SeatMap_Dialog
from UI.ReservationInfo_Dialog import Ui_ReservationInfo_Dialog
from UI.SelectPaymentMethod_Dialog import Ui_SelectPaymentMethod_Dialog

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
        self.username = self.ui.UserName_LineEdit.text()
        self.passwrd = self.ui.Pwd_LineEdit.text()
        self.ui.Login_PushButton.clicked.connect(lambda: self.account_check(self.username, self.passwrd))

    def account_check(self, username, passwrd):
        global clientsocket
        account_check_output = functions.Check_account(clientsocket, str(username), str(passwrd))

        if account_check_output:
            self.next_window = Search_MainWindow(self.username)
            self.next_window.show()
            self.close()
        else:
            QMessageBox.about(self,"Error", "Username/Password incorrect!")
            
    def signup(self):
        self.next_dialog = Signup_Dialog()
        self.next_dialog.show()

class Signup_Dialog(QDialog):
    def __init__(self):
        super(Signup_Dialog, self).__init__()
        self.ui = Ui_Signup_Dialog()
        self.ui.setupUi(self)
        self.main()

    def main(self):
        self.ui.Create_PushButton.clicked.connect(self.signup)

    def signup(self): 
        global clientsocket
        self.username = self.ui.YourName_LineEdit.text()
        self.passwrd = self.ui.CreatPass_LineEdit.text()
        re_passwrd = self.ui.Reenterpwd_LineEdit.text()

        if self.passwrd != re_passwrd:
            QMessageBox.about(self, "Error", "Passwords must match!")
        elif self.username and self.passwrd and re_passwrd:
            if functions.Add_account(clientsocket, str(self.username), str(self.passwrd)):
                QMessageBox.about(self, "Success", "Account created successfully! Please login to continue.")
                self.close()
            else:
                QMessageBox.about(self,"Error", "Something went wrong when creating account. Please try again.")
        else:
            QMessageBox.about(self,"Error", "Username and passwords must be filled!")
    
    def return_login(self):
        self.return_dialog = Login_Dialog()
        self.return_dialog.show()

class Search_MainWindow(QMainWindow):
    def __init__(self, username):
        super(Search_MainWindow, self).__init__()
        self.ui = Ui_Search_MainWindow()
        self.ui.setupUi(self)
        self.username = username
        
        self.main()

    def main(self):
        self.tablemodel = QtGui.QStandardItemModel(self)
        self.tablemodel.setHorizontalHeaderLabels(
            ["Name", "Cinema", "Showtime", "Screen"])
       
        self.ui.Search_PushButton.clicked.connect(self.search_content)
        self.ui.UpdateInfo_Action.triggered.connect(self.update_info)
        self.ui.SearchDis_TableView.doubleClicked.connect(self.show_movie_info)

    def search_content(self):
        global clientsocket
        search_type = self.ui.NameType_comboBox.currentText()
        search_content = self.ui.Search_LineEdit.text()
        if search_type == 'Name':
            search_result = functions.Search_name(clientsocket, str(search_content))
            print(search_result)
        if search_type == 'Type':
            search_result = functions.Search_type(clientsocket, str(search_content))
            print(search_result)
        if search_result:
            for row, movie_info in enumerate(search_result):
                self.tablemodel.setItem(row, 0, QtGui.QStandardItem(movie_info['movie']))
                self.tablemodel.setItem(row, 1, QtGui.QStandardItem(movie_info['cinema']))
                self.tablemodel.setItem(row, 2, QtGui.QStandardItem(movie_info['showtime']))
                self.tablemodel.setItem(row, 3, QtGui.QStandardItem(movie_info['screen']))

                # self.tablemodel.item(ro, k).setTextAlignment(QtCore.Qt.AlignCenter)
        
            self.ui.SearchDis_TableView.setModel(self.tablemodel)
            for i in range(4):
                self.ui.SearchDis_TableView.horizontalHeader().setSectionResizeMode(
                    i, QHeaderView.ResizeToContents)

        else:
            QMessageBox(self, "Error", "No movies found.")
        
        functions.Logout(clientsocket)

    def update_info(self):
        self.next_dialog = UpdateInfo_Dialog(self.username)
        self.next_dialog.show()

    def show_movie_info(self):
        index = self.ui.SearchDis_TableView.selectionModel().selectedRows()
        if len(index):
            movie_name = self.tablemodel.item(index[0].row(), 0).text()            
            self.movie_info_dialog(movie_name)

    def movie_info_dialog(self, movie_name):
        print("show movie info dialog")
        # self.next_dialog = MovieInfo_Dialog(movie_name)
        # self.next_dialog.show()

class UpdateInfo_Dialog(QDialog):
    def __init__(self, username):
        super(UpdateInfo_Dialog, self).__init__()

        self.ui = Ui_UpdateInfo_Dialog()
        self.ui.setupUi(self) 
        self.username = username
        self.main() 

    def main(self):
        self.ui.Update_PushButton.clicked.connect(self.update_info)
    
    def update_info(self):
        old_username = self.username
        new_username = self.ui.UpdateUserName_LineEdit.text()
        first_name = self.ui.UpdatefirstName_LineEdit.text()
        last_name = self.ui.UpdateLastName_LineEdit.text()
        new_passwrd = self.ui.UpdatePwd_LineEdit.text()
        new_email = self.ui.UpdateEmail_LineEdit.text()
        phone = self.ui.UpdateHomePhone_LineEdit.text() 

        # TODO: update account info
        if update_account_info(old_username, new_username, first_name,last_name,new_passwrd, new_email, phone):
            QMessageBox(self, 'success', 'Updated account info success!')

# class MovieInfo_Dialog(QDialog, movie_name):
#     def __init__(self):
#         super(MovieInfo_Dialog, self).__init__()

#         self.ui = Ui_MovieInfo_Dialog()
#         self.ui.setupUi(self) 
#         self.movie_name = movie_name
#         self.main() 

#     def main(self):
#     # call get_movie_info(movie_name) and display on QTableView
#         self.Cancel_PushButton.clicked.connect(self.close)
#         self.Continue_PushButton.clicked.connect(self.seat_selection)

#         self.tablemodel = QtGui.QStandardItemModel(self)
#         self.tablemodel.setHorizontalHeaderLabels(["Name", "Type", "Description", "Actors"])

#         # # TODO: take the output of get_movie_info and put into list

#         #     for k in range(6):
#         #         self.tablemodel.setItem(n, k, QtGui.QStandardItem(row[k]))
#         #         self.tablemodel.item(n, k).setTextAlignment(QtCore.Qt.AlignCenter)
 
#         self.ui.MovieInfoDis_tableView.setModel(self.tablemodel)
       
#     def seat_selection(self):
#         self.next_dialog = SeatMap_Dialog()
#         self.next_dialog.show()

# class SeatMap_Dialog(QDialog):
#     def __init__(self):
#         super(SeatMap_Dialog, self).__init__()

#         self.ui = Ui_SeatMap_Dialog()
#         self.ui.setupUi(self)
#         self.main()

#     def main(self):
#         self.display_seats()

#     def display_seats(self):
#         # TODO: get seat_dict, read it into seat_list as etc: str(bin(row0))[2:]
#         seat_disable_dict = {'A1': self.ui.A1_PushButton.setDisable(False),
#                      'A2': self.ui.A2_PushButton.setDisable(False),
#                      'A3': self.ui.A3_PushButton.setDisable(False),
#                      'A4': self.ui.A4_PushButton.setDisable(False),
#                      'A5': self.ui.A5_PushButton.setDisable(False),
#                      'A6': self.ui.A6_PushButton.setDisable(False),
#                      'B1': self.ui.B1_PushButton.setDisable(False),
#                      'B2': self.ui.B2_PushButton.setDisable(False),
#                      'B3': self.ui.B3_PushButton.setDisable(False),
#                      'B4': self.ui.B4_PushButton.setDisable(False),
#                      'B5': self.ui.B5_PushButton.setDisable(False),
#                      'B6': self.ui.B6_PushButton.setDisable(False),
#                      'C1': self.ui.C1_PushButton.setDisable(False),
#                      'C2': self.ui.C2_PushButton.setDisable(False),
#                      'C3': self.ui.C3_PushButton.setDisable(False),
#                      'C4': self.ui.C4_PushButton.setDisable(False),
#                      'C5': self.ui.C5_PushButton.setDisable(False),
#                      'C6': self.ui.C6_PushButton.setDisable(False),
#                      'D1': self.ui.D1_PushButton.setDisable(False),
#                      'D2': self.ui.D2_PushButton.setDisable(False),
#                      'D3': self.ui.D3_PushButton.setDisable(False),
#                      'D4': self.ui.D4_PushButton.setDisable(False),
#                      'D5': self.ui.D5_PushButton.setDisable(False),
#                      'D6': self.ui.D6_PushButton.setDisable(False),
#                      'E1': self.ui.E1_PushButton.setDisable(False),
#                      'E2': self.ui.E2_PushButton.setDisable(False),
#                      'E3': self.ui.E3_PushButton.setDisable(False),
#                      'E4': self.ui.E4_PushButton.setDisable(False),
#                      'E5': self.ui.E5_PushButton.setDisable(False),
#                      'E6': self.ui.E6_PushButton.setDisable(False),
#             }

#         for row_index, row in enumerate(seat_list):
#             row_list = row.split()
#             colum_index = [i for i, x in enumerate(row_list) if x == 1]

#             row_alpha = chr(row_index + 65)

#             for i in colum_index:
#                 seat_disable_dict[str(row_alpha + str(i+1))]

if __name__ == '__main__':   
    # Setting up socket infomation
    global clientsocket
    clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    host = socket.gethostname() 
    port = 6666
    clientsocket.connect((host, port))
    
    app = QApplication(sys.argv)

    window = Login_Dialog()
    window.show()

    sys.exit(app.exec_())
    functions.Logout(clientsocket)
    clientsocket.close()
