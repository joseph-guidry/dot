#!/usr/bin/env python3
aList = [3, 1, -10, 54, 75, 29]
aTuple = ("Cheese", "Pepperoni", "Bacon", "Mushrooms")
aSet = {"AL", "NY", "MD", "VA", "PA", "KY", "VT" }
aDictionary = {'New Hampshire':'NH', 'Maryland':'MD',
               'Nevada':'NV', 'Maine':'ME'}
originals = [aList, aTuple, aSet, aDictionary]
print("Original Collections")
for collection in originals:
    print(collection)
print()
for collection in originals:
    sortedList = sorted(collection)
    print(type(collection).__name__, "sorted:", sortedList)
print()
print("Original Collections")
for collection in originals:
    print(collection)