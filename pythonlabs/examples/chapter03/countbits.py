#!/usr/bin/env python3
""" Count the bits that are set in a variable """

count  = 0
value = int(input("Please enter an integer: "))
print("Number", "\tDec:", value, "\tHex:", hex(value),
      "\tOct:", oct(value),"\tBin:", bin(value), "\n")

while value > 0:
    bit = value & 1   # perform a bitwise AND
    txt = "{0:08b} & {1:08b} =  {2}".format(value, 1, bit)
    print(txt)
    
    if bit:
        count += 1
    value = value >> 1 # value >>= 1 would also work

print("\n# of bits set = ", count)