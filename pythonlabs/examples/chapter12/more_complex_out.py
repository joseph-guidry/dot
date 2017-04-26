#!/usr/bin/env python3
import pickle
from datetime import datetime
def main():
    alist = ['mike', 'jane', 'pete', 'bill']
    dictionary = {}
    date = datetime.today()
    for i,value in enumerate(alist):
        dictionary[i] = value
    print("Pickled:", alist, dictionary, date, sep="\n")
    with open('data', 'ab') as file:
        pickle.dump(alist, file) # write the dictionary
        pickle.dump(dictionary, file)      # write the list
        pickle.dump(date, file) # write date
    
if __name__ == "__main__": main()