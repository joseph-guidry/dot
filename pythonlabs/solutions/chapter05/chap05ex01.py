#!/usr/bin/env python3
#
# A Solution For Chapter 5 Exercise 1
#
def positive(alist):
    result = []
    for element in alist:
        if element > 0:
            result.append(element)
    return result

data = [5, -10, 10, -20, 30]
results = positive(data)
print(results)