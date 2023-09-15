#!/usr/bin/python3
"""
This script displays all values in the states table where the name matches the provided argument.
"""

import sys
import MySQLdb

if __name__ == "__main__":
    # Check if the correct number of arguments is provided
    if len(sys.argv) != 5:
        print("Usage: {} <username> <password> <database> <state_name>".format(sys.argv[0]))
        sys.exit(1)

    # Get the command line arguments
    username, password, database, state_name = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]

    # Connect to the MySQL server
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database
    )

    # Create a cursor object to interact with the database
    cursor = db.cursor()

    # Prepare the SQL query with user input using format
    query = "SELECT * FROM states WHERE name = '{}' ORDER BY id".format(state_name)

    # Execute the SQL query
    cursor.execute(query)

    # Fetch all the results
    results = cursor.fetchall()

    # Print the results
    for row in results:
        print(row)

    # Close the cursor and the database connection
    cursor.close()
    db.close()

