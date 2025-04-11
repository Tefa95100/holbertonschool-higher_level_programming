#!/usr/bin/python3
"""
Prints the id of a State object.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
import re

if __name__ == "__main__":

    username, password, db_name, state_name = sys.argv[1:5]
    # Remove all quotes
    state_name = re.sub(r"^['\"]+|['\"]+$", "", state_name)

    # Create engine and bind it to the database
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
            username, password, db_name
        ),
        pool_pre_ping=True
    )

    # Create a configured "Session" class and a session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query states with the letter 'a'
    states_a = session.query(State).filter(State.name == state_name).first()

    if state:
        print(state.id)
    else:
        print("Not found")
