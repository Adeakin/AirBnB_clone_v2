#!/usr/bin/python3
"""Define the Review class."""
from sqlalchemy import Column, String, ForeignKey
from models.base_model import BaseModel, Base


class Review(BaseModel, Base):
    """Review class representing different reviews.

    Attributes:
        text (str): The description of the review.
        place_id (str): The place id associated with the review.
        user_id (str): The user id associated with the review.
    """
    __tablename__ = "reviews"
    text = Column(String(1024), nullable=False)
    place_id = Column(String(60), ForeignKey("places.id"), nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
