#!/usr/bin/python3
"""
Lists all State objects from the database.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":

    username, password, db_name = sys.argv[1:4]

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

    # Query all State objects, ordered by id
    states = session.query(State).order_by(State.id).all()

    for state in states:
        print(f"{state.id}: {state.name}")
