import unittest
import models.amenity
from models.base_model import BaseModel
from os import getenv
from unittest.mock import patch
from datetime import datetime, timedelta
from time import sleep
import pycodestyle


class TestAmenity(unittest.TestCase):
    """Test cases for the Amenity class"""

    def test_is_subclass(self):
        """Test that Amenity is a subclass of BaseModel"""
        amenity = models.amenity.Amenity()
        self.assertIsInstance(amenity, BaseModel)
        self.assertTrue(hasattr(amenity, "id"))
        self.assertTrue(hasattr(amenity, "created_at"))
        self.assertTrue(hasattr(amenity, "updated_at"))

    def test_name_attr(self):
        """Test that Amenity has attribute name"""
        amenity = models.amenity.Amenity()
        self.assertTrue(hasattr(amenity, "name"))
        if getenv("HBNB_TYPE_STORAGE") == 'db':
            self.assertIsNone(amenity.name)
        else:
            self.assertEqual(amenity.name, "")

    def test_to_dict_creates_dict(self):
        """Test that to_dict method creates a dictionary with proper attributes"""
        am = models.amenity.Amenity()
        new_d = am.to_dict()
        self.assertEqual(type(new_d), dict)
        self.assertNotIn("_sa_instance_state", new_d)
        for attr in am.__dict__:
            if attr != "_sa_instance_state":
                self.assertIn(attr, new_d)
        self.assertIn("__class__", new_d)

    def test_to_dict_values(self):
        """Test that values in dict returned from to_dict are correct"""
        t_format = "%Y-%m-%dT%H:%M:%S.%f"
        am = models.amenity.Amenity()
        new_d = am.to_dict()
        self.assertEqual(new_d["__class__"], "Amenity")
        self.assertIsInstance(new_d["created_at"], str)
        self.assertIsInstance(new_d["updated_at"], str)
        self.assertEqual(new_d["created_at"], am.created_at.strftime(t_format))
        self.assertEqual(new_d["updated_at"], am.updated_at.strftime(t_format))

    def test_str(self):
        """Test that the str method has the correct output"""
        amenity = models.amenity.Amenity()
        string = "[Amenity] ({}) {}".format(amenity.id, amenity.__dict__)
        self.assertEqual(string, str(amenity))

    def test_name_type(self):
        """Test that the name attribute of Amenity is of type string"""
        amenity = models.amenity.Amenity()
        self.assertIsInstance(amenity.name, str)


class TestAmenityMethods(unittest.TestCase):
    """Test cases for additional Amenity methods"""

    def test_init(self):
        """Test the initialization of Amenity"""
        amenity = models.amenity.Amenity()
        self.assertIsNone(amenity.name)

    def test_init_params(self):
        """Test the initialization of Amenity with parameters"""
        amenity = models.amenity.Amenity(name="Pool")
        self.assertEqual(amenity.name, "Pool")
