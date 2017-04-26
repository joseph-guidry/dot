#!/usr/bin/env python3
def outer(a, b):
    x = 15
    y = 20

    def inner():
        print(a, b, x, y)

    return inner # a reference to inner function

result = outer(5, 10)
print(type(result))
result() # invoke the returned function