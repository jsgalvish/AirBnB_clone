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

classes = {"Amenity": Amenity, "BaseModel": BaseModel, "City": City,
           "Place": Place, "Review": Review, "State": State, "User": User}


class FileStorage():
    """FileStorage class"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns __objects"""
        return self.__objects

    def new(self, obj):
        """new obj"""
        if obj is not None:
            k = obj.__class__.__name__ + "." + obj.id
            self.__objects[k] = obj

    def save(self):
        """save json"""
        json_objects = {}
        for key in self.__objects:
            json_objects[key] = self.__objects[key].to_dict()
        with open(self.__file_path, 'w') as f:
            json.dump(json_objects, f)

    def reload(self):
        """reload json"""
        if path.isfile(self.__file_path):
            with open(self.__file_path, 'r') as f:
                for key, value in json.load(f).items():
                    self.new(classes[value['__class__']](**value))
