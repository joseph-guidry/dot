#!/usr/bin/env python3
import pickle
from records import *
def main():
    with open("complex", "rb") as file:
        for obj in pickle.load(file):
            print(obj)
if __name__ == "__main__": main()