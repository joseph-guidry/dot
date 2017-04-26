#!/usr/bin/env python3

s = "Spam and eggs"

print(s[0], "|", s[3])           # Indexing
print(s[-1], "|", s[-4])         # Negative Index
print()

print(s[2:7])                    # Slicing
print(s[5:])
print(s[:8])
print()

print(s[-3:-1])                    # Slice from end
print(s[-3:])
print(s[:-1])
print()

x = "abcdefghijklmnopqrstuvwxyz"
print(x[2:18:3])                 # Extended Slicing
start = 18
print(x[start::1])
print(x[::1])
