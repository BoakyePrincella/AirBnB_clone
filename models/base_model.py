#!/usr/bin/python3
""" This is the base module of the AirBnB project """


import uuid
from datetime import datetime


class BaseModel:
    """ The BaseModel class """
    def __init__(self):
        """ The initialisation method """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """ The string representation """
        return ("[{}] ({}) {}"
                .format(self.__class__.__name__, self.id, self.__dict__))

    def save(self):
        """ The save method """
        self.updated_at = datetime.now()

    def to_dict(self):
        """ Returns dictionary after the instance is called """
        dictionary = dict(self.__dict__)
        dictionary["__class__"] = self.__class__.__name__
        dictionary["created_at"] = self.created_at.isoformat()
        dictionary["updated_at"] = self.updated_at.isoformat()
        return dictionary
