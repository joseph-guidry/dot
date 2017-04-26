#! /usr/bin/env python3

number1 = input("Enter a number: ")
number2 = input("Enter another number: ")


if (number1 < number2):
    print("The number " + number2 + "is larger")
elif (number1 > number2):
    print("The number " + number1 +" is larger")
else:
    print("The numbers are equal")


