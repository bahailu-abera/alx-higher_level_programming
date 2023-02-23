#!/usr/bin/python3
"""
Module for deleting states that contains letter 'a'
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from model_state import Base, State


def main():
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}".
                           format(sys.argv[1],
                                  sys.argv[2],
                                  sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)

    # Create a Session instance
    with Session() as session:
        for state in session.query(State).filter(State.name.like("%a%")).all():
            session.delete(state)
        session.commit()


if __name__ == "__main__":
    main()
