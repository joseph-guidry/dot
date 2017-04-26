#!/usr/bin/env python3
import pickle
def main():
    with open('data', 'rb') as file:
        try:
            while True:
                obj = pickle.load(file)
                print(obj)
        except EOFError:
            pass #quietly ignore as it is expected to happen
if __name__ == "__main__": main()