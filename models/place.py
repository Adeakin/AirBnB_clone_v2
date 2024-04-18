#!/usr/bin/python3
"""Define the Place class."""
from os import getenv
from sqlalchemy import Column, String, Integer, Float, ForeignKey, Table
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base
from models.review import Review
from models.amenity import Amenity
import models


place_amenity = Table(
    "place_amenity", Base.metadata,
    Column("place_id", String(60), ForeignKey("places.id"), primary_key=True, nullable=False),
    Column("amenity_id", String(60), ForeignKey("amenities.id"), primary_key=True, nullable=False)
)


class Place(BaseModel, Base):
    """Place class representing different places.

    Attributes:
        city_id (str): The city id of the place.
        user_id (str): The user id of the place.
        name (str): The name of the place.
        description (str): The description of the place.
        number_rooms (int): The number of rooms in the place.
        number_bathrooms (int): The number of bathrooms in the place.
        max_guest (int): The maximum guest capacity of the place.
        price_by_night (int): The price per night for the place.
        latitude (float): The latitude coordinate of the place.
        longitude (float): The longitude coordinate of the place.
        reviews (relationship): Relationship with the Review class.
        amenities (relationship): Relationship with the Amenity class.
    """
    __tablename__ = "places"
    city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024))
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float)
    longitude = Column(Float)

    if getenv("HBNB_TYPE_STORAGE") == "db":
        reviews = relationship("Review", cascade='all, delete, delete-orphan', backref="place")
        amenities = relationship("Amenity", secondary=place_amenity, viewonly=False, back_populates="place_amenities")
    else:
        @property
        def reviews(self):
            """Return list of reviews for the place."""
            return [review for review in models.storage.all(Review).values() if review.place_id == self.id]

        @property
        def amenities(self):
            """Return list of amenities for the place."""
            return [amenity for amenity in models.storage.all(Amenity).values() if amenity.id in self.amenity_ids]

        @amenities.setter
        def amenities(self, obj=None):
            """Append amenity ids to the attribute."""
            if isinstance(obj, Amenity) and obj.id not in self.amenity_ids:
                self.amenity_ids.append(obj.id)
