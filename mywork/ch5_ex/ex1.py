#! /usr/bin/env python3


def only_positive(alist):
    """Create list that returns only negative numbers"""
    list = []
    
    for number in alist:
        print(number)
        if number > 0:
            
            list.append(number)
    
    return list


alist = [ -1, 2, 0, 1.1, -1.34, -10, 10, 10]
pos_list = only_positive(alist)

print(pos_list)
