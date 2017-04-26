#!/usr/bin/env python3
#
# A Solution For Chapter 7 Exercise 1
#
class Person:
    def __init__(self, fn = "Unknown", age = 21, gender="Unkown"):
        self.name = fn
        self.age = age
        self.gender = gender

    def __str__(self):
        s = self.name + " " + str(self.age) + " " + self.gender
        return s

mom = Person("Sally", 76, "F") 
dad = Person("Arthur", 62, "M")
print(mom)
print(dad)