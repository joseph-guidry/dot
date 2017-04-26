#!/usr/bin/env python3
import sys
from socket import socket, AF_INET, SOCK_STREAM
def main():
    host, port = 'time.nist.gov', 13
    if len(sys.argv) == 3:
        host, port = sys.argv[1], int(sys.argv[2])
    
    with socket(AF_INET, SOCK_STREAM) as s:
        s.connect((host, port))
        print("Connected To:", s.getpeername(),
              "From:", s.getsockname())
        while True:
            data = s.recv(1024)
            if not data: break
            print('Received:', data.decode())
if __name__ == "__main__": main()