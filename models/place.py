#!/usr/bin/python3
""" Place Module for HBNB project """
from os import getenv

from models.base_model import BaseModel, ExtendedBase, Base
from sqlalchemy import Column, String, DateTime, ForeignKey, Integer, Float
from sqlalchemy.orm import relationship


class Place(BaseModel, Base, ExtendedBase):
    """ A place to stay """
    __tablename__ = 'places'

    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024))
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float)
    longitude = Column(Float)
    amenity_ids = []

    reviews = relationship('Review', backref='place', cascade='delete')

    if getenv('HBNB_TYPE_STORAGE') != 'db':
        @property
        def reviews(self):
            """get linked reviews"""
            reviews_list = []
            for review in self.reviews:
                if review.place_id == self.id:
                    reviews_list.append(review)
            return reviews_list