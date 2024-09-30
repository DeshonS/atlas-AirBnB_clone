#!/usr/bin/python3
"""File Storage Class"""
import json
import os


class FileStorage:
    __file_path = "file.json"
    __objects = {}
    
    def all(self):
        return self.__objects
    
    def new(self, obj):
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj
        
    def save(self):
        with open(self.__file_path, 'w') as file:
            obj_dict = {key: obj.to_dict() for key, obj in self.__objects.items()}
            json.dump(obj_dict, file)
            
    def reload(self):
        if os.path.exists(self.__file_path):
            with open(self.__file_path, 'r') as file:
                obj_dict = json.load(file)
                from models.base_model import BaseModel
                for key, val in obj_dict.items():
                    cls = val['__class__']
                    if cls == 'BaseModel':
                        self.__objects[key] = BaseModel(**val)
                    if cls == 'User':
                        from models.user import User
                        self.__objects[key] = User(**val)
                    if cls == 'City':
                        from models.city import City
                        self.__objects[key] = City(**val)
                    if cls == 'State':
                        from models.state import State
                        self.__objects[key] = State(**val)
                    if cls == 'Amenity':
                        from models.amenity import Amenity
                        self.__objects[key] = Amenity(**val)
                    if cls == 'Place':
                        from models.place import Place
                        self.__objects[key] = Place(**val)
                    if cls == 'Review':
                        from models.review import Review
                        self.__objects[key] = Review(**val)