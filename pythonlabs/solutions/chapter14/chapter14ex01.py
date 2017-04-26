#!/usr/bin/env python3
#
# A Solution For Chapter 14 Exercise 1
#
import sqlite3

txtfile = open("records.txt", "r")
csvList = txtfile.readlines()
txtfile.close()
rows = []
for line in csvList:
    rows.append(line.rstrip().split(","))
 
conn = sqlite3.connect('dbase1')
print("connected to database")
curs = conn.cursor()
cmd = 'create table people \
       (name char(30), job char(10), pay int(4))'
curs.execute(cmd)

for row in rows:
    curs.execute('insert into people values(?,?,?)',
                 row)
conn.commit()

curs.execute('select * from people where pay > 50000')
for n,o,p in curs.fetchall():
    print(n,o,p)
