#!/usr/bin/python3
"""
Module responsible for handling file-based data storage
and retrieval for models.
"""

from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review
from os.path import exists
import json


class FileStorage:
    """
    This class manages file-based data storage and
    retrieval for model instances.

    Attributes:
        __file_path (str): The path to the JSON file used for data storage.
        __objects (dict): A dictionary that holds instances of model classes
        indexed by class name and instance ID.
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        Retrieve all stored objects.

        Returns:
            dict: A dictionary containing all stored instances
            indexed by class name and instance ID.
        """
        return self.__objects

    def new(self, obj):
        """
        Add a new object to the storage.

        Args:
            obj: An instance of a model class.
        """
        key = obj.__class__.__name__ + "." + obj.id
        self.__objects[key] = obj

    def save(self):
        """
        Save objects to the JSON file.

        This method serializes the stored objects and
        writes them to the JSON file.
        """
        dictionary = {}
        for key, value in self.__objects.items():
            dictionary[key] = value.to_dict()
        with open(self.__file_path, "w", encoding="utf-8") as f:
            f.write(json.dumps(dictionary))

    def reload(self):
        """
        Load objects from the JSON file.

        This method deserializes objects from the JSON file
        and populates the storage dictionary.
        """
        if exists(self.__file_path):
            with open(self.__file_path, "r", encoding="utf-8") as f:
                dictionary = json.loads(f.read())
                for key, value in dictionary.items():
                    self.__objects[key] = eval(value["__class__"])(**value)
