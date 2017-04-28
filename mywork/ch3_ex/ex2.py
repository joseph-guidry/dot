#! /usr/bin/env python3

number1 = input("Enter a number:  ")
number2 = input("Enter a number a bigger number:  ")

total = 0

for i in range(int(number1), int(number2) + 1):
    total = total + i 

print(total)
