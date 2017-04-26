#!/usr/bin/env python3
def findmax(a,b):
    max = 0
    if a < b:
        max = b
    elif a > b:
        max = a
    assert max == a or max == b, \
          "Max is not " + str(a) + " or " + str(b)
    return max;
def main():
    try:
        print(findmax(2,9), findmax(7,4))
        print(findmax(3,3))
    except AssertionError as ae:
        print("Assertion Failed:", ae)
if __name__ == "__main__": main()
