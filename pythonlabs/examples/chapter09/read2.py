#!/usr/bin/env python3
def main():
    theFile =  open(input("Enter a file name: "), "r")
    for aLine in theFile:
        print(aLine, end="")
    theFile.close()
if __name__ == "__main__": main()