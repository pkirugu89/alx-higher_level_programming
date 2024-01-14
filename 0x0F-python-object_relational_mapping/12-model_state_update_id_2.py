#!/usr/bin/python3
"""
Script that updates a state obj to the database hbtn_0e_6_usa
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

    # Query the db to update the State
    update_state = session.query(State).filter_by(id=2).first()
    if update_state:
        update_state.name = "New Mexico"
        session.commit()

    # Close the session
    session.close()
