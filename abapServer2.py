
### ABAP SERVER ###

import socket							#load the socket functions
import sys							#load the sys functions, we need this to grab arguements

sock = socket.socket()						#set up a new socket to use

port = 666							#name our port within the ip
sock.bind(("127.0.0.1",port))					#socket now uses our hostname and port

try:
	print("Welcome to ABAP SERVER:\nusing file: " + sys.argv[1])
except:
	sys.exit("ERROR: NO ARGUMENTS SPECIFIED, PLEASE TRY AGAIN\n")	#if no arg, exit

f = open(sys.argv[1], "r")						#open file from 1e argument in read-mode
wave = f.read()								#read file and store as variable

sock.listen(5)							#listen for new connections, max backlog is 5.

while True:							#loop forever
	client, addr = sock.accept()				#sock.accept() gives 2 items as output. one is a new client object, and one is their address
	print("Reciving connection from:", addr)
	client.send(wave)
	client.close()						#Close client connection
	print("\n")
