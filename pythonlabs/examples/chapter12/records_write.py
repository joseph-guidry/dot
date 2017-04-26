#!/usr/bin/env python3
import pickle
from records import *
def main():
    rec1 = Record1("Mike", 25)
    lis = [rec1, Record2("Joe", rec1)];
    with open("complex", "wb") as file:
        pickle.dump(lis, file)
if __name__ == "__main__": main()