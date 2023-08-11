#!/usr/bin/env python3
"""
Models Review Class
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """
    class Review inherits from BaseModel
    """
    place_id = ""
    user_id = ""
    text = ""
