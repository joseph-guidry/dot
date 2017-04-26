#! /usr/bin/env python3


numbers = set()
counter = 0


while(True):
    data = input("enter a number (enter 'quit' to exit)\n>")
    if data == 'quit':
        break

    if int(data) not in numbers:
        numbers.add(int(data)) 
    else:
        counter += 1
print(numbers)
print(str(counter) + " entries were not added")
