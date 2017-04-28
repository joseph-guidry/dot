#! /usr/bin/env python3


def sort(alist):

    return sorted(alist)

def reverse(alist):
    rlist = list(alist)
    rlist.reverse()
    
    return rlist


bubble_list = [ 5, 2, 3, 9, 10]

print(bubble_list)

print(sort(bubble_list))
print(reverse(bubble_list))
print(reverse(sort(bubble_list)))
print(bubble_list)

