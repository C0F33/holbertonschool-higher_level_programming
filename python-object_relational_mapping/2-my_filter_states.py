#!/usr/bin/python3
"""Displays all values in the states table of the database hbtn_0e_0_usa"""

import sys
import MySQLdb

def display_filtered_states():
	"""
	Connects to the database and displays all values in the states table
	that match the provided name argument.
	"""
	db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
	cursor = db.cursor()
	cursor.execute("SELECT * \
				 FROM `states` \
				WHERE BINARY `name` = '{}'".format(sys.argv[4]))
	[print(state) for state in cursor.fetchall()]

if __name__ == "__main__":
	display_filtered_states()
