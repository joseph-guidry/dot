#!/usr/bin/env python3
import math, decimal, random

def math_examples():
    print("Square Root of 10:", math.sqrt(10))
    print("64 to 3/2 pow:", math.pow(64, 1.5))
    print("Hypotenuse of 6 and 8:", math.hypot(6,8))
    radians = math.radians(360)
    print("Radians to Degrees:", radians)
    print("Degrees to Radians", math.degrees(radians))
    print("Round 2.5 up", math.ceil(2.5))
    print("Round 2.5 down", math.floor(2.5))
    print("Pi", math.pi)

def decimal_examples():
    print(".1 + .2 is not normally thought of as", .1 + .2)
    d1 = decimal.Decimal(".1")
    d2 = decimal.Decimal(".2")
    print("It is normally:", d1 + d2)

def random_examples():
    aList = [9, 8, 7, 6, 5, 4, 3, 2]
    print("Random:")
    print(" float 0.0 <= x < 1.0:", random.random())
    print(" int from 0 to 9:", random.randrange(10))
    print(" choice ", aList, ":", random.choice(aList))
    random.shuffle(aList)
    print(" shuffle", ":", aList)
    print(" sample ", aList, ":", random.sample(aList, 4))

def main():
    math_examples()
    decimal_examples()
    random_examples()

if __name__ == "__main__": main()