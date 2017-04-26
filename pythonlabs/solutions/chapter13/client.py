#!/usr/bin/env python3
#
# Client Part Of A Solution For Chapter 13 Exercise 1
#
import socket

HOST = 'localhost'
PORT = 2310

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

while 1:
    line = input("Enter a string ('quit' to exit): ")
    if line == 'quit':
        break
    
    s.send(line.encode())
    data = s.recv(1024)
    print('Received:', data.decode())
    val = data.decode()
    val = int(val)
    val = val % 100
    print("Result is", val)
s.close()
