#!/usr/bin/env python3
def fun():
    first = 0
    second = 1
    def fibonacci():
        nonlocal first, second
        nextNum = first
        first, second = second, first + second
        return nextNum
    
    return fibonacci


result = fun()
for i in range(10):
    print(result(), end = " ")
print()