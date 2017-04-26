#!/usr/bin/env python3
from fraction import Fraction

def main():
    fractions = [Fraction(1,3), Fraction(), Fraction(3,4)]
    for f in fractions:
        print(f)

    a,b,c = fractions
    print(a, "<", b, ":", a < b)      # 1/3 < 0/1 : False
    print(a, "<", c, ":", a < c)      # 1/3 < 3/4 : True
    result = a * c
    print(a, "*", c, "=", result)     # 1/3 * 3/4 = 3/12
    
if __name__ == "__main__": main()