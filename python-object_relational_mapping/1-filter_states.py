from sys import argv
import MySQLdb

#!/usr/bin/python3


if __name__ == "__main__":
		# Establish a connection to the database
		db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
							 passwd=argv[2], db=argv[3], charset="utf8")
		cursor = db.cursor()

		# Execute the query with the desired filter
		query = "SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC;"
		cursor.execute(query)

		# Fetch all records and print them
		records = cursor.fetchall()
		for row in records:
			print(row)
		cursor.close()
		db.close()

