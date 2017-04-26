#!/usr/bin/env python3
import shelve
from records import *
def main():
    with shelve.open('myfile') as file:
        r1 = Record1('mike', 55)
        r2 = Record2('jane', r1)
    
        file['first'] = r1
        file['second'] = r2
    
        result1 = file['second']
        print(result1)
        
        result2 = file['first']
        print(result2)

if __name__ == "__main__": main()