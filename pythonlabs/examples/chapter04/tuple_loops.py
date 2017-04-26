#!/usr/bin/env python3
grades = ("A", "B", "C", "D", "F")
ranges = ("90-100", "80-89", "70-79", "60-69", "00-59")
for grade in grades:
    print(grade, end="\t")
print()

for aTuple in enumerate(grades):
    print(str(aTuple[0]) + ":" + aTuple[1], end="\t")
print()

# Unpacking the tuple from enumerate
for i, grade in enumerate(grades, start=1):
    print(str(i) + ":" + grade, end="\t")
print()

# Process the two lists in parallel
for index, grade in enumerate(grades):
    print(grade, ":", ranges[index])