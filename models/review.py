#!/usr/bin/python3
"""This is the state class"""
from models.base_model import BaseModel, Base
from os import getenv


class Review(BaseModel, Base):

    """This is the class for State
    Attributes:
        place_id: The place id
        user_id: The user id
        name: input name
    """
    __tablename__ = 'reviws'
    if getenv("HBNB_TYPE_STORAGE") != 'db':
        place_id = ""
        user_id = ""
        text = ""
