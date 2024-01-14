#!/usr/bin/python3
"""
Script that prints all City objs from  the database hbtn_0e_14_usa
"""

import sys
from model_state import Base, State
from model_city import Base, City
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

if __name__ == "__main__":
    # Check if the correct number of arguments is provided
    if len(sys.argv) != 4:
        print("\
                Usage: {} <username> <password> \
                <database>".format(sys.argv[0]))
        sys.exit(1)

    # Extract arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Connect to the MySQL server
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        username,
        password,
        database),
        pool_pre_ping=True
        )

    # Create a session
    session = Session(engine)

    # Query all City Objs
    cities = session.query(City, State).join(State).order_by(City.id).all()
    # Display the cities by state
    for city, state in cities:
        print("{}: ({}) {}".format(state.name, city.id, city.name))

    # Close the session
    session.close()
