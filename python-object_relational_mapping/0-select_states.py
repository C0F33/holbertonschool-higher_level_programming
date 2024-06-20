#!/usr/bin/python3
"""this script lists all states in the db"""

from MySQLdb import MySQLdb
import sys



if __name__ == "__main__":
	username = sys.argv[1]
	password = sys.argv[2]
	db_name = sys.argv[3]


	db = MySQLdb.connect(host="localhost", port=3306, user="user", passwd="password", db="db_name")
	cursor = db.cursor()
	cursor.execute("SELECT * FROM states ORDER BY id ASC")
	data = cursor.fetchall()
	for state in data:
		print(state)

	db.close()