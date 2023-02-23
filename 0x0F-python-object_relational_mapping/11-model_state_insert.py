#!/usr/bin/python3
"""
Module for inserting new rows to database
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

    # create new state
    louisiana = State(name="Louisiana")

    print(louisiana.id)

    # Create a Session instance
    with Session() as session:
        session.add(louisiana)
        session.commit()
        print(louisiana.id)


if __name__ == "__main__":
    main()
