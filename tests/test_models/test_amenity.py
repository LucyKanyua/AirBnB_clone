#!/usr/bin/python3
"""
This module contains unit tests for the Amenity class.
"""
from models.amenity import Amenity
from tests.test_models.test_base_model import TestBaseModel


class TestAmenity(TestBaseModel):
    """
    This class contains unit tests for the Amenity class.
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.test_name = "Amenity"
        self.test_class = Amenity

    def test_amenity(self):
        """
        Test if 'name' attribute is a string.
        """
        a = self.test_class()
        self.assertIsInstance(a.name, str)
