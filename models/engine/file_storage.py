#!/usr/bin/python3
"""FileStorage class"""
from models.base_model import BaseModel
import json
from os import path
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage():
    """File Storage class"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns __objects"""
        return self.__objects

    def new(self, obj):
        """new obj"""
        k = obj.__class__.__name__ + "." + obj.id
        self.__objects[k] = obj

    def save(self):
        """save json"""
        d = {k: v.to_dict()
             for k, v in self.__objects.items()}
        with open(self.__file_path, mode='w') as f:
            json.dump(d, f)

    def reload(self):
        """reload json"""
        if path.isfile(self.__file_path):
            with open(self.__file_path) as f:
                d = json.load(f)
                for k, v in d.items():
                    cls = v["__class__"]
                    self.new(eval(cls)(**v))
    def reset(self):
        """Reset all objects in __objects"""
        self.__objects = {}
