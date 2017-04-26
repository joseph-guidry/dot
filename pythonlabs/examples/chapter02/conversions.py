#!/usr/bin/env python3
# conversions to an integer
print(int(23.45) + int("10"))
s = "11"
print("String of '11' converted to various bases as int")
print("Base 10:", int(s), "\tBase 2:", int(s,2))
print("Base 8:", int(s,8), "\tBase 16:", int(s, 16))

# conversions to a float
print(float("12.34") + float(".660") + float(10))

# As binary, octal, and hexadecimal strings
number = 987
print("Binary: " + bin(number))
print("Octal: " + oct(number))
print("Hex: " + hex(number))

print(ord("A"), chr(66))

print(str(99) + str(123.456))