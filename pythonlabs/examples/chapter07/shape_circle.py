#!/usr/bin/env python3
import math
from shape import Shape

class Circle(Shape):
    def __init__(self, name, radius):
        super().__init__(name)
        self.radius = radius

    def __str__(self):
        return super().__str__() + " Radius:" + \
               str(self.radius)

    def area(self):
        return math.pi * self.radius ** 2