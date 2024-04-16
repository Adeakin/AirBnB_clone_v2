#!/usr/bin/python3
""" File storage class
"""

import json
from models.base_model import BaseModel
from models.state import State
from models.city import City
from models.user import User
from models.place import Place
from models.review import Review
from models.amenity import Amenity
from os import path

class FileStorage:
    """ File storage class """
    __file_path = "file.json"
    __objects = {}

    def all(self, cls=None):
        """
        Returns the list of objects of one type of class.
        """
        if cls is None:
            return self.__objects

        return {k: v for k, v in self.__objects.items() if isinstance(v, cls)}

    def new(self, obj):
        """ Sets in __objects the obj with key <obj class name>.id
        """
        FileStorage.__objects["{}.{}".format(obj.__class__.__name__, obj.id)] = obj

    def save(self):
        """ Serializes __objects to the JSON file (path: __file_path)
        """
        obj_dict = {}
        for key, value in FileStorage.__objects.items():
            obj_dict[key] = value.to_dict()
        with open(FileStorage.__file_path, mode="w", encoding="utf-8") as f:
            json.dump(obj_dict, f)

    def reload(self):
        """ Deserializes the JSON file to __objects
        """
        if path.exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, mode="r", encoding="utf-8") as f:
                obj_dict = json.load(f)
                for key, value in obj_dict.items():
                    cls_name, obj_id = key.split('.')
                    cls = eval(cls_name)
                    obj = cls(**value)
                    FileStorage.__objects[key] = obj

    def delete(self, obj=None):
        """
        Deletes obj from __objects if it's inside.
        If obj is equal to None, the method should not do anything.
        """
        if obj is not None:
            key = "{}.{}".format(type(obj).__name__, obj.id)
            if key in self.__objects:
                del self.__objects[key]
