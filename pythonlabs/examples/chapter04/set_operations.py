#!/usr/bin/env python3
a, b = [set('efgy'), set('exyz')]
print("The following operators return a new set")
print("Leaving the original two sets unchanged")
print("Set a:", a, "\t\t", "Set b: ", b)
print("\t", "a | b:", a | b )  # union
print("\t", "a & b:", a & b )  # intersection
print("\t", "a - b:", a - b )  # difference
print("\t", "b - a:", b - a )  # difference
print("\t", "a ^ b:", a ^ b )  # symmetric difference
print("Set a:", a, "\t\t", "Set b: ", b)
print("\n", "*" * 75)

print("\nThe following operator modifies the original set")
print("Set a:", a, "\t\t", "Set b: ", b)
a, b = [set('efgy'), set('exyz')]
a |= b
print("\t", "a |= b:", a )  # union
print("Set a:", a, "\t\t", "Set b: ", b)