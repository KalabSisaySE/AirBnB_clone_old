#!/usr/bin/python3
"""Unittest for base_model([..])
"""
import unittest
from models.base_model import BaseModel
from uuid import uuid4
from datetime import datetime
from models import storage


class TestBaseModelInstantitation(unittest.TestCase):
    """test the instantiation of `BaseModel` object"""

    def test_no_args(self):
        """test instantiation with no args"""
        my_bm = BaseModel()
        self.assertIsInstance(my_bm, BaseModel)

    def test_kwargs_instantiation(self):
        """test instantiation with a dict"""
        my_dict = {
            'id': str(uuid4()),
            'created_at': datetime.now(),
            'updated_at': datetime.now(),
            'school': "ALX"
        }
        my_bm = BaseModel(**my_dict)
        self.assertEqual(my_bm.id, my_dict['id'])
        self.assertEqual(my_bm.created_at, my_dict['created_at'])
        self.assertEqual(my_bm.updated_at, my_dict['updated_at'])
        self.assertEqual(my_bm.school, my_dict['school'])

    def test_new_instance_saved_in_storage(self):
        """test if the instance is saved in the file_storage"""
        my_bm = BaseModel()

        # test if the new object is now found in the storage
        self.assertIn(my_bm, storage.all().values())


class TestBaseModelStr(unittest.TestCase):
    """tests the __str__ method of `BaseModel`"""

    def test_return_type(self):
        """test the return type of __str__"""
        my_bm = BaseModel()

        # test if __str__ returns a string
        self.assertIsInstance(my_bm.__str__(), str)

    def test_return_format(self):
        """test the return value of __str__"""
        my_dict = {
            'id': str(uuid4()),
            'created_at': datetime.now(),
            'updated_at': datetime.now(),
            'school': "ALX"
        }

        my_bm = BaseModel(**my_dict)

        my_str = "[BaseModel] ({}) {}".format(my_dict['id'], my_dict)

        # test if __str__ returns the right format
        self.assertEqual(my_bm.__str__(), my_str)


class TestBaseModelSave(unittest.TestCase):
    """unittests for the save method of `BaseModel`"""

    def test_save(self):
        """test if the object will be save to the storage"""

        my_bm = BaseModel()
        my_bm.save()

        with open("file.json", "r") as f:
            self.assertIn(my_bm.id, f.read())


class TestBaseModelToDict(unittest.TestCase):
    """test the `to_dict` method of `BaseModel`"""

    def test_to_dict_return_type(self):
        """test if to_dict returns dict"""
        my_bm = BaseModel()
        self.assertIsInstance(my_bm.to_dict(), dict)

    def test_to_dict_return(self):
        """test the return value of to_dict"""
        my_dict = {
            'id': str(uuid4()),
            'created_at': datetime.now().isoformat(),
            'updated_at': datetime.now().isoformat(),
            'school': "ALX"
        }

        my_bm = BaseModel(**my_dict)
        my_dict.update({'__class__': "BaseModel"})
        self.assertEqual(my_bm.to_dict(), my_dict)


if __name__ == "__main__":
    unittest.main()
