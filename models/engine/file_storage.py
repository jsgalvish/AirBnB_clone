#!/usr/bin/python3

import json
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State

classes = {"BaseModel": BaseModel, "User": User, "Amenity": Amenity,
           "City": City, "Place": Place, "Review": Review, "State": State}


class FileStorage:

    __file_path = "file.json"
    __objects = {}

    def all(self):
        return self.__objects

    def new(self, obj):
        if obj is not None:
            key = obj.__class__.__name__ + "." + obj.id
            self.__objects[key] = obj

    def save(self):
        j__objects = {}
        for key in self.__objects:
            j__objects[key] = self.__objects[key].to_dict()
        with open(self.__file_path, 'w') as __file:
            json.dump(j__objects, __file)

    def reload(self):
        try:
            with open(self.__file_path, 'r') as __file:
                j__objects = json.load(__file)
            for key in j__objects:
                self.__objects[key] = classes[j__objects[key]
                                              ["__class__"]](**j__objects[key])
        except Exception as e:
            pass
