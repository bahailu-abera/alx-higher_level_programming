#!/usr/bin/python3
"""
Module creating state and cities and reletes them
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

    # Createa a session instance
    with Session() as session:
        # Create California state
        california = State(name="California")

        # Create San Francisco city
        new_city = City(name="San Francisco", state=california)
        session.add(new_city)
        session.commit()


if __name__ == "__main__":
    main()
