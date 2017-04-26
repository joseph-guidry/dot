#!/usr/bin/env python3
""" Add the integers from 5 to 10 """
counter = 5
total = 0

while counter <= 10:
    total += counter
    counter += 1
    print("Partial Total =", total, "Counter =", counter)

print("Final Total: ", total)