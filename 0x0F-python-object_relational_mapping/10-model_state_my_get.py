#!/usr/bin/python3
"""
Module for get a state
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from model_state import Base, State


def main():
    """
    Main method
    """
    state_name = sys.argv[4]
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}".
                           format(sys.argv[1],
                                  sys.argv[2],
                                  sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)

    # Createa a session instance
    with Session() as session:
        state = session.query(State).filter_by(name=state_name).first()
        if state:
            print(state.id)
        else:
            print("Not found")


if __name__ == "__main__":
    main()
