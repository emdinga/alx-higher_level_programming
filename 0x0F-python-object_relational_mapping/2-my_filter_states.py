#!/usr/bin/python3
"""
This script displays all values in the states table where the name matches the provided argument.
"""

import sys
import MySQLdb
if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
            passwd=sys.argv[2], db=sys.argv[3], port=3306)
    cursor = db.cursor()
    query = "SELECT * FROM states WHERE name = '{}' ORDER BY id".format(state_name)
    cursor.execute(query)
    results = cursor.fetchall()
    for row in results:
        print(row)
    cursor.close()
    db.close()

