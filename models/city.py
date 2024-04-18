#!/usr/bin/python3
"""Define the City class."""
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base
from models.place import Place


class City(BaseModel, Base):
    """City class representing different cities.

    Attributes:
        name (str): The name of the city.
        state_id (str): The state id of the city.
        places (relationship): Relationship with the Place class.
    """
    __tablename__ = "cities"
    name = Column(String(128), nullable=False)
    state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
    places = relationship("Place", cascade='all, delete, delete-orphan', backref="cities")
