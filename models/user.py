#!/usr/bin/python3
"""This is the user class"""
from models.base_model import BaseModel
from sqlalchemy import Column, String
from models.review import Review
from sqlalchemy.orm import relationship
from models.base_model import Base
from sqlalchemy import Column, Integer, String, ForeignKey
from os import getenv
import models


storage_type = getenv("HBNB_TYPE_STORAGE")


class User(BaseModel, Base):
    """This is the class for user
    Attributes:
        email: email address
        password: password for you login
        first_name: first name
        last_name: last name
    """
    __tablename__ = 'users'
    if storage_type == 'db':
        email = Column(String(128), nullable=False)
        password = Column(String(128), nullable=False)
        first_name = Column(String(128), nullable=True)
        last_name = Column(String(128), nullable=True)
        places = relationship(
            'Place', cascade="delete", backref="users")
        reviews = relationship(
            "Review", backref="user")
    else:
        email = ""
        password = ""
        first_name = ""
        last_name = ""

    def __init__(self, *args, **kwargs):
        """initializes user"""
        super().__init__(*args, **kwargs)
