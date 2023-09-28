#!/usr/bin/python3
"""
This script lists all cities of a specified state from the hbtn_0e_4_usa database.
"""
import sys
import MySQLdb


if __name__ == "__main__":
    if len(sys.argv) != 5:
        print('Usage: {} <username> <password> <database> <state_name>'.format(sys.argv[0]))
        sys.exit(1)
    username, password, database, state_name = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database
    )
    cursor = db.cursor()
    cursor.execute("SELECT GROUP_CONCAT(name SEPARATOR ', ') "
                   "FROM cities "
                   "JOIN states ON cities.state_id = states.id "
                   "WHERE states.name = %s "
                   "ORDER BY cities.id ASC", (state_name,))
    cities = cursor.fetchall()
    city_names = [city[0] for city in cities]
    cities_str = ', '.join(city_names)
    print(cities_str)
    cursor.close()
    db.close()
