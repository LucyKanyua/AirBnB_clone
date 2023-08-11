#!/usr/bin/python3
"""
This module defines the User class,
representing a user entity in the application.
"""
from models.base_model import BaseModel


class User(BaseModel):
    """
    This class represents a user in the application.

    Attributes:
        id (str): A unique identifier for the User.
        created_at (datetime): The datetime when the User was created.
        updated_at (datetime): The datetime when the User was last updated.
        email (str): The email address of the user.
        password (str): The password associated with the user's account.
        first_name (str): The user's first name.
        last_name (str): The user's last name.
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
