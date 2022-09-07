#!/usr/bin/python3
"""The base_model module
defines the class `BaseModel`
"""
import uuid
from datetime import datetime
import models


class BaseModel:
    """defines all common attributes/methods for other classes"""

    def __init__(self, *args, **kwargs):
        """instantiates a `BaseModel` object."""
        if len(kwargs) > 0:
            for key, value in kwargs.items():
                if key != "__class__":
                    setattr(self, key, value)
            if hasattr(self, "created_at") and type(self.created_at) is str:
                self.created_at = datetime.fromisoformat(kwargs['created_at'])
            if hasattr(self, "updated_at") and type(self.updated_at) is str:
                self.updated_at = datetime.fromisoformat(kwargs['updated_at'])
        else:
            self.updated_at = datetime.now()
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """returns the string represenation of the object."""
        return "[{}] ({}) {}".format(type(self).__name__,
                                     self.id,
                                     self.__dict__)

    def save(self):
        """ saves the object to JSON and updates the attribute `updated_at` \
            with the current datetime."""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """returns the dictionary representation of the instance."""
        my_dict = self.__dict__.copy()
        my_dict['created_at'] = self.created_at.isoformat()
        my_dict['updated_at'] = self.updated_at.isoformat()
        my_dict.update({'__class__': self.__class__.__name__})
        return my_dict
