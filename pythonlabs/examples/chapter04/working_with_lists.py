#!/usr/bin/env python3
lis = [10, 20, 30, 40, 20, 50]
fmt = "{0:>24} {1}"
print(fmt.format("Original:", lis))
print(fmt.format("Pop Last Element:", lis.pop()))
print(fmt.format("Pop Element at pos# 2:", lis.pop(2)))
print(fmt.format("Resulting List:", lis))

lis.append(100)
print(fmt.format("Appended 100:", lis))
lis.remove(20)
print(fmt.format("Removed First 20:", lis))
lis.insert(1, 1000)
print(fmt.format("Inserted 1000 at pos# 1:", lis))

lis.sort()
print(fmt.format("Sorted:", lis))
lis.reverse()
print(fmt.format("Reversed:", lis))
lis[0] = -99
print(fmt.format("Modified:", lis))