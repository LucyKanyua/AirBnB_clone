#!/usr/bin/python3
"""
This module contains unit tests for the FileStorage class.
"""
import os
import unittest
import models
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel


class TestFileStorage(unittest.TestCase):
    """
    This class contains unit tests for the FileStorage class.
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.test_class = FileStorage

    def test_pathname(self):
        """
        Test if 'file_path' attribute is a string.
        """
        p = self.test_class()
        self.assertIsInstance(p._FileStorage__file_path, str)

    def test_objects(self):
        """
        Test if '__objects' attribute is a dictionary.
        """
        obj = self.test_class()
        self.assertIsInstance(obj._FileStorage__objects, dict)

    def test_save(self):
        """
        Test if 'save' method creates the file 'file.json'.
        """
        models.storage.save()
        self.assertTrue(os.path.exists("file.json"))

    def tearDown(self):
        """
        Remove 'file.json' after each test.
        """
        try:
            os.remove("file.json")
        except Exception:
            pass

    def test_file_empty(self):
        """
        Test if 'save' method correctly writes data to 'file.json'.
        """
        b = BaseModel()
        new_dict = b.to_dict()
        b.save()
        b2 = BaseModel(**new_dict)
        self.assertFalse(os.stat("file.json").st_size == 0)
