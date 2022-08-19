import socket
from threading import Thread

# socked object for handling connecitons
s=socket.socket()
print( "Socket created Successfully ")

# port to bind socket
HOST = ''
PORT = 3000

#binding socket to 127.0.0.1 : 3000
s.bind( (HOST , PORT) )
print( "Socket binded to {}:{} ".format( HOST, PORT ))

# put socket in listening mode
s.listen( 5 )
print( "Socket is listening ")

# Maintains list of clients
list_of_clients = []

# Function to handle each user connection
def client_thread( conn, addr ):
    conn.send( "Welcome to chat room ".encode() )
    while True:
        try:
            message = conn.recv( 1024 ) 
            print( "Client > {}".format(message) )
            # if message:
            #     message_to_send =  "<{}> {}".format( addr[0], message )
            #     broadcast( message_to_send , conn )
            # else:
            #     # if message is empty, it means connection ended abruptly
            #     remove ( conn )
        except:
            continue

# Funcion to broadcast message to all connections
def broadcast ( message, conn ):
    for client in list_of_clients:
        if client == conn: 
            continue
        else:
            try:
                client.send( message.encode() )
            except:
                # if unable to send message, connection has disconnected
                client.close()
                remove( client )

#Function to remove connecton
def remove ( connection ):
    if connection in list_of_clients:
        list_of_clients.remove( connection )
        connection.close()

# SERVER LOGIC
while True:
    # Wait for connections
    # s.accept() is a blocking fn
    conn, addr = s.accept()
    print( "Got connection from ", addr )

    list_of_clients.append( conn )

    Thread( 
        target = client_thread,
        args = ( conn, addr )).start()

s.close()