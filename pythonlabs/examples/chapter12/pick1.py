#!/usr/bin/env python3
import pickle
def main():
    with open('pick', 'wb') as file:
        pickle.dump("This is a string", file)
        pickle.dump("This is another string of text", file)
if __name__ == "__main__": main()