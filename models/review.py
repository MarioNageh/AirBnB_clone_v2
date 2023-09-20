#!/usr/bin/python3
""" Review module for the HBNB project """
from models.base_model import BaseModel, ExtendedBase, Base
from models.base_model import BaseModel, Base, ExtendedBase
from sqlalchemy import Column, String, DateTime,ForeignKey

class Review(BaseModel):
    """ Review classto store review information """
    __tablename__ = 'reviews'
    place_id = ""
    user_id = ""
    text = ""
