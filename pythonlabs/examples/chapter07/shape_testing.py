#!/usr/bin/env python3
from shape_circle import Circle
from shape_square import Square
from shape_rectangle import Rectangle

def main():
    c1 = Circle("Circle 1", 10)
    s1 = Square("Square 1", 5)
    r1 = Rectangle("Rectang1e 1", 5, 10)
    
    shapes = [ c1, s1, r1 ]
    for shape in shapes:
        print(shape)
        print("AREA:", shape.area())
        print("******************")

if __name__ == "__main__": main()