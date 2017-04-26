#!/usr/bin/env python3
#
# A Solution For Chapter 12 Exercise 1 Part 2
#
import dbm

with dbm.open('customers.dbm', 'c') as file:
    customerKeys = file.keys()
    for key in customerKeys:
        print(key.decode(), ":", file[key].decode())