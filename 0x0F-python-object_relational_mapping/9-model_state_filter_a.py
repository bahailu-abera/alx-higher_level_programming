#!/usr/bin/python3
"""
Module to list all 'States' that contains letter 'a'
"""
import sys
from model_state import Base, State

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


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

        # query all the State objects that contains letter 'a'
        # and print them in ascending order by id
        for state in session.query(State).order_by(State.id).filter(
                State.name.like("%a%")):
            print("{}: {}".format(state.id, state.name))


if __name__ == "__main__":
    main()
