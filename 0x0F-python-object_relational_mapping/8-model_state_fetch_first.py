#!/usr/bin/python3
"""
Module to list first state
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

        # query the first State object and print id and name of the state
        state = session.query(State).filter_by(id=1).first()
        if state:
            print("{}: {}".format(state.id, state.name))
        else:
            print("Nothing")


if __name__ == "__main__":
    main()
