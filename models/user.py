#!/usr/bin/python3
"""This module contains a class that inherits from BaseModel"""

from models.base_model import BaseModel


class User(BaseModel):
    """The user class that inherits from BaseModel"""
    email = ""
    password = ""
    firstname = ""
    last_name = ""
