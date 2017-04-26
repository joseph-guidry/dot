#!/usr/bin/env python3
import pickle
def main():
    with open('pick', 'rb') as file:
        print(pickle.load(file))
        print("*" * 30)
        print(pickle.load(file))
if __name__ == "__main__": main()