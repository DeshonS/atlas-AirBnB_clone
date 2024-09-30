#!/usr/bin/python3
"""
BaseModel Class

__init__ - initializes BaseModel class with keyword args or a new instance

__str__ - returns a string representation of an instance

save - updates updated_at with the current datetime and saves the instance

to_dict - returns a dictionary representation of an instance

"""
import uuid                     # universally unique identifier
from datetime import datetime   # date and time
from models import storage      # storage engine

class BaseModel():
    def __init__(self, *args, **kwargs):                                    #only kwargs is used for keywords
        if kwargs:                                                          # if kwargs is not empty
            for key, val in kwargs.items():                                 #for each key, value pair in kwargs
                if key == "created_at" or key == "updated_at":              #if key is created_at or updated_at
                    setattr(self, key, datetime.fromisoformat(val))         #set attribute for key to datetime
                elif key != '__class__':                                    #else if key is not __class__
                    setattr(self, key, val)                                 #set attribute for key to value
        else:
            self.id = str(uuid.uuid4())                                     #generate a unique id
            self.created_at = datetime.now()                                #set created_at to current datetime
            self.updated_at = self.created_at                               #set updated_at to created_at
            storage.new(self)                                               #add instance to storage
        
    def __str__(self):
        """Returns a string representation of an instance"""
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)
    
    def save(self):
        """Saves the instance and updates updated_at attribute with current date and time"""
        self.updated_at = datetime.now()
        storage.save()
        
    def to_dict(self):
        """converts an instance to a dictionary"""
        instance_dict = self.__dict__.copy()
        instance_dict["__class__"] = self.__class__.__name__                #pairs __class__ to class name
        instance_dict["created_at"] = self.created_at.isoformat()           #pairs created_at to to the isoformat of created_at
        instance_dict["updated_at"] = self.updated_at.isoformat()           #pairs updated_at to the isoformat of updated_at
        return instance_dict                                                #return the dictionary