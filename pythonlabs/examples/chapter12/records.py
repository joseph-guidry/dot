#!/usr/bin/env python3
class Record1:
    def __init__(self, name, age):
        self.name = name;
        self.age = age
    def __str__(self):
        return "This is a record 1 type."

class Record2:
    def __init__(self, name, record1):
        self.record1 = record1
        self.name = name
    def __str__(self):
        return "This is a record 2 type."