#!/usr/bin/env python3
quot = """First Name: {0}
Last Name: {2}
Middle Initial: {1}"""
line = quot.format("John", "C.", "Smith")
print(line)
 
quot="Type: {type}\nHeight:{height}, Width:{width}"
line=quot.format(height=50, width=25, type="Rectangle")
print(line)