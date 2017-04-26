#!/usr/bin/env python3
import sqlite3

def get_customers():
    with open("customers.txt", "r") as thefile:
        customer_list = thefile.readlines();
    # use a list comprehension to convert to a
    # nested list of lists (each a list of strings)
    return [customer.rstrip().split(",") for
                     customer in customer_list]
    
def main():
    customer_list = get_customers()
    conn = sqlite3.connect('customerdb')
    print("connected to database")
    curs = conn.cursor()
    cmd = 'create table if not exists customers (firstname text, lastname text,  street text, city text, state text, zip text)'
    curs.execute(cmd)
    
    curs.executemany('insert into customers values(?, ?, ?, ?, ?, ?)', customer_list)
    conn.commit()
    
    curs.execute("select * from customers where state = 'WV'")
    for row in curs.fetchall():
        print(row)

if __name__ == "__main__": main()