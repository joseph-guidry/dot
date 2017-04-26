#!/usr/bin/env python3
import sys, os
from socket import socket, AF_INET, SOCK_STREAM
def main():
    host, port = 'localhost', 4000 + os.getuid()
    if len(sys.argv) == 3:
        host, port = sys.argv[1], int(sys.argv[2])
    
    with socket(AF_INET, SOCK_STREAM) as toserver:
        toserver.connect((host, port))
        prompt = "Enter a string to send to the server:"
        print("Connected To:", toserver.getpeername(),
              "From:", toserver.getsockname())
        while True:
            text = input(prompt)
            if text.lower() == "quit": break
            toserver.send(text.encode())
            data = toserver.recv(1024)
            if not data: break
            print(data.decode())
if __name__ == "__main__": main()