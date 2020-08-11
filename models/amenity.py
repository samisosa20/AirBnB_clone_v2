#!/usr/bin/python3
"""This is the state class"""
from models.base_model import BaseModel, Base
from os import getenv


class Amenity(BaseModel, Base):
    """This is the class for State
    Attributes:
        name: input name
    """
    __tablename__ = 'amenitys'
    if getenv("HBNB_TYPE_STORAGE") != 'db':
        name = ""
