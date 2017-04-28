#! /usr/bin/env python

import sys

def sum_args(args_list, total=0):
    for num in args_list:
        total += num
    return total

def avg_args(total, num):
    avg = float(total/num)

    return avg

def main():
    args_list = sys.argv
    args_list.pop(0)

    args_list = list(map(int, args_list))
    total = sum_args(args_list)
    average = avg_args(total, len(args_list))
    

    fmt = "For {2} numbers, the average is: {0:.2f}. The total: {1:08b} or {1}"
    print(fmt.format(average, total, len(args_list)))

if __name__=="__main__": main()
