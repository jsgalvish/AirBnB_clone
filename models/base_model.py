#!/usr/bin/python3

from datetime import datetime
import uuid
import models

time = "%Y-%m-%dT%H:%M:%S.%f"


class BaseModel:

    def __init__(self, *args, **kwargs):
        if kwargs:
            for key, value in kwargs.items():
                if key != "__class__":
                    setattr(self, key, value)
            if hasattr(self, "created_at") and type(self.created_at) is str:
                self.created_at = datetime.strptime(kwargs["created_at"], time)
            if hasattr(self, "updated_at") and type(self.updated_at) is str:
                self.updated_at = datetime.strptime(kwargs["updated_at"], time)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            models.storage.new(self)
            models.storage.save()

    def __str__(self):
        return "[{:s}] ({:s}) {}".format(self.__class__.__name__,
                                         self.id, self.__dict__)

    def save(self):
        self.updated_at = datetime.now()

    def to_dict(self):
        n_dict = self.__dict__.copy()
        if "created_at" in n_dict:
            n_dict["created_at"] = n_dict["created_at"].strtime(time)
        if "updated_at" in n_dict:
            n_dict["updated_at"] = n_dict["updated_at"].strtime(time)
        n_dict["__class"] = self.__class__.__name__
        return n_dict
