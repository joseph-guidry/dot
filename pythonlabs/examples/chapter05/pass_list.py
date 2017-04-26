#!/usr/bin/env python3
def multiply_by(qty, aList):
    for index, value in enumerate(aList):
        aList[index] = value * qty
data = [ 10, 20, 30, 40 ]
print("Before:", data)
multiply_by(5, data)
print("After:", data)

otherData = ["Me", "the", "Hello"]
print("Before:", otherData)
multiply_by(5, otherData)
print("After:", otherData)