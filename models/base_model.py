#!/usr/bin/python3
# -*- coding: utf-8 -*-

from datetime import datetime
import models
import uuid


class BaseModel:
    id(str)

    def __init__(self, *args, **kwargs):
        if kwargs:
            for arg, value in kwargs.items():
                if arg in ("created_at", "updated_at"):
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")

                if arg != '__class__':
                    setattr(self, arg, value)
            else:
                self.id = str(uuid.uuid4())
                self.created_at = datetime.now()
                self.updated_at = datetime.now()
                models.storage.new(self)

    def __str__(self):
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        new_dict = self.__dict__.copy()
        new_dict["__class__"] = self.__class__.__name__
        new_dict["created_at"] = self.created_at.isoformat()
        new_dict["updated_at"] = self.updated_at.isoformat()
        return new_dict
