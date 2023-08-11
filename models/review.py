#!/usr/bin/env python3
"""
This module defines the Review class,
representing a review of a place in the application.
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """
    This class represents a review of a place in the application.

    Attributes:
        id (str): A unique identifier for the Review.
        created_at (datetime): The datetime when the Review was created.
        updated_at (datetime): The datetime when the Review was last updated.
        place_id (str): The ID of the place being reviewed.
        user_id (str): The ID of the user who wrote the review.
        text (str): The text of the review.
    """
    place_id = ""
    user_id = ""
    text = ""
