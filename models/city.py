#!/usr/bin/env python3
"""
This module defines the City class,
representing a city in the application.
"""
from models.base_model import BaseModel


class City(BaseModel):
    """
    This class represents a city within the application.

    Attributes:
        id (str): A unique identifier for the City.
        created_at (datetime): The datetime when the City was created.
        updated_at (datetime): The datetime when the City was last updated.
        state_id (str): The ID of the state associated with the city.
        name (str): The name of the city.
    """

    state_id = ""
    name = ""
