#!/usr/bin/python3
"""
This module contains unit tests to ensure PEP 8 compliance
for the different modules in the project.
"""
import pep8
import unittest
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class Testpep8(unittest.TestCase):
    """
    This class contains unit tests to ensure PEP 8 compliance
    for the different modules in the project.
    """

    def test_pep8_file_storage(self):
        """
        Test if the file_storage module follows PEP 8 coding style.

        Raises:
            AssertionError: If the module does not follow PEP 8 coding style.
        """
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(['models/engine/file_storage.py'])
        self.assertEqual(p.total_errors, 0, "fix pep8")

    def test_pep8_base_model(self):
        """
        Test if the base_model module follows PEP 8 coding style.

        Raises:
            AssertionError: If the module does not follow PEP 8 coding style.
        """
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(['models/base_model.py'])
        self.assertEqual(p.total_errors, 0, "fix pep8")

    def test_pep8_console(self):
        """
        Test if the console module follows PEP 8 coding style.

        Raises:
            AssertionError: If the module does not follow PEP 8 coding style.
        """
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(['console.py'])
        self.assertEqual(p.total_errors, 0, "fix pep8")

    def test_pep8_init(self):
        """
        Test if the __init__ module follows PEP 8 coding style.

        Raises:
            AssertionError: If the module does not follow PEP 8 coding style.
        """
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(['models/__init__.py'])
        self.assertEqual(p.total_errors, 0, "fix pep8")

    def test_pep8_user(self):
        """
        Test if the user module follows PEP 8 coding style.

        Raises:
            AssertionError: If the module does not follow PEP 8 coding style.
        """
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(['models/user.py'])
        self.assertEqual(p.total_errors, 0, "fix pep8")

    def test_pep8_state(self):
        """
        Test if the state module follows PEP 8 coding style.

        Raises:
            AssertionError: If the module does not follow PEP 8 coding style.
        """
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(['models/state.py'])
        self.assertEqual(p.total_errors, 0, "fix pep8")

    def test_pep8_city(self):
        """
        Test if the city module follows PEP 8 coding style.

        Raises:
            AssertionError: If the module does not follow PEP 8 coding style.
        """
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(['models/city.py'])
        self.assertEqual(p.total_errors, 0, "fix pep8")

    def test_pep8_place(self):
        """
        Test if the place module follows PEP 8 coding style.

        Raises:
            AssertionError: If the module does not follow PEP 8 coding style.
        """
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(['models/place.py'])
        self.assertEqual(p.total_errors, 0, "fix pep8")

    def test_pep8_amenity(self):
        """
        Test if the amenity module follows PEP 8 coding style.

        Raises:
            AssertionError: If the module does not follow PEP 8 coding style.
        """
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(['models/amenity.py'])
        self.assertEqual(p.total_errors, 0, "fix pep8")

    def test_pep8_review(self):
        """
        Test if the review module follows PEP 8 coding style.

        Raises:
            AssertionError: If the module does not follow PEP 8 coding style.
        """
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(['models/review.py'])
        self.assertEqual(p.total_errors, 0, "fix pep8")
