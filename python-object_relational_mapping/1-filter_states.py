#!/usr/bin/python3
""" Listing states with name starting with N from database hbtn_0e_0_usa"""
import MySQLdb
import sys


if __name__ == "__main__":
    mysql_user = sys.argv[1]
    mysql_password = sys.argv[2]
    db_name = sys.argv[3]

    db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=mysql_user,
            passwd=mysql_password,
            db=db_name)

    cursor = db.cursor()
    query = "SELECT * FROM states WHERE name LIKE BINARY 'N%'
    ORDER BY states.id ASC"
    cursor.execute(query)
    result = cursor.fetchall()
    for el in result:
        print(el)
    db.close()
