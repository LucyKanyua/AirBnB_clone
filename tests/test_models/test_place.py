#!/usr/bin/python3
"""
This module contains unit tests for the Place class.
"""
from models.place import Place
from models.base_model import BaseModel
from tests.test_models.test_base_model import TestBaseModel


class TestPlace(TestBaseModel):
    """
    This class contains unit tests for the Place class.
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.test_name = "Place"
        self.test_class = Place

    def test_user_id(self):
        """
        Test if 'user_id' attribute is a string.
        """
        p = self.test_class()
        self.assertIsInstance(p.user_id, str)

    def test_city_id(self):
        """
        Test if 'city_id' attribute is a string.
        """
        p = self.test_class()
        self.assertIsInstance(p.city_id, str)

    def test_city_name(self):
        """
        Test if 'name' attribute is a string.
        """
        p = self.test_class()
        self.assertIsInstance(p.name, str)

    def test_description(self):
        """
        Test if 'description' attribute is a string.
        """
        p = self.test_class()
        self.assertIsInstance(p.description, str)

    def test_number_rooms(self):
        """
        Test if 'number_rooms' attribute is an integer.
        """
        p = self.test_class()
        self.assertIsInstance(p.number_rooms, int)

    def test_number_bathrooms(self):
        """
        Test if 'number_bathrooms' attribute is an integer.
        """
        p = self.test_class()
        self.assertIsInstance(p.number_bathrooms, int)

    def test_max_guest(self):
        """
        Test if 'max_guest' attribute is an integer.
        """
        p = self.test_class()
        self.assertIsInstance(p.max_guest, int)

    def test_price_by_night(self):
        """
        Test if 'price_by_night' attribute is an integer.
        """
        p = self.test_class()
        self.assertIsInstance(p.price_by_night, int)

    def test_latitude(self):
        """
        Test if 'latitude' attribute is a float.
        """
        p = self.test_class()
        self.assertIsInstance(p.latitude, float)

    def test_longitude(self):
        """
        Test if 'longitude' attribute is a float.
        """
        p = self.test_class()
        self.assertIsInstance(p.longitude, float)

    def test_amenity_ids(self):
        """
        Test if 'amenity_ids' attribute is a list.
        """
        p = self.test_class()
        self.assertIsInstance(p.amenity_ids, list)
