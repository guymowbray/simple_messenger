#!/usr/bin/env python3


import socket
import time

server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = '127.0.0.1'
port = 8888

print("connected to 172.0.0.1:8888")

server_sock.connect((host, port))


while True:
    send_message = input("Enter your message:")

    server_sock.sendall(send_message.encode())
