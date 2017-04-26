#!/usr/bin/env python3
def thesum(*args):
    total = 0
    print("Parameter type:", type(args), end=" ")
    for elem in args:
        total += elem
    return total

x = thesum(1,2,3,4,5)
print("Sum is: ", x)
x = thesum(5,2,7)
print("Sum is: ", x)