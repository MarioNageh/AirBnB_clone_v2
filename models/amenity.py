#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base, ExtendedBase


class Amenity(BaseModel, Base, ExtendedBase):
    name = ""
