
import MySQLdb
from sys import argv
import sys

if __name__ == "__main__":

    db = MySQLdb.connect(host='localhost', port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])

    cursor = db.cursor()
    query = "SELECT * FROM states WHERE name LIKE '{:s}' ORDER BY id ASC".format(argv[4])
    cursor.execute(query)
    rows = cursor.fetchall()
    for row in rows:
        if row[1] == argv[4]:
            print(row)
        cursor.close()
        db.close()