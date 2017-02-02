#!/usr/bin/python3
import socket

# Create socket.
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Get hostname.
host = socket.gethostname()

# Set port.
port = 80

# Connect hostname to port.
s.connect((host, port))                               

# Receive no more than 1024 bytes.
msg = s.recv(1024)

# Close down sockets.
s.close()
print (msg.decode('ascii'))
