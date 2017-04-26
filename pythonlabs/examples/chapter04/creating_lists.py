#!/usr/bin/env python3
listA = list()
listB = []
listC = [20, 3, 7, 82, -3, 456, 3, 65, 23]
listD = ["James", "Heather", "Monica", "Eugene"]
listE = listC + listD
print(listA, listB, listC, listD, listE, sep="\n")
print()
print(listC[0], listC[-1], listD[2], listE[4])
x = listC[0:5]
print(type(x), x)
print(listE[-5:])