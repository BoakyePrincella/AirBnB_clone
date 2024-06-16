#!/usr/bin/python3
""" The test for the BaseModel class """

import unittest
import uuid
from models.base_model import BaseModel

class TestBaseModel_Istantiation(unittest.TestCase):
    """ The test for BaseModel Instantiation """

    def test_instance(self):
        new_instance = BaseModel()

        self.assertIsInstance(new_instance, BaseModel)


if __name__ == '__main__':
    unittest.main()
