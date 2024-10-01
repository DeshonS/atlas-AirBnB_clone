#!/usr/bin/python3
"""
BaseModel Class

__init__ - initializes BaseModel class with keyword args or a new instance

__str__ - returns a string representation of an instance

save - updates updated_at with the current datetime and saves the instance

to_dict - returns a dictionary representation of an instance

"""
import uuid
from datetime import datetime
from models import storage


class BaseModel():
    def __init__(self, *args, **kwargs):
        if kwargs:
            for key, val in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    setattr(self, key, datetime.fromisoformat(val))
                elif key != '__class__':
                    setattr(self, key, val)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            storage.new(self)

    def __str__(self):
        """Returns a string representation of an instance"""
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """
        Saves inst to updates updated_at atribute with current date/time
        """
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """converts an instance to a dictionary"""
        instance_dict = self.__dict__.copy()
        instance_dict["__class__"] = self.__class__.__name__
        instance_dict["created_at"] = self.created_at.isoformat()
        instance_dict["id"] = self.id
        instance_dict["updated_at"] = self.updated_at.isoformat()
        return instance_dict
