#!/usr/bin/python3
"""Unittest for file_storage([..])
"""
import unittest
from models.engine.file_storage import FileStorage
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


class TestFileStorageInstantiation(unittest.TestCase):
    """unittests the instantiation of the `FileStorage`"""

    def test_instantiation(self):
        """test `FileStorage` instantiation"""
        fs = FileStorage()
        self.assertIsInstance(fs, FileStorage)


class TestFileStorageAll(unittest.TestCase):
    """unittests for the `all` method"""

    def test_return_type(self):
        """test if `all` returns dictionary"""
        fs = FileStorage()
        self.assertIsInstance(fs.all(), dict)

    def test_returns_str_keys(self):
        """test if the keys in the dict are all strings"""
        fs = FileStorage()
        for key in fs.all().keys():
            self.assertIsInstance(key, str)

    def test_returns_obj_values(self):
        """test if the values in the dict are all objects"""

        objs = [Amenity, BaseModel, City, Place, Review, State, User]
        fs = FileStorage()

        for value in fs.all().values():
            self.assertIn(type(value), objs)


class TestFileStorageNew(unittest.TestCase):
    """unittests for the `new` method"""

    def test_key_format(self):
        """test if `all` saves objects with the right key format"""
        bm = BaseModel()
        key = "BaseModel" + "." + bm.id
        fs = FileStorage()

        self.assertIn(key, fs.all().keys())

    def test_saving_to_objects(self):
        """test if instantiating new object will save it to the dictionary"""
        fs = FileStorage()
        john = User()
        key = "User." + john.id
        self.assertIn(key, fs.all().keys())
        self.assertIn(john, fs.all().values())


class TestFileStorageSave(unittest.TestCase):
    """unittests for the `save` method"""

    def test_saving_to_json(self):
        """test if save method saves it to the json file"""

        AddisAbaba = Place()
        fs = FileStorage()
        fs.save()

        with open('file.json', 'r') as f:
            self.assertIn(AddisAbaba.id, f.read())


if __name__ == "__main__":
    unittest.main()
