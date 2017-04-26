#!/usr/bin/env python3
from student4 import Student
def main():
    s1 = Student("Elizabeth", "Electrical Engineering")
    s2 = Student("Robert", "Electrical Engineering")
    print(s1,"id=", id(s1))
    print(s2,"id=", id(s2))
    print("s1 == s2:", s1 == s2)
    s2.name = "Elizabeth"
    print()
    print(s1,"id=", id(s1))
    print(s2,"id=", id(s2))
    print("s1 == s2:", s1 == s2)

if __name__ == "__main__": main()