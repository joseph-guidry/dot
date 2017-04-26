#!/usr/bin/env python3
class Student:
    def __init__(self, name, major):
        self._name = name
        self._major = major

    def getName(self):
        return self._name
    
    def setName(self, name):
        self._name = name
        
    def getMajor(self):
        return self._major
    
    def setMajor(self, major):
        self._major = major

def main():
    jeff = Student("Jeff", "American History")
    print(jeff.getName(), ":", jeff.getMajor())
    jeff.setName("Jeffrey")
    print(jeff.getName(), ":", jeff.getMajor())
    
if __name__ == "__main__": main()