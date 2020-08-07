#!/usr/bin/python3
"""This is the state class"""
from models.base_model import BaseModel


class Review(BaseModel):
    """This is the class for State
    Attributes:
        place_id: The place id
        user_id: The user id
        name: input name
    """
    place_id = ""
    user_id = ""
    text = ""
