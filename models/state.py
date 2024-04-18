#!/usr/bin/python3
"""Define the State class."""
from sqlalchemy import Column, String
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """State class representing different states.

    Attributes:
        name (str): The name of the state.
        cities (relationship): Relationship with the City class.
    """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship("City", cascade='all, delete, delete-orphan', backref="state")
