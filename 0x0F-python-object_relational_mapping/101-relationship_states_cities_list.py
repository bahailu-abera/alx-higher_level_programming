#!/usr/bin/python3
"""
Module to list all 'States'
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from relationship_state import Base, State
from relationship_city import City


def main():
    """
    Main method
    """
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}".
                           format(sys.argv[1],
                                  sys.argv[2],
                                  sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)

    # Create a Session instance
    with Session() as session:
        # query all the State objects and print them in ascending order by id
        states = session.query(State).order_by(State.id).all()
        for state in states:
            print("{}: {}".format(state.id, state.name))
            for city in state.cities:
                print("\t{}: {}".format(city.id, city.name))


if __name__ == "__main__":
    main()
