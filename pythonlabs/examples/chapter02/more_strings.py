#!/usr/bin/env python3
x = "Capital of Mississippi is Jackson"
position = x.find("is")
print(position)
print(x.find("is", position + 1))
print(x.find("is", 8, 12))
print()

x = "1 1 1 1abc"
y = x.replace("1","0")
print(y)
y = x.replace("1", "0", 2)
print(y)
print()

aList = x.split(' ')
print(x)
print(aList)