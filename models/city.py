#!/usr/bin/python3
""" City Module for HBNB project """
from sqlalchemy import Column, String, DateTime,ForeignKey

from models.base_model import BaseModel, Base, ExtendedBase


class City(BaseModel, Base,ExtendedBase):
    """ The city class, contains state ID and name """
    __tablename__ = 'cities'
    state_id = Column(String(60), ForeignKey('states.id'),
                      primary_key=True,
                      nullable=False)
    name = Column(String(128), nullable=False)