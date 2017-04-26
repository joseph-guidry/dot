#!/usr/bin/env python3
import os
from datetime import datetime
from socket import *

def setServerOptions(server, host, port):
    server.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    server.bind((host, port)) 
    server.listen(20)  # max number of queued connections
    
def main():
    host = '' # all available local interfaces
    port = 2000 + os.getuid() # Port based on userid
    msgs = "Waiting for connection:", " Connection from ..."
    with socket(AF_INET, SOCK_STREAM) as server:
        setServerOptions(server, host, port)
        print("Server started on port #:", port)
        while True:
            try:
                print(msgs[0], end="", flush=True)
                client, client_addr = server.accept()
                with client:
                    print(msgs[1], client_addr)
                    time = str(datetime.today()).encode()
                    client.send(time)
            except KeyboardInterrupt:
                print("\nShutting down the server")
                break;
            except Exception as err:
                print("Error w/Client:", client_addr, err)
if __name__ == "__main__": main()