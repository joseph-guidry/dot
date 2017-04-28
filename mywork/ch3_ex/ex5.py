#! /usr/bin/env python3

for i in range(0, 50):
    if i % 10 == 0:
        print()
    txt = "{:<2d}".format(i) 
    print(txt, end=" ")

print()
