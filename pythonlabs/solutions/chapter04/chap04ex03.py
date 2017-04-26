#!/usr/bin/env python3
#
# A Solution For Chapter 4 Exercise 3
#
themap = { 0:'zero', 1:'one', 2:'two', 3:'three', 4:'four',
           5:'five', 6:'six', 7:'seven', 8:'eight', 9:'nine'}

number = input("Enter a number: ")

for digit in number:
    print(themap[int(digit)], end=" ")

print()

# Alternate Solution
themap = { '0':'zero', '1':'one', '2':'two', '3':'three', '4':'four',
           '5':'five', '6':'six', '7':'seven', '8':'eight', '9':'nine'}

number = input("Enter a number: ")

for digit in number:
    print(themap[digit], end=" ")