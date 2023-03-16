#!/usr/bin/python3
""" Script that takes an argument and returns name where matches the argument"""
import MySQLdb
import sys


if __name__ == "__main__":
    mysql_user = sys.argv[1]
    mysql_password = sys.argv[2]
    db_name = sys.argv[3]
    search_term = sys.argv[4]

    db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=mysql_user,
            passwd=mysql_password,
            db=db_name)
    
    cursor = db.cursor()
    query = "SELECT * FROM states WHERE name LIKE '{}%' ORDER BY id ASC".format(search_term)
    cursor.execute(query)
    result = cursor.fetchall()
    for el in result:
        print(el)
    db.close()
