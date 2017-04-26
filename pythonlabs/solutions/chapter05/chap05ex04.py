#!/usr/bin/env python3
#
# A Solution For Chapter 5 Exercise 4
#
def deliver(a, b):
    def addthem():
        return a + b
    return addthem

f = deliver(10,20)
print(f())