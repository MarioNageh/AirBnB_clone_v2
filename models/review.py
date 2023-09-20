#!/usr/bin/python3
""" Review module for the HBNB project """
from models.base_model import BaseModel, ExtendedBase, Base
from models.base_model import BaseModel, Base, ExtendedBase
from sqlalchemy import Column, String, DateTime,ForeignKey

class Review(BaseModel, Base, ExtendedBase):
    """ Review classto store review information """
    __tablename__ = 'reviews'
    place_id = Column(String(60), ForeignKey('places.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    text = Column(String(1024), nullable=False)
