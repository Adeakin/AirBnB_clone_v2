#!/usr/bin/python3
"""Create a unique storage instance for the application."""
from os import getenv
from models.engine.file_storage import FileStorage
from models.engine.db_storage import DBStorage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


storage_type = getenv("HBNB_TYPE_STORAGE", "fs")
storage = DBStorage() if storage_type == "db" else FileStorage()
storage.reload()
