#!/usr/bin/python3
""" Listing all states from the database hbtn_0e_0_usa in ORM method"""
import MySQLdb
import sys


if __name__ == "__main__":
    mysql_user = sys.argv[1]
    mysql_password = sys.argv[2]
    db_name = sys.argv[3]

    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=mysql_user,
                         passwd=mysql_password,
                         db=db_name)

    cursor = db.cursor()
    query = "SELECT * FROM states ORDER BY id"
    cursor.execute(query)
    results = cursor.fetchall()
    for row in results:
        print(row)
    db.close()
