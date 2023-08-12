#!/usr/bin/python3
"""
This module contains unit tests for verifying classes and inheritance
in the console module.
"""
import unittest
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class TestConsole(unittest.TestCase):
    """
    This class contains unit tests for verifying classes and inheritance
    in the console module.
    """

    def test_class(self):
        """
        Test if instances of classes have the correct class name.

        Raises:
            AssertionError: If any instance's class name does not match
            the expected class name.
        """
        user = User()
        state = State()
        city = City()
        amenity = Amenity()
        place = Place()
        review = Review()
        self.assertEqual(user.__class__.__name__, "User")
        self.assertEqual(state.__class__.__name__, "State")
        self.assertEqual(city.__class__.__name__, "City")
        self.assertEqual(amenity.__class__.__name__, "Amenity")
        self.assertEqual(place.__class__.__name__, "Place")
        self.assertEqual(review.__class__.__name__, "Review")

    def test_inheritance(self):
        """
        Test if instances of classes inherit from BaseModel.

        Raises:
            AssertionError: If any instance's class does not inherit
            from BaseModel.
        """
        user = User()
        state = State()
        city = City()
        amenity = Amenity()
        place = Place()
        review = Review()
        self.assertTrue(issubclass(user.__class__, BaseModel))
        self.assertTrue(issubclass(state.__class__, BaseModel))
        self.assertTrue(issubclass(city.__class__, BaseModel))
        self.assertTrue(issubclass(amenity.__class__, BaseModel))
        self.assertTrue(issubclass(place.__class__, BaseModel))
        self.assertTrue(issubclass(review.__class__, BaseModel))
