#!/usr/bin/python3
"""
This module contains unit tests for the City class.
"""
from models.city import City
from tests.test_models.test_base_model import TestBaseModel


class TestCity(TestBaseModel):
    """
    This class contains unit tests for the City class.
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.test_name = "City"
        self.test_class = City

    def test_name(self):
        """
        Test if 'name' attribute is a string.
        """
        c = self.test_class()
        self.assertIsInstance(c.name, str)

    def test_state_id(self):
        """
        Test if 'state_id' attribute is a string.
        """
        c = self.test_class()
        self.assertIsInstance(c.state_id, str)
