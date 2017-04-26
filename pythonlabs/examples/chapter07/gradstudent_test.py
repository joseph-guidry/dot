#!/usr/bin/env python3
from gradstudent import GradStudent

def main():
    gs1 = GradStudent("James", "Anthropology", 25000)
    
    print("  MAJOR:", gs1.major)
    print("   NAME:", gs1.name)
    print("STIPEND:", gs1.stipend)
    print(gs1)

if __name__ == "__main__": main()