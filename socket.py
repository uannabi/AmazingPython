
import socket

# create a socket object
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# get local machine name
host = socket.gethostname()

# set port number
port = 12345

# bind the socket to a specific address and port
s.bind((host, port))

# listen for incoming connections
s.listen(5)

while True:
    # wait for a connection
    conn, addr = s.accept()
    print('Got connection from', addr)

    # send a message to the client
    message = 'Thank you for connecting'
    conn.send(message.encode('ascii'))

    # close the connection
    conn.close()

