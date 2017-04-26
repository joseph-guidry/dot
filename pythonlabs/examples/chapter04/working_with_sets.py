#!/usr/bin/env python3
# Define the strings that are used multiple times
prompt1 = "Please enter some first names "
prompt2 = prompt1 + "again "
prompt3 = prompt2 + "to delete "
nameList = input(prompt1).split()
uniqueNames = set(nameList)
backedupNames = set(uniqueNames)
print(uniqueNames, "\n")

# Check to see if name exists prior to adding
nameList = input(prompt2).split()
for name in nameList:
    if not name in uniqueNames:
        uniqueNames.add(name)
    else:
        print("\t", name, "already exists and is ignored")
print(uniqueNames, "\n")

# Update contents of set with contents of a list
nameList = input(prompt2).split()
uniqueNames.update(nameList)
print(uniqueNames, "\n")

# Check to see if name exists prior to removing
nameList = input(prompt3).split()
for name in nameList:
    if name in uniqueNames:
        uniqueNames.remove(name)

# Discard words without checking first
nameList = input(prompt3).split()
for name in nameList:
    uniqueNames.discard(name)
print(uniqueNames, "\n")

# Check the relationship of one set to another
print()
print("Original:", backedupNames)
print("Current :", uniqueNames, "\n")
print("Original is subset of Current ? ",
      backedupNames.issubset(uniqueNames))
print("Current is superset of Original ? ",
      uniqueNames.issuperset(backedupNames))

# Pop each element from the set until it is empty
print("Popping each name from set: ", uniqueNames)
while len(uniqueNames):
    print(uniqueNames.pop(), end=" ")
print()