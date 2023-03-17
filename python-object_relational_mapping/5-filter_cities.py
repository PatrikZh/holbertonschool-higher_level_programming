#!/usr/bin/python3
""" Listing name of a state as an argument and lists all cities"""
import MySQLdb
import sys


if __name__ == "__main__":
    mysql_user = sys.argv[1]
    mysql_password = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]

    db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=mysql_user,
            passwd=mysql_password,
            db=db_name)
    cursor = db.cursor()
    query = "SELECT cities.* FROM cities \
    JOIN states ON cities.state_id = states.id \
    WHERE states.name=%s ORDER BY cities.id"
    cursor.execute(query, state_name,))
    result = cursor.fetchall()
    for el in result:
        print(el)
    db.close()
