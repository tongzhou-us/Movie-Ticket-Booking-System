import functions
import socket


clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
host = socket.gethostname() 
port = 6666
clientsocket.connect((host, port))

print(functions.Check_account(clientsocket,'Shrey','12345'))

print(functions.Add_account(clientsocket, 'alex', 'pwdalex'))

print(functions.Update_account(clientsocket, 'alex', 'fn', 'ln', 'npwd', '1@1.com', '911'))

print(functions.movie_info(clientsocket, 'The Meg'))

functions.Logout(clientsocket)
clientsocket.close()