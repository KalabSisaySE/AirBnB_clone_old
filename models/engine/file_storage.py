#!/usr/bin/python3
"""the `file_storage` module
defines a class `FileStorage`
"""
import json
import os
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


class FileStorage:
    """ serializes instances to a JSON file and deserializes \
         JSON file to instances"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns the dictionary that contains all the objects stored"""
        return type(self).__objects

    def new(self, obj):
        """sets in the dictionary with the obj with key <obj class name>.id

        Args:
            obj (object): the object to be added to the dictionary
        """
        key = str(type(obj).__name__) + '.' + obj.id
        type(self).__objects.update({key: obj})

    def save(self):
        """serializes the dictionary to the JSON file"""
        json_objects = {}
        for key in type(self).__objects:
            json_objects.update({key: type(self).__objects[key].to_dict()})
        with open(type(self).__file_path, "w") as f:
            f.write(json.dumps(json_objects))

    def reload(self):
        """deserializes the JSON file to the dictionary"""
        if os.path.exists(type(self).__file_path):
            with open(type(self).__file_path, "r") as f:
                # retrieve the dict from the json
                x = json.loads(f.read())

                # recreate the object based on the dict
                # store it in __objects
                for key in x:
                    obj = eval(x[key]['__class__'])(**x[key])
                    type(self).__objects.update({key: obj})
