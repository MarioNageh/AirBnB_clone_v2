#!/usr/bin/python3
""" Review module for the HBNB project """
from models.base_model import BaseModel


class Review(BaseModel, Base, ExtendedBase):
    """ Review classto store review information """
    place_id = ""
    user_id = ""
    text = ""
