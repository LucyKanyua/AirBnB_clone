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

    def test_all(self):
        """Test if the 'all' method returns the __objects attribute"""
        obj = self.test_class()
        objects = obj.all()
        self.assertEqual(objects, obj._FileStorage__objects)
        mod_key = "ExtraObject"
        obj._FileStorage__objects[mod_key] = BaseModel()
        obj._FileStorage__objects[mod_key].save()
        mod_objs = obj.all()
        del obj._FileStorage__objects[mod_key]
        self.assertEqual(mod_objs, obj._FileStorage__objects)

    def test_new(self):
        """Test if the 'new' method adds an object to __objects"""
        obj = self.test_class()
        new_obj = BaseModel()
        obj.new(new_obj)
        self.assertIn("BaseModel." + new_obj.id, obj._FileStorage__objects)

    def test_reload(self):
        """Test if the 'reload' method reloads __objects from file"""
        obj = self.test_class()
        new_obj = BaseModel()
        obj.new(new_obj)
        obj.save()
        obj.reload()
        self.assertIn("BaseModel." + new_obj.id, obj._FileStorage__objects)
        empty_obj = self.test_class()
        empty_obj.save()
        new_empty = self.test_class()
        new_empty._FileStorage__file_path = "empty.json"
        new_empty.reload()
        self.assertNotEqual(len(new_empty._FileStorage__objects), 1)
