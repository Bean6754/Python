#!usr/bin/python3
import time
import socket
import sys

print ("Server starting in: ")
print ("2")
time.sleep(1)
print("1")
time.sleep(1)

# Create socket.
serversocket = socket.socket(
	        socket.AF_INET, socket.SOCK_STREAM)

# Obtain system hostname.
host = socket.gethostname()

# Set port.
port = 80

# Bind socket to port.
serversocket.bind((host, port))

# Listen for 5 socket requests.
serversocket.listen(5)

while True:
    # Establish connection.
    clientsocket,addr = serversocket.accept()
    print("Got a connection from %s" % str(addr))
    msg='Thank you for connecting'+ "\r\n"
    clientsocket.send(msg.encode('ascii'))
    clientsocket.close()
