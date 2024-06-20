#!/usr/bin/python3
"""Lists all states"""


import MySQLdb

from sys import argv, sys

if __name__ == '__main__':

    username = argv[1]
    password = argv[2]
    database_name = argv[3]

    db = MySQLdb.connect(host="localhost", port=3306, user=username,
                         passwd=password, db=database_name)
    cur = db.cursor()
    cur.execute("SELECT * FROM states ORDER BY id ASC;")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
