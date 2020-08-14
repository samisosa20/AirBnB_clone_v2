#!/usr/bin/python3
"""This is the state class"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, ForeignKey, Float, Table
from sqlalchemy.orm import relationship
from os import getenv
import models


class Place(BaseModel, Base):
    """This is the class for Place
    Attributes:
        city_id: city id
        user_id: user id
        name: name input
        description: string of description
        number_rooms: number of room in int
        number_bathrooms: number of bathrooms in int
        max_guest: maximum guest in int
        price_by_night:: pice for a staying in int
        latitude: latitude in flaot
        longitude: longitude in float
        amenity_ids: list of Amenity ids
    """
    if getenv("HBNB_TYPE_STORAGE") == 'db':
        __tablename__ = 'places'
        city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
        user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
        name = Column(String(128), nullable=False)
        description = Column(String(1024), nullable=True)
        number_rooms = Column(Integer, nullable=False, default=0)
        number_bathrooms = Column(Integer, nullable=False, default=0)
        max_guest = Column(Integer, nullable=False, default=0)
        price_by_night = Column(Integer, nullable=False, default=0)
        latitude = Column(Float, nullable=True)
        longitude = Column(Float, nullable=True)
        reviews = relationship("Review", backref="place")
        place_amenity = Table(
            'place_amenity', Base.metadata,
            Column(
                'place_id', String(60), ForeignKey('places.id'),
                nullable=False, primary_key=True
            ),
            Column(
                'amenity_id', String(60), ForeignKey('amenities.id'),
                nullable=False, primary_key=True
            )

        )
        amenities = relationship("Amenity", secondary="place_amenity",
                                 back_populates="place_amenities",
                                 viewonly=False)
    else:
        city_id = ""
        user_id = ""
        name = ""
        description = ""
        number_rooms = 0
        number_bathrooms = 0
        max_guest = 0
        price_by_night = 0
        latitude = 0.0
        longitude = 0.0
        amenity_ids = []

        @property
        def reviews(self):
            """Get reviews"""
            list_reviews = []
            all_reviews = models.storage.all(Review)
            for key, review_obj in all_reviews.items():
                if review_obj.place_id == self.id:
                    list_reviews.append(city_obj)
            return list_reviews

        @property
        def amenities(self):
            """get for amenities"""
            list_amenities = []
            all_amenities = models.storage.all(Amenities)
            for key, ameniti_obj in all_amenities.items():
                if ameniti_obj.id in self.amenity_ids:
                    list_amenities.append(ameniti_obj)
            return list_amenities

        @amenities.setter
        def amenities(self, obj):
            """Set amenities"""
            if isinstance(obj, Amenity):
                self.amenity_ids.append(obj.id)
