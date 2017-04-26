#! /usr/bin/env python3 

number_map = {"0":"zero", "1":"one", "2":"two", "3":"three", "4":"four", "5": "five","6":"six", 	      "7":"seven", "8":"eight", "9":"nine", "10":"ten", ".":"dot"}

input_num = input("enter a whole number> ")

for num in input_num:
    print(number_map.get(num), end=" ")

print()
print(number_map)
