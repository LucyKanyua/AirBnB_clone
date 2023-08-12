#!/usr/bin/python3
"""
This module contains unit tests for the User class.
"""
from models.user import User
from tests.test_models.test_base_model import TestBaseModel


class TestUser(TestBaseModel):
    """
    This class contains unit tests for the User class.
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.test_name = "User"
        self.test_class = User

    def test_firstName(self):
        """
        Test if 'first_name' attribute is initialized as an empty string.
        """
        u = self.test_class()
        self.assertEqual(u.first_name, "")

    def test_lastName(self):
        """
        Test if 'last_name' attribute is initialized as an empty string.
        """
        u = self.test_class()
        self.assertEqual(u.last_name, "")

    def test_email(self):
        """
        Test if 'email' attribute is initialized as an empty string.
        """
        u = self.test_class()
        self.assertEqual(u.email, "")

    def test_password(self):
        """
        Test if 'password' attribute is initialized as an empty string.
        """
        u = self.test_class()
        self.assertEqual(u.password, "")
