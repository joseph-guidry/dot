#!/usr/bin/env python3
#
# A Solution For Chapter 5 Exercise 8
#
def reverse(param):
    lis = list(param)
    lis.reverse()
    return lis

def sort(param):
    return sorted(param)

values = [10,40,30,20,5]
print(sort(values))
print(reverse(values))
print(reverse(sort(values)))
print(values)