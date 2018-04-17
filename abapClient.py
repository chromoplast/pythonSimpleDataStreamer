#### ABAP CLIENT ####

import socket								#load functions for sockets

sock = socket.socket()							#define a new socket
port = 666								#define ip port to connect to

sock.connect(("127.0.0.1", port))					#127.0.0.1-> LOCALHOST
print(sock.recv(2048))							#recev max amt of data as 2048
sock.close								#shut it down

