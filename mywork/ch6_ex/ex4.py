#! /usr/bin/env python3

import sys

def convert_num(list_a):
    num_list = list(map(int, list_a))

    return num_list
         
def main():
    args_list = (sys.argv)
    args_list.pop(0)
    
    args_list = convert_num(args_list)
    args_list.sort()
    print(args_list)


if __name__=="__main__":main()
