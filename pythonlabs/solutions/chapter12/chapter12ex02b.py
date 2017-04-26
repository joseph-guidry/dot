#!/usr/bin/env python3
#
# A Solution For Chapter 12 Exercise 2 Part 2
#
import pickle


with open('customers.pickle', 'rb') as file:
    customers = pickle.load(file)
    for customer in customers:
        print(customer)
        print()
