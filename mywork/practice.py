#! /usr/bin/env python3

import sys

text = input(">")
N = int(text.strip())

if (N % 2):
    print("Weird")
else:
    if (N >= 2) & (N <= 5):
        print("Not Weird1")
    elif N >= 6 & N <= 20:
        print("Weird")
    else:
        print("Not Weird2")
