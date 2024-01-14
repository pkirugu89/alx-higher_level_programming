#!/usr/bin/python3
"""
Script that filters all states based on state name
from hbtn_0e_0_usa db.
"""

import MySQLdb
import sys

if __name__ == "__main__":
    # check if the correct number of args is provided
    if len(sys.argv) != 5:
        print("\
                Usage: {} <username> <password> \
                <database> <state_name>".format(sys.argv[0]))
        sys.exit(1)

    # extract arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]
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
    # Execute the SQL query to select states ordered by id
    dbquery2 = "\
            SELECT * FROM states WHERE name \
            LIKE BINARY '{}' ORDER BY id ASC;".format(state_name)
    cursor.execute(dbquery2)

    # Fetch all rows from the result set
    rows = cursor.fetchall()

    # Display the results
    for row in rows:
        print(row)

    # close the cursor and db connection
    cursor.close()
    db.close()
