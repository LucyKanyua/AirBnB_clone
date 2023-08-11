#!/usr/bin/env python3
"""
This module defines the Amenity class, which represents an amenity offered
by properties in the application.
"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """
    This class represents an amenity offered by properties in the application.

    Attributes:
        id (str): A unique identifier for the Amenity.
        created_at (datetime): The datetime when the Amenity was created.
        updated_at (datetime): The datetime when the Amenity was last updated.
        name (str): The name of the amenity.
    """

    name = ""
