#!/usr/bin/python3
"""
First state Model
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from relationship_city import Base


class State(Base):
    """
    State model for states table
    """
    __tablename__ = "states"
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state", cascade="all, delete")
