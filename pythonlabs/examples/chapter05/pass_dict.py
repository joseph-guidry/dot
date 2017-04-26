#!/usr/bin/env python3
def getAverage(param):
    total = 0
    for elem in param.values():
        total += elem
    return total/len(param)
scores = { 'mike':99, 'jill':100, 'sam':87 }
x = getAverage(scores)
print("Unformatted:", x)
print("Formatted: {:.4f}".format(x))