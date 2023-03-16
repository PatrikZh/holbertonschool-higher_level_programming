#!/usr/bin/python3
""" Listing all states from the database hbtn_0e_0_usa in ORM method"""
import MySQLdb
import sys

mydb = MySQLdb.connect(
    host = "localhost",
    user = sys.argv[1],
    password = sys.argv[2],
    database = sys.argv[3]
)
cursor = mydb.cursor()
query = "SELECT * FROM states ORDER BY id"
cursor.execute(query)
results = cursor.fetchall()
for row in results:
    print(row)
mydb.close()
