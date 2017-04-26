#! /usr/bin/env python3


#start = input("Enter a starting number:  ")
#upper = input("Enter an upper limit:  \n> ")
#step  = input("Enter the step value:  ")

numbers  = input("enter a range with step -> start, end, step:   \n> ")
number = numbers.split(',')

print(number)
start, upper, step = number
for i in range(int(start), int(upper), int(step)):
    print(i, end=" ")
print()
