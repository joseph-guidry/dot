#!/usr/bin/env python3
#
# A Solution For Chapter 12 Exercise 2 Part 1
#
from customer_and_address import Address, Customer
import pickle

def get_customers():
    customer_list = []
    with open("customers.txt", "r") as thefile:
        for customer_txt in thefile:
            c = customer_txt.rstrip().split(",")
            address = Address(c[2], c[3], c[4], c[5])
            customer = Customer(c[0], c[1], address)
            customer_list.append(customer)
    return customer_list

customers = get_customers()
with open('customers.pickle', 'wb') as file:
    pickle.dump(customers, file)

print("Customers persisted")