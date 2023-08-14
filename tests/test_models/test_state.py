#!/usr/bin/python3
"""
This module contains unit tests for the State class.
"""
from models.state import State
from tests.test_models.test_base_model import TestBaseModel


class TestState(TestBaseModel):
    """
    This class contains unit tests for the State class.
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.test_name = "State"
        self.test_class = State

    def test_state_id(self):
        """
        Test if 'id' attribute is a string (UUID).
        """
        s = self.test_class()
        self.assertIsInstance(s.id, str)

    def test_state_name(self):
        """
        Test if 'name' attribute is a string.
        """
        s = self.test_class()
        self.assertIsInstance(s.name, str)
