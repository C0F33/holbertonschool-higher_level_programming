#!/usr/bin/python3

from sys import argv
import MySQLdb

"""Lists all states"""


if __name__ == '__main__':
    mysql_username = argv[1]
    mysql_password = argv[2]
    database_name = argv[3]

    db = MySQLdb.connect(host="localhost", port=3306,
                         user=mysql_username, passwd=mysql_password, db=database_name)

    cursor = db.cursor()

    cursor.execute("SELECT * FROM states ORDER BY states.id")