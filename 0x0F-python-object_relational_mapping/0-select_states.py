#!/usr/bin/python3
"""
This script lists all states from the database hbtn_0e_0_usa.
"""

import MySQLdb
import sys

if __name__ == '__main__':
    # Check if the correct number of arguments is provided
    if len(sys.argv) != 4:
        print("Usage: {} <username> <password> <database>".format(sys.argv[0]))
        sys.exit(1)

    try:
        # Establish a database connection
        db = MySQLdb.connect(host='localhost', port=3306,
                             user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])

        # Create a cursor object to interact with the database
        cur = db.cursor()

        # Execute the SQL query to select all states sorted by states.id
        cur.execute("SELECT * FROM states ORDER BY states.id ASC;")

        # Fetch all the rows
        rows = cur.fetchall()

        # Print the results
        for row in rows:
            print(row)

    except MySQLdb.Error as e:
        print("Error:", e)

    finally:
        # Close the cursor and the database connection
        cur.close()
        db.close()

