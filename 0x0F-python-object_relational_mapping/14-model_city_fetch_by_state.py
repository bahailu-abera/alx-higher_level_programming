#!/usr/bin/python3
"""
Script that lists all City objects from the database
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from model_state import Base, State
from model_city import City


def main():
    # Create an engine to the database
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)

    # Create a configured "Session" class
    Session = sessionmaker(bind=engine)

    # Create a Session object
    with Session() as session:
        # Query all City objects from the database, sorted by id
        cities = session.query(City).order_by(City.id).all()

        # Print the results in the desired format
        for city in cities:
            state = session.query(State).filter_by(id=city.state_id).first()
            print("{}: ({}) {}".format(state.name, city.id, city.name))


if __name__ == "__main__":
    main()
