#!/usr/bin/python3
"""
File Storage Class

all - returns the dictionary __objects

new - puts new object in __objects with key <obj class name>.id

save - serializes __objects to JSON file (path: __file_path)

reload - deserializes JSON file to __objects if file exists
"""
import json
import os


class FileStorage:
    """
    initialize filestorage

    __file_path - path to JSON file

    __objects - empty dictionary
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        return self.__objects

    def new(self, obj):
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        with open(self.__file_path, 'w') as file:
            obj_dict = {key: obj.to_dict() for
                        key, obj in self.__objects.items()}
            json.dump(obj_dict, file)

    def reload(self):
        from models.base_model import BaseModel
        from models.user import User
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.place import Place
        from models.review import Review
        if os.path.exists(self.__file_path):
            try:
                with open(self.__file_path, 'r') as file:
                    obj_dict = json.load(file)

                    classes = {'BaseModel': BaseModel,
                               'User': User,
                               'State': State,
                               'City': City,
                               'Amenity': Amenity,
                               'Place': Place,
                               'Review': Review
                               }

                    for key, val in obj_dict.items():
                        cls_name = val['__class__']
                        cls = classes.get(cls_name)
                        if cls:
                            self.__objects[key] = cls(**val)
            except Exception as e:
                print(f"Error loading from {self.__file_path}: {e}")
