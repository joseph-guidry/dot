#!/usr/bin/env python3
#
# A Solution For Chapter 3 Exercise 5
#
for value in range(50):
    print("%3d " % value, end="")
    #print("{:3}".format(value), end="")
    if value % 10 == 9:
        print()