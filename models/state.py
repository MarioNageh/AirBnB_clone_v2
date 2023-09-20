#!/usr/bin/python3
""" State Module for HBNB project """

from sqlalchemy import Column, String, DateTime,ForeignKey
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base, ExtendedBase


class State(BaseModel, Base,ExtendedBase):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref='state',cascade="delete")