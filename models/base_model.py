#!/usr/bin/python3
"""
Base Model module for all models
"""
import uuid
from datetime import datetime


class BaseModel:
    """Base model class
    Public instance attributes:
        id (str): Unique ID for each BaseModel instance.
        created_at (datetime): Datetime when the instance is created.
        updated_at (datetime): Datetime when the instance is updated.

    Public instance methods:
        save(self): Updates the public instance attribute 'updated_at' with the current datetime.
        to_dict(self): Returns a dictionary containing all instance attributes in a serialized format.
    """
    id = str(uuid.uuid4())
    created_at = datetime.now()
    updated_at = datetime.now()

    def __init__(self, *args, **kwargs):
        """ Initialize a new instance of BaseModel.

        Args:
            *args: Variable length argument list (not used in this implementation).
            **kwargs: Arbitrary keyword arguments to initialize instance attributes.
                      If the class is called with keyword arguments, it sets the corresponding
                      attributes with the provided values.
                      Otherwise, it generates new values for 'id', 'created_at', and 'updated_at'.

        Attributes:
            id (str): Unique ID for each BaseModel instance.
            created_at (datetime): Datetime when the instance is created.
            updated_at (datetime): Datetime when the instance is updated.
        """
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

    def __str__(self):
        """
        Returns a string representation of the instance.

        Returns:
            str: String representation in the format:
                 "[<class name>] (<self.id>) <self.__dict__>"
        """
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)
    
    def save(self):
        """
        Updates updated_at with current time when instance is changed
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        Returns a dictionary representation of the instance.

        Returns:
            dict: Dictionary containing all instance attributes in a serialized format.
                  The 'created_at' and 'updated_at' attributes are converted to ISO format strings.
        """
        my_dict = self.__dict__.copy()
        my_dict['__class__'] = self.__class__.__name__
        my_dict['created_at'] = self.created_at.isoformat()
        my_dict['updated_at'] = self.updated_at.isoformat()
        return my_dict
