#!/usr/bin/python3
"""
This module contains unit tests for the Review class.
"""
from models.review import Review
from tests.test_models.test_base_model import TestBaseModel
from datetime import datetime
import uuid
import models


class TestReview(TestBaseModel):
    """
    This class contains unit tests for the Review class.
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.test_name = "Review"
        self.test_class = Review

    def test_review_id(self):
        """
        Test if 'id' attribute is a string (UUID).
        """
        r = self.test_class()
        self.assertIsInstance(r.id, str)
        # Test if the ID is a valid UUID
        self.assertTrue(uuid.UUID(r.id, version=4))

    def test_user_id(self):
        """
        Test if 'user_id' attribute is a string.
        """
        r = self.test_class()
        self.assertIsInstance(r.user_id, str)

    def test_place_id(self):
        """
        Test if 'place_id' attribute is a string.
        """
        r = self.test_class()
        self.assertIsInstance(r.place_id, str)

    def test_text(self):
        """
        Test if 'text' attribute is a string.
        """
        r = self.test_class()
        self.assertIsInstance(r.text, str)

    def test_created_at(self):
        """
        Test if 'created_at' attribute is a datetime.
        """
        r = self.test_class()
        self.assertIsInstance(r.created_at, datetime)

    def test_updated_at(self):
        """
        Test if 'updated_at' attribute is a datetime and changes upon update.
        """
        r = self.test_class()
        r.updated_at = datetime.now()
        storage = r.updated_at
        self.assertIsInstance(r.updated_at, datetime)
        r.updated_at = datetime.now()
        self.assertNotEqual(r.updated_at, storage)

    def test_to_dict(self):
        """
        Test if the 'to_dict' method returns a dictionary representation
        of the instance.
        """
        r = self.test_class()
        r_dict = r.to_dict()
        self.assertEqual(r.to_dict(), r_dict)

    def test_save(self):
        """
        Test if 'save' method updates 'updated_at' and adds the instance
        to storage.
        """
        r = self.test_class()
        r.save()
        key = "{}.{}".format(r.__class__.__name__, r.id)
        self.assertIn(key, models.storage.all())
