#!/usr/bin/env python3
def add():
    val = input("Enter value to add: ")
    aList.append(val)

def delete():
    x = aList.pop(0)
    print("removing", x)

def display():
    print("displaying:", aList)

def terminate():
    print("terminating") 
    exit()

def illegal():
    print("Illegal Selection\n")

aList = []
menu = {"1":add, "2":delete, "3":display, "4":terminate}
keys = sorted(menu.keys())
while True:
    print("Make selection:")
    for key in keys:
        print("\t", key, menu[key].__name__)
    key = input(">")
    
    menu.get(key, illegal)()