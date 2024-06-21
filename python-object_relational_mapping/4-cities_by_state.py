#!/usr/bin/python3
# Lists all cities of the database hbtn_0e_4_usa, ordered by city id.

import sys
import MySQLdb

def list_cities_by_state():
	"""
	Lists all cities of the database hbtn_0e_4_usa, ordered by city id.
	"""
	db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
	cursor = db.cursor()
	cursor.execute("SELECT `c`.`id`, `c`.`name`, `s`.`name` \
				 FROM `cities` as `c` \
				INNER JOIN `states` as `s` \
				   ON `c`.`state_id` = `s`.`id` \
				ORDER BY `c`.`id`")
	[print(city) for city in cursor.fetchall()]

if __name__ == "__main__":
	list_cities_by_state()
