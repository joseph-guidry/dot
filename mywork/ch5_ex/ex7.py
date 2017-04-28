#! /usr/bin/env python3

def update_value(dictionary, num):
    """Take a dictionary and number to add values. Returns an updated
       dictionary"""
    for key in dictionary:
        dictionary[key] += num  #with no return


dict_value = {"cats":0, "dogs":0}

#get input and convert to int
number = int(input("What value do you want to increase by?\n>"))

update_value(dict_value, number)   #no need to use a return of function()
                                   #dict_value is updated in place.
animal = list(dict_value.keys())

for thing in animal:
    print("there are " + str(dict_value[thing]) + " " + thing +" in the zoo")


