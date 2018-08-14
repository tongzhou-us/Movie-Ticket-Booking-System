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
        self.ui.menuBar.setNativeMenuBar(False)
        self.tablemodel = QtGui.QStandardItemModel(self)
        self.tablemodel.setHorizontalHeaderLabels(
            ["Name", "Cinema", "Showtime", "Screen", "SID"])
       
        self.ui.Search_PushButton.clicked.connect(self.search_content)
        self.ui.UpdateInfo_Action.triggered.connect(self.update_info)
        self.ui.SearchDis_TableView.doubleClicked.connect(self.show_movie_info)

    def search_content(self):
        global clientsocket
        search_type = self.ui.NameType_comboBox.currentText()
        search_content = self.ui.Search_LineEdit.text()
        if search_type == 'Name':
            search_result = functions.Search_name(clientsocket, str(search_content))
        if search_type == 'Type':
            search_result = functions.Search_type(clientsocket, str(search_content))
        
        if search_result:
            print(search_result)
            for row, movie_info in enumerate(search_result):
                self.tablemodel.setItem(row, 0, QtGui.QStandardItem(movie_info['movie']))
                self.tablemodel.setItem(row, 1, QtGui.QStandardItem(movie_info['cinema']))
                self.tablemodel.setItem(row, 2, QtGui.QStandardItem(movie_info['showtime']))
                self.tablemodel.setItem(row, 3, QtGui.QStandardItem(movie_info['screen']))
                self.tablemodel.setItem(row, 4, QtGui.QStandardItem(str(movie_info['sid'])))

            self.ui.SearchDis_TableView.setModel(self.tablemodel)
            for i in range(4):
                self.ui.SearchDis_TableView.horizontalHeader().setSectionResizeMode(
                    i, QHeaderView.ResizeToContents)

        else:
            QMessageBox(self, "Error", "No movies found.")
            self.tablemodel.clear()
        
    def update_info(self):
        self.next_dialog = UpdateInfo_Dialog(self.username)
        self.next_dialog.show()

    def show_movie_info(self):
        index = self.ui.SearchDis_TableView.selectionModel().selectedRows()
        if len(index):
            self.movie_name = self.tablemodel.item(index[0].row(), 0).text()            
            self.sid = self.tablemodel.item(index[0].row(), 4).text()   
            self.movie_info_dialog()

    def movie_info_dialog(self):
        self.next_dialog = MovieInfo_Dialog(self.movie_name, self.sid)
        self.next_dialog.show()

class UpdateInfo_Dialog(QDialog):
    def __init__(self, username):
        super(UpdateInfo_Dialog, self).__init__()

        self.ui = Ui_UpdateInfo_Dialog()
        self.ui.setupUi(self) 
        self.username = username
        self.main() 

    def main(self):
        self.ui.Update_PushButton.clicked.connect(self.update_info)
        self.ui.Cancel_PushButton.clicked.connect(self.close)
    
    def update_info(self):
        global clientsocket
        first_name = self.ui.UpdatefirstName_LineEdit.text()
        last_name = self.ui.UpdateLastName_LineEdit.text()
        new_passwrd = self.ui.UpdatePwd_LineEdit.text()
        new_passwrd_confirm = self.ui.Update_ConfirmPwd_LineEdit.text()
        new_email = self.ui.UpdateEmail_LineEdit.text()
        phone = self.ui.UpdateHomePhone_LineEdit.text() 

        if new_passwrd != new_passwrd_confirm:
            QMessageBox.about(self, "Error", "Passwords must match!")

        elif functions.Update_account(clientsocket, self.username, first_name,last_name,new_passwrd, new_email, phone):
            QMessageBox.about(self, 'success', 'Updated account info success!')
            self.close()
        else:
            QMessageBox.about(self, "Error", "Unable to update. All fields must be filled.\nPlease try again.")

class MovieInfo_Dialog(QDialog):
    # call get_movie_info(movie_name) and display on QTableView
    def __init__(self, movie_name, sid):
        super(MovieInfo_Dialog, self).__init__()

        self.ui = Ui_MovieInfo_Dialog()
        self.ui.setupUi(self) 
        self.movie_name = movie_name
        self.sid = sid
        self.main() 

    def main(self):
        global clientsocket
        self.ui.Cancel_PushButton.clicked.connect(self.close)
        self.ui.Continue_PushButton.clicked.connect(self.seat_selection)

        self.tablemodel = QtGui.QStandardItemModel(self)
        self.tablemodel.setHorizontalHeaderLabels(["Name", "Type", "Description", "Actors"])

        movie_info = functions.movie_info(clientsocket, str(self.movie_name))
        if movie_info:
            for info in movie_info:
                self.tablemodel.setItem(0, 0, QtGui.QStandardItem(self.movie_name))
                self.tablemodel.setItem(0, 1, QtGui.QStandardItem(movie_info['Type']))
                self.tablemodel.setItem(0, 2, QtGui.QStandardItem(movie_info['Description']))
                self.tablemodel.setItem(0, 3, QtGui.QStandardItem(movie_info['Actors']))
        
            self.ui.MovieInfoDis_tableView.setModel(self.tablemodel)
            for i in range(4):
                self.ui.MovieInfoDis_tableView.horizontalHeader().setSectionResizeMode(
                    i, QHeaderView.ResizeToContents)

        else:
            QMessageBox(self, "Error", "No movie info provided.")
            self.tablemodel.clear()
                
    def seat_selection(self):
        self.next_dialog = SeatMap_Dialog(self.sid)
        self.next_dialog.show()

class SeatMap_Dialog(QDialog):
    def __init__(self, sid):
        super(SeatMap_Dialog, self).__init__()

        self.ui = Ui_SeatMap_Dialog()
        self.ui.setupUi(self)
        self.sid = sid
        self.main()

    def main(self):
        self.display_seats()
        self.ui.Cancel_PushButton.clicked.connect(self.close)

    def display_seats(self):
        # TODO: get seat_dict, read it into seat_list as etc: str(bin(row0))[2:]
        global clientsocket
        check_seat_dict = functions.Check_seat(clientsocket, self.sid) 
        print(check_seat_dict)
        self.seat_list = []
        self.seat_list.append(str(bin(int(check_seat_dict['r0'])))[2:])
        self.seat_list.append(str(bin(int(check_seat_dict['r1'])))[2:])
        self.seat_list.append(str(bin(int(check_seat_dict['r2'])))[2:])
        self.seat_list.append(str(bin(int(check_seat_dict['r3'])))[2:])
        self.seat_list.append(str(bin(int(check_seat_dict['r4'])))[2:])

        for row_index, row in enumerate(self.seat_list):
            row_list = [int(d) for d in row]
            column_index = []
            for index, i in enumerate(row_list):
                if i == 1:
                    column_index.append(index)

            for n in column_index:
                row_alpha = chr(row_index + 65)
                seat_disabled = str(row_alpha + str(n+1))
                if seat_disabled == 'A1':
                    self.ui.A1_PushButton.setEnabled(False)
                    self.ui.A1_PushButton.setChecked(False)
                elif seat_disabled == 'A2':
                    self.ui.A2_PushButton.setEnabled(False)
                    self.ui.A2_PushButton.setChecked(False)
                elif seat_disabled == 'A3':
                    self.ui.A3_PushButton.setEnabled(False)
                    self.ui.A3_PushButton.setChecked(False)
                elif seat_disabled == 'A4':
                    self.ui.A4_PushButton.setEnabled(False)
                    self.ui.A4_PushButton.setChecked(False)
                elif seat_disabled == 'A5':
                    self.ui.A5_PushButton.setEnabled(False)
                    self.ui.A5_PushButton.setChecked(False)
                elif seat_disabled == 'A6':
                    self.ui.A6_PushButton.setEnabled(False)
                    self.ui.A6_PushButton.setChecked(False)
                elif seat_disabled == 'B1':
                    self.ui.B1_PushButton.setEnabled(False)
                    self.ui.B1_PushButton.setChecked(False)
                elif seat_disabled == 'B2':
                    self.ui.B2_PushButton.setEnabled(False)
                    self.ui.B2_PushButton.setChecked(False)
                elif seat_disabled == 'B3':
                    self.ui.B3_PushButton.setEnabled(False)
                    self.ui.B3_PushButton.setChecked(False)
                elif seat_disabled == 'B4':
                    self.ui.B4_PushButton.setEnabled(False)
                    self.ui.B4_PushButton.setChecked(False)
                elif seat_disabled == 'B5':
                    self.ui.B5_PushButton.setEnabled(False)
                    self.ui.B5_PushButton.setChecked(False)
                elif seat_disabled == 'B6':
                    self.ui.B6_PushButton.setEnabled(False)
                    self.ui.B6_PushButton.setChecked(False)
                elif seat_disabled == 'C1':
                    self.ui.C1_PushButton.setEnabled(False)
                    self.ui.C1_PushButton.setChecked(False)
                elif seat_disabled == 'C2':
                    self.ui.C2_PushButton.setEnabled(False)
                    self.ui.C2_PushButton.setChecked(False)
                elif seat_disabled == 'C3':
                    self.ui.C3_PushButton.setEnabled(False)
                    self.ui.C3_PushButton.setChecked(False)
                elif seat_disabled == 'C4':
                    self.ui.C4_PushButton.setEnabled(False)
                    self.ui.C4_PushButton.setChecked(False)
                elif seat_disabled == 'C5':
                    self.ui.C5_PushButton.setEnabled(False)
                    self.ui.C5_PushButton.setChecked(False)
                elif seat_disabled == 'C6':
                    self.ui.C6_PushButton.setEnabled(False)
                    self.ui.C6_PushButton.setChecked(False)
                elif seat_disabled == 'D1':
                    self.ui.D1_PushButton.setEnabled(False)
                    self.ui.D1_PushButton.setChecked(False)
                elif seat_disabled == 'D2':
                    self.ui.D2_PushButton.setEnabled(False)
                    self.ui.D2_PushButton.setChecked(False)
                elif seat_disabled == 'D3':
                    self.ui.D3_PushButton.setEnabled(False)
                    self.ui.D3_PushButton.setChecked(False)
                elif seat_disabled == 'D4':
                    self.ui.D4_PushButton.setEnabled(False)
                    self.ui.D4_PushButton.setChecked(False)
                elif seat_disabled == 'D5':
                    self.ui.D5_PushButton.setEnabled(False)
                    self.ui.D5_PushButton.setChecked(False)
                elif seat_disabled == 'D6':
                    self.ui.D6_PushButton.setEnabled(False)
                    self.ui.D6_PushButton.setChecked(False)
                elif seat_disabled == 'E1':
                    self.ui.E1_PushButton.setEnabled(False)
                    self.ui.E1_PushButton.setChecked(False)
                elif seat_disabled == 'E2':
                    self.ui.E2_PushButton.setEnabled(False)
                    self.ui.E2_PushButton.setChecked(False)
                elif seat_disabled == 'E3':
                    self.ui.E3_PushButton.setEnabled(False)
                    self.ui.E3_PushButton.setChecked(False)
                elif seat_disabled == 'E4':
                    self.ui.E4_PushButton.setEnabled(False)
                    self.ui.E4_PushButton.setChecked(False)
                elif seat_disabled == 'E5':
                    self.ui.E5_PushButton.setEnabled(False)
                    self.ui.E5_PushButton.setChecked(False)
                elif seat_disabled == 'E6':
                    self.ui.E6_PushButton.setEnabled(False)
                    self.ui.E6_PushButton.setChecked(False)

        self.ui.A1_PushButton.clicked.connect(lambda:self.update_seat('A1'))
        self.ui.A2_PushButton.clicked.connect(lambda:self.update_seat('A2'))
        self.ui.A3_PushButton.clicked.connect(lambda:self.update_seat('A3'))
        self.ui.A4_PushButton.clicked.connect(lambda:self.update_seat('A4'))
        self.ui.A5_PushButton.clicked.connect(lambda:self.update_seat('A5'))
        self.ui.A6_PushButton.clicked.connect(lambda:self.update_seat('A6'))
        self.ui.B1_PushButton.clicked.connect(lambda:self.update_seat('B1'))
        self.ui.B2_PushButton.clicked.connect(lambda:self.update_seat('B2'))
        self.ui.B3_PushButton.clicked.connect(lambda:self.update_seat('B3'))
        self.ui.B4_PushButton.clicked.connect(lambda:self.update_seat('B4'))
        self.ui.B5_PushButton.clicked.connect(lambda:self.update_seat('B5'))
        self.ui.B6_PushButton.clicked.connect(lambda:self.update_seat('B6'))
        self.ui.C1_PushButton.clicked.connect(lambda:self.update_seat('C1'))
        self.ui.C2_PushButton.clicked.connect(lambda:self.update_seat('C2'))
        self.ui.C3_PushButton.clicked.connect(lambda:self.update_seat('C3'))
        self.ui.C4_PushButton.clicked.connect(lambda:self.update_seat('C4'))
        self.ui.C5_PushButton.clicked.connect(lambda:self.update_seat('C5'))
        self.ui.C6_PushButton.clicked.connect(lambda:self.update_seat('C6'))
        self.ui.D1_PushButton.clicked.connect(lambda:self.update_seat('D1'))
        self.ui.D2_PushButton.clicked.connect(lambda:self.update_seat('D2'))
        self.ui.D3_PushButton.clicked.connect(lambda:self.update_seat('D3'))
        self.ui.D4_PushButton.clicked.connect(lambda:self.update_seat('D4'))
        self.ui.D5_PushButton.clicked.connect(lambda:self.update_seat('D5'))
        self.ui.D6_PushButton.clicked.connect(lambda:self.update_seat('D6'))
        self.ui.E1_PushButton.clicked.connect(lambda:self.update_seat('E1'))
        self.ui.E2_PushButton.clicked.connect(lambda:self.update_seat('E2'))
        self.ui.E3_PushButton.clicked.connect(lambda:self.update_seat('E3'))
        self.ui.E4_PushButton.clicked.connect(lambda:self.update_seat('E4'))
        self.ui.E5_PushButton.clicked.connect(lambda:self.update_seat('E5'))
        self.ui.E6_PushButton.clicked.connect(lambda:self.update_seat('E6'))

    def update_seat(self, selected_seat):
        self.ui.Continue_PushButton.clicked.connect(lambda:self.update_seat_2(selected_seat))

    def update_seat_2(self, selected_seat):
        self.ui.selectedseat_Label.setText(selected_seat + " selected.")
        global clientsocket

        # UPDATE SEAT DO NOT WORK AS OF NOW
        # new_row = ord(list(selected_seat)[0]) - 65
        # new_column = int(list(selected_seat)[1])

        # update_column = list(self.seat_list[new_row])
        # update_column[new_column] = '1'
        # self.seat_list[new_row] = str(update_column)

        new_seat_dict = {
            'r0' : str(self.seat_list[0]),
            'r1' : str(self.seat_list[1]),
            'r2' : str(self.seat_list[2]),
            'r3' : str(self.seat_list[3]),
            'r4' : str(self.seat_list[4])
        }

        if functions.Update_seat(clientsocket, self.sid, new_seat_dict):
            QMessageBox.about(self, "success", 'Reserved seat ' + selected_seat + " success. Please complete payment in 15 minutes.")
            self.next_dialog = Payment_Dialog()
            self.next_dialog.show()
            self.close()
        else:
            QMessageBox.about(self, "error", "There was an error confirming your seat, please try again!")
            self.display_seats()

class Payment_Dialog(QDialog):
    def __init__(self):
        super(Payment_Dialog, self).__init__()

        self.ui = Ui_SelectPaymentMethod_Dialog()
        self.ui.setupUi(self)
        self.main()

    def main(self):
        self.ui.Cancel_PushButton.clicked.connect(self.close)
        self.ui.Visa_PushButton.clicked.connect(lambda:self.showMessage('Visa'))
        self.ui.Alipay_PushButton.clicked.connect(lambda:self.showMessage('Alipay'))
        self.ui.Paypal_PushButton.clicked.connect(lambda:self.showMessage('Paypal'))

    def showMessage(self, method):
        if method == 'Visa':
            QMessageBox.about(self, 'info', 'Selected Visa as Payment Method.')
        if method == 'Paypal':
            QMessageBox.about(self, 'info', 'Selected Paypal as Payment Method.')
        if method == 'Alipay':
            QMessageBox.about(self, 'info', 'Selected Alipay as Payment Method.')

        functions.Logout(clientsocket)

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
    # functions.Logout(clientsocket)
    clientsocket.close()
