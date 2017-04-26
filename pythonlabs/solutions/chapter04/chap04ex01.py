#!/usr/bin/env python3
#
# A Solution For Chapter 4 Exercise 1
#
count = 0
s = set()

while True:
    value = input("enter a value, or 'end': " )
    if value == "end":
        break

    if not value in s:
        s.add(value)
    else:
        count += 1

print(count, "values were not unique")
print("The set is", s)