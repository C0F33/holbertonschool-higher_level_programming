#!/usr/bin/python3

from sys import argv
import MySQLdb

"""Lists all states"""


if __name__ == "__main__":
    """ establishes a connection to the database """
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3], charset="utf8")
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC;")
    records = cursor.fetchall()
    for row in records:
        if row[1][0] == 'N':
            print(row)
    cursor.close()
    db.close()