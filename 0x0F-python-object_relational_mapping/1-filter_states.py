#!/usr/bin/python3
"""
SQL script that list all states filtered based on 'N'
from hbtn_0e_0_usa db.
"""

import MySQLdb
import sys

if __name__ == "__main__":
    # check if the correct number of args are provided
    if len(sys.argv) != 4:
        print("Usage: {} <username> <password> <database>".format(sys.argv[0]))
        sys.exit(1)

    # Extract arguments
    username, password, database = sys.argv[1], sys.argv[2], sys.argv[3]
    # Connect to the MYSQL server
    db = MySQLdb.connect(
        host="localhost",
        user=username,
        passwd=password,
        db=database,
        port=3306
    )
    # Create a cursor obj to interact with the db
    cursor = db.cursor()
    # query statement
    query1 = "SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC"
    # Execute the above SQL Query.
    cursor.execute(query1)
    # Fetch all the rows from the result set
    rows = cursor.fetchall()
    # Display all the results
    for row in rows:
        print(row)

    # Close the cursor and db connection
    cursor.close()
    db.close()
