#!/usr/bin/python3
"""
First state Model
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

# Define the base class
Base = declarative_base()


class State(Base):
    """
    State model for states table
    """
    __tablename__ = "states"
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
