#!/usr/bin/python3
"""this script lists all states in the db"""

from MySQLdb import MySQLdb
import sys
from MySQLdb import MySQLdb



if __name__ == "__main__":
	username = sys.argv[1]
	password = sys.argv[2]
	database_name = sys.argv[3]


	db = MySQLdb.connect(host="localhost", port=3306, user=user, passwd=password, db=database_name)
	cur = db.cursor()
	cur.execute("SELECT * FROM states")
	data = cur.fetchall()
	for row in rows:
		print(row)

	db.close()