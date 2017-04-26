#!/usr/bin/env python3
import sys, socket

def main():
    host = 'time.nist.gov'  # default server address
    port = 13               # deafult server port
    buffersize = 1024
    if len(sys.argv) == 3:
        host = sys.argv[1]
        port = int(sys.argv[2])
    
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))
    print("Connected To:", s.getpeername(),
          "From:", s.getsockname())
    while True:
        data = s.recv(buffersize)
        if not data: break
        print('Received:', data.decode()) # Decode to string
    s.close()
    
if __name__ == "__main__": main()