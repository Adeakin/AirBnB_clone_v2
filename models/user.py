#!/usr/bin/python3
"""Define the User class."""
from sqlalchemy import Column, String
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship


class User(BaseModel, Base):
    """User class representing users.

    Attributes:
        email (str): The email address of the user.
        password (str): The password for user login.
        first_name (str): The first name of the user.
        last_name (str): The last name of the user.
        places (relationship): Relationship with the Place class.
        reviews (relationship): Relationship with the Review class.
    """
    __tablename__ = "users"
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128))
    last_name = Column(String(128))
    places = relationship("Place", cascade='all, delete, delete-orphan', backref="user")
    reviews = relationship("Review", cascade='all, delete, delete-orphan', backref="user")
