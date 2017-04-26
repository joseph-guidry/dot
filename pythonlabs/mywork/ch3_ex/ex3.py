#! /usr/bin/env python3

numbers = input("Enter multiple numbers: ")

number = numbers.split()

for piece in number:
   if (int(piece) > 0):
       print(piece)


