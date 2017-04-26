#!/usr/bin/env python3
for each_character in "Hello":
    print(each_character, end="\t")

print("\nrange(5)", end="\t")
for i in range(5):
    print(i, end=" ")

print("\nrange(5, 10)", end="\t")
for i in range(5, 10):
    print(i, end=" ")

print("\nrange(-5, 9, 3)", end="\t")
for i in range(-5, 9, 3):
    print(i, end=" ")
    
print()