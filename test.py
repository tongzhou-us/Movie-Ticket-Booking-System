import functions
import socket


clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
host = socket.gethostname() 
port = 6666
clientsocket.connect((host, port))

# if functions.Check_account(clientsocket,'Shrey','12345'):
	# print("Check_account success!")

if functions.Add_account(clientsocket, "abd", "abcde"):
	print("Added account successfully")

functions.Logout(clientsocket)
clientsocket.close()