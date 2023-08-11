#!/usr/bin/python3

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
        __file_path = "file.json"
        __objects = {}

        def all(self):
                return self.__objects

        def new(self, obj):
                key = obj.__class__.__name__ + "." + obj.id
                self.__objects[key] = obj

        def save(self):
            dictionary = {}
            for key, value in self.__objects.items():
                dictionary[key] = value.to_dict()
            with open(self.__file_path, "w", encoding="utf-8") as f:
                f.write(json.dumps(dictionary))

        def reload(self):
            if exists(self.__file_path):
                with open(self.__file_path, "r", encoding="utf-8") as f:
                    dictionary = json.loads(f.read())
                    for key, value in dictionary.items():
                        self.__objects[key] = eval(value["__class__"])(**value)
