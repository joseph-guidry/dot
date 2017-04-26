#!/usr/bin/env python3
#
# A Solution For Chapter 7 Exercise 3
#

class Person:
    def __init__(self, fn = "Unknown", age = 21, gender="Unkown"):
        self.name = fn
        self.age = age
        self.gender = gender

    def __str__(self):
        s = self.name + " " + str(self.age) + " " + self.gender
        return s

class Family:
    def __init__(self, m, d, *args):
        self.mom = m
        self.dad = d
        self.kids = []
        for i in args:
            self.kids.append(i)

    def add(self, kid):
        self.kids.append(kid)
 
    def __str__(self):
        s = str(self.mom) + " " + str(self.dad) 
        for i in self.kids:
            s += "\n\t" + str(i)
        return s

    def __gt__(self, other):
        return len(self.kids) > len(other.kids)

    def __eq__(self, other):
        return len(self.kids) == len(other.kids)

    def __lt__(self, other):
        return len(self.kids) < len(other.kids)

mom = Person("Sally", 76, "F") 
dad = Person("Arthur", 62, "M")
joe = Person("Joel", 34, "M")
judy = Person("Judy", 35, "F");
fam1 = Family(mom, dad, joe, judy)
fam2 = Family(mom, dad, joe)

if fam1 > fam2:
    print("fam1 has more kids than fam2")

fam2.add(joe)

if fam1 == fam2:
    print("families have == number of kids"); 

fam2.add(joe)

if fam1 < fam2:
    print("fam1 has fewer kids than fam2")