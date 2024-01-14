#!/usr/bin/python3
"""
Script that lists all cities and their respective states
from hbtn_0e_0_usa db.
"""

import MySQLdb
import sys

if __name__ == "__main__":
    # check if the correct number of args is provided
    if len(sys.argv) != 4:
        print("Usage: {} <username> <password> <database>".format(sys.argv[0]))
        sys.exit(1)

    # extract arguments
    username, password, database = sys.argv[1], sys.argv[2], sys.argv[3]
    # connect to the MySQL server
    db = MySQLdb.connect(
        host="localhost",
        user=username,
        passwd=password,
        db=database,
        port=3306
    )
    # Create a cursor obj to interact with the db
    cursor = db.cursor()
    # Execute the SQL query to select cities & its states ordered by city id
    dbquery = """
    SELECT cities.id, cities.name, states.name
    FROM cities
    JOIN states ON cities.state_id = states.id
    ORDER BY id ASC;
    """
    cursor.execute(dbquery)

    # Fetch all rows from the result set
    rows = cursor.fetchall()

    # Display the results
    for row in rows:
        print(row)

    # close the cursor and db connection
    cursor.close()
    db.close()
