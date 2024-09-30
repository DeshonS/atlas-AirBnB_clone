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