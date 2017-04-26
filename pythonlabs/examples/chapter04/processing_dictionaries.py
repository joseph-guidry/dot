#!/usr/bin/env python3
#!/usr/bin/env python3
rewardPoints = {"Bryce":500, "Heather":2000, "Kaylie":750,
                "Amanda": 1350, "Casey":2400, "Jason":800,
                "Kaylie":25}
print("Looping through dictionary")
print("*" * 75)
for name in rewardPoints:
    print(name, rewardPoints[name])

print("\n\n", "Looping through keys()")
print("*" * 75)
for name in rewardPoints.keys():
    print(name, end=" ")

print("\n\n", "Looping through values()")
print("*" * 75)
for value in rewardPoints.values():
    print(value, end=" ")


print("\n\n", "Looping through items() as tuples")
print("*" * 75)
for item in rewardPoints.items():
    print(item)

fmt = "{:8}~{:>8}\t\t"
print("\n\n", "Items() unpacked as keys and values")
print("*" * 75)
print(fmt.format("Name", "Points"))
for name, points in rewardPoints.items():
    print(fmt.format(name, points))

print("\n\n", "Data types of returned views")
print("*" * 75)
print("keys()  ", type(rewardPoints.keys()))
print("values()", type(rewardPoints.values()))
print("items() ", type(rewardPoints.items()))