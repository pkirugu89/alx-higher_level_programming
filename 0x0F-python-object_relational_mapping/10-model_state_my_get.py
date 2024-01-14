#!/usr/bin/python3
"""
Script that prints the state obj with the name passed as an argument
from the database hbtn_0e_6_usa
"""

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

if __name__ == "__main__":
    # Check if the correct number of arguments is provided
    if len(sys.argv) != 5:
        print("\
                Usage: {} <username> <password> \
                <database> <state_name>".format(sys.argv[0]))
        sys.exit(1)

    # Extract arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    # Connect to the MySQL server
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        username,
        password,
        database),
        pool_pre_ping=True
        )

    # Create a session
    session = Session(engine)

    # Search for the State obj with provided name
    state = session.query(State).filter_by(name=state_name).first()
    if state:
        print(state.id)
    else:
        print("Not found")

    # Close the session
    session.close()
