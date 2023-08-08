#!/usr/bin/python3

from datetime import datetime
import uuid


class BaseModel:
	id = str(uuid.uuid4())
	created_at = datetime.now()
	updated_at = datetime.now()

	def __init__(self, *args, **kwargs):
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
		return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

	def save(self):
		self.updated_at = datetime.now()

	def to_dict(self):
		new_dict = self.__dict__.copy()
		new_dict['__class__'] = self.__class__.__name__
		new_dict['created_at'] = self.created_at.isoformat()
		new_dict['updated_at'] = self.updated_at.isoformat()
		return new_dict
