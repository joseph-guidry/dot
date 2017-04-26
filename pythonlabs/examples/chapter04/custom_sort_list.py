#!/usr/bin/env python3
fmt = "For Input: {:18}    Sort Using: {}"
def theLastWord(aString):
    lastWord = aString.strip().split()[-1]
    print(fmt.format(aString, lastWord))
    return lastWord

names = """Ava Smith, Ethan Johnson, Abigail Williams, \
Sophia Brown, Michael Jones, Emily Miller, Declan Lee"""
names = names.split(", ")
print(names)
names.sort(key=theLastWord)
print(names)
