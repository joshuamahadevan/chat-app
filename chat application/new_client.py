import socket
from threading import Thread

#socket object to connect to server
s = socket.socket()

# ip and port of host ( server )
HOST = '127.0.0.1' 
PORT = 3000

# connect to server
s.connect( (HOST, PORT ) )

# server - client logic
while True:
    print( " Server > {} ".format (s.recv(1024).decode()) )

    message = input ( "You > " )
    s.send( message.encode() )
