#!/usr/bin/env python3
import pickle
lis = ['mike', 'jane', 'pete', 'bill']
map = {}
for i,v in enumerate(lis):
    map[i] = v
    print(i,v)
print(map)
file = open('data', 'wb')
pickle.dump(map, file) # write the map
pickle.dump(lis, file) # write the list