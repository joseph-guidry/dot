#!/usr/bin/env python3
#
# A Solution For Chapter 3 Exercise 2
#
num1 = int(input("enter the first number: "))
num2 = int(input("enter the second number: "))

total = 0
while( num1 <= num2 ):
    total += num1
    num1 += 1

print("Total = ", total)

# Alternative way to calculate the sum
num1 = int(input("enter the first number: "))
num2 = int(input("enter the second number: "))
total = 0
for val in range(num1, num2 + 1):
    total += val

print("Total = ", total)    