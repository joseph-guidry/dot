#!/usr/bin/env python3
#
# A Solution For Chapter 12 Exercise 1 Part 1
#
import dbm

def get_customers():
    with open("customers.txt", "r") as thefile:
        customer_list = thefile.readlines();
    # use a list comprehension to convert to a
    # nested list of lists (each a list of strings)
    return [customer.rstrip().split(",") for
                     customer in customer_list]

customers = get_customers()
with dbm.open('customers.dbm', 'c') as file:
    for customer in customers:
        file[customer[0] + " " + customer[1]] = customer[5]

print("Customers persisted")