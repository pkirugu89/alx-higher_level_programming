#!/usr/bin/python3
"""
Script that filters all cities of a specifi state
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
    dbquery5 = """
    SELECT GROUP_CONCAT(cities.name ORDER BY cities.id ASC SEPARATOR ', ')
    FROM cities
    JOIN states ON cities.state_id = states.id
    WHERE states.name LIKE BINARY %s;
    """
    cursor.execute(dbquery5, (state_name,))

    # Fetch the result
    result = cursor.fetchone()

    # Display the result
    if result and result[0]:
        print(result[0])
    else:
        print()

    # close the cursor and db connection
    cursor.close()
    db.close()
