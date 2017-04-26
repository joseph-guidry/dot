#!/usr/bin/env python3
#
# Server Part Of A Solution For Chapter 13 Exercise 1
#
import socket

HOST = 'localhost'
PORT = 2310

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(5)

print('Waiting for connection...')
conn, addr = s.accept()
print('Connection from:', addr)

while True:
    data = conn.recv(1024)
    if not data: 
        break
    thestring = data.decode()
    tot = 0
    for i in thestring:
        tot += ord(i)
    data = str(tot)
    data = data.encode()
    conn.send(data)
conn.close()
