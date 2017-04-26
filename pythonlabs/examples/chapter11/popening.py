#!/usr/bin/env python3
import os
def main():
    stream = os.popen("ls", "r")
    for filename in stream:
        print(filename)

if __name__ == "__main__": main()