#!/usr/bin/python3
"""This is the file storage class for AirBnB"""
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    """Class for serializing instances to a JSON file and deserializing JSON file to instances."""

    __file_path = "file.json"
    __objects = {}

    def all(self, cls=None):
        """Return dictionary of all objects or objects of a specific class."""
        if cls:
            return {k: v for k, v in self.__objects.items() if isinstance(v, cls)}
        return self.__objects

    def new(self, obj):
        """Add a new object to the storage."""
        key = "{}.{}".format(type(obj).__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """Serialize objects to JSON file."""
        serialized = {k: v.to_dict() for k, v in self.__objects.items()}
        with open(self.__file_path, 'w') as f:
            json.dump(serialized, f)

    def reload(self):
        """Deserialize objects from JSON file."""
        try:
            with open(self.__file_path, 'r') as f:
                data = json.load(f)
                for k, v in data.items():
                    cls_name = v["__class__"]
                    obj = eval(cls_name)(**v)
                    self.__objects[k] = obj
        except FileNotFoundError:
            pass

    def delete(self, obj=None):
        """Delete an object from storage."""
        if obj:
            key = "{}.{}".format(type(obj).__name__, obj.id)
            del self.__objects[key]

    def close(self):
        """Reload objects."""
        self.reload()
