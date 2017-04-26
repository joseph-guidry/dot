#! /usr/bin/env python3


pi = 3.14159;
radius = input("Radius = ");

print(type(pi * (int(radius)**2)))


areaCircle ="Area with radius " + radius + " is  :  %7.2f" % ( pi * (int(radius))**2) ;


print(areaCircle);
