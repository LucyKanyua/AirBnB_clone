#!/usr/bin/env python3
"""
This module defines the State class,
representing a state in the application.
"""
from models.base_model import BaseModel


class State(BaseModel):
    """
    This class represents a state within the application.

    Attributes:
        id (str): A unique identifier for the State.
        created_at (datetime): The datetime when the State was created.
        updated_at (datetime): The datetime when the State was last updated.
        name (str): The name of the state.
    """
    name = ""
