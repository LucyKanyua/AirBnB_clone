#!/usr/bin/python3
"""
This module defines the BaseModel class, which serves as
the foundation for all models in the application.

Classes:
    BaseModel: The base model for all other models.
"""

import uuid
from datetime import datetime


class BaseModel:
    """
    This class represents the base model for all other models
    in the application. It provides common attributes
    and methods that are inherited by specific model classes.

    Attributes:
        id (str): The unique identifier for the instance.
        created_at (datetime): The creation timestamp.
        updated_at (datetime): The last update timestamp.

    Methods:
        __init__(self, *args, **kwargs): Initialize a new instance.
        __str__(self): Return a human-readable string representation.
        save(self): Update timestamps and save to storage.
        to_dict(self): Convert instance to a dictionary.
    """

    def __init__(self, *args, **kwargs):
        """
        Initialize a new instance of the BaseModel class.

        Args:
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.
                If provided, the instance attributes are set based
                on these arguments.
                If not provided, default values are set,
                and the instance is registered with
                the storage system.
        """
        import models

        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                if key != "__class__":
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """
        Return a human-readable string representation of
        the BaseModel instance.

        Returns:
            str: A formatted string containing the class name,
            instance id, and attribute dictionary.
        """
        return "[{}] ({}) {}".format(
                self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """
        Update the 'updated_at' attribute with the current datetime
        and trigger the saving of the instance to the storage system.
        """
        import models

        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        Convert the BaseModel instance to a dictionary representation.

        Returns:
            dict: A dictionary containing instance attributes
            along with metadata.
        """
        my_dict = self.__dict__.copy()
        my_dict["__class__"] = self.__class__.__name__
        my_dict["created_at"] = self.created_at.isoformat()
        my_dict["updated_at"] = self.updated_at.isoformat()
        return my_dict
