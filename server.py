#!/usr/bin/env python3

import socket
import time


address = '127.0.0.1'
port = 8888

server_sock = socket.socket()
print("server socket successfully created")

server_sock.bind((address, port))
print("server socket bound")

a = 0

server_sock.listen(1)
print("server socket now listening\n")

conn, addr = server_sock.accept()
while True:

    
    data = conn.recv(1024)
    print(data.decode())
