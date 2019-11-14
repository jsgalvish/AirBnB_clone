#!/usr/bin/python3

"""
 BaseModel class.
"""

import models
from uuid import uuid4
from datetime import datetime


class BaseModel():
    """BaseModel class"""

    def __init__(self, *args, **kwargs):
        """initialize"""
        if kwargs:
            for k, v in kwargs.items():
                if k == "created_at" or k == "updated_at":
                    setattr(self, k, datetime.strptime(
                        v, "%Y-%m-%dT%H:%M:%S.%f"))
                elif k == "__class__":
                    continue
                else:
                    setattr(self, k, v)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.utcnow()
            self.updated_at = datetime.utcnow()
            models.storage.new(self)

    def __str__(self):
        """print"""
        cls_name = self.__class__.__name__
        return "[{}] ({}) {}".format(cls_name, self.id, self.__dict__)

    def save(self):
        """save"""
        self.updated_at = datetime.utcnow()
        models.storage.save()

    def to_dict(self):
        """dictionary"""
        d = {}
        for k, v in self.__dict__.items():
            if k == "created_at" or k == "updated_at":
                d[k] = datetime.isoformat(v)
            else:
                d[k] = v
        d["__class__"] = self.__class__.__name__
        return d
