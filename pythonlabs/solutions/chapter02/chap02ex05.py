#!/usr/bin/env python3
#
# A Solution For Chapter 2 Exercise 5
#
data = input("enter a string: ")
x = data.isalpha()

print("ENDS WITH A PERIOD:", data.endswith("."))
print("ALL ALPHA CHARS   :", x)
print("x IN THE STRING   :", 'x' in data)

newstring = data.replace('e', 'E')
print(newstring)