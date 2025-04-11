#!/usr/bin/python3
"""
Prints all City.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City

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

    # Make a join between State and City.
    results = session.query(State.name, City.id, City.name).join(
        City).order_by(City.id).all()

    for state_name, city_id, city_name in results:
        print(f"{state_name}: ({city_id}) {city_name}")

    # Close session
    session.close()
