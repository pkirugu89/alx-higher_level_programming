#!/usr/bin/python3
"""
Script that adds a state obj to the database hbtn_0e_6_usa
"""

import sys
from model_state import Base, State
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

    # Add a new state Object to the db
    new_state = State(name="Lousiana")
    session.add(new_state)
    session.commit()

    # Print the new_state id after insertion
    print(new_state.id)

    # Close the session
    session.close()
