#!/usr/bin/python3
"""
This module contains unit tests for the BaseModel class.
"""
import os
import unittest
import uuid
from models.base_model import BaseModel
from datetime import datetime


class TestBaseModel(unittest.TestCase):
    """
    This class contains unit tests for the BaseModel class.
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.test_name = "BaseModel"
        self.test_class = BaseModel

    def setUp(self):
        pass

    def tearDown(self):
        try:
            os.remove("file.json")
        except Exception:
            pass

    def test_created_at(self):
        """
        Test if 'created_at' attribute is a datetime and is less than or equal
        to the current datetime.
        """
        b = self.test_class()
        n = datetime.now()
        self.assertIsInstance(b.created_at, datetime)
        self.assertTrue(b.created_at <= n)

    def test_updated_at(self):
        """
        Test if 'updated_at' attribute is a datetime and changes upon update.
        """
        b = self.test_class()
        b.updated_at = datetime.now()
        storage = b.updated_at
        self.assertIsInstance(b.updated_at, datetime)
        b.updated_at = datetime.now()
        self.assertNotEqual(b.updated_at, storage)

    def test_str(self):
        """
        Test the __str__ method's output format.
        """
        b = self.test_class()
        self.assertEqual(str(b), "[{}] ({}) {}".format(
            b.__class__.__name__, b.id, b.__dict__))

    def test_id(self):
        """
        Test if 'id' attribute is a string (UUID).
        """
        b = self.test_class()
        self.assertIsInstance(b.id, str)
        # Test if the ID is a valid UUID
        self.assertTrue(uuid.UUID(b.id, version=4))

    def test_to_dict(self):
        """
        Test if the 'to_dict' method returns a dictionary representation
        of the instance.
        """
        b = self.test_class()
        b_dict = b.to_dict()
        self.assertEqual(b.to_dict(), b_dict)

    def test_save(self):
        """
        Test if 'save' method updates 'updated_at' and
        adds the instance to storage.
        """
        b = self.test_class()
        b.save()
        key = "{}.{}".format(b.__class__.__name__, b.id)
        self.assertIn(key, models.storage.all())
