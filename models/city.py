#!/usr/bin/python3
""" City Module for HBNB project """
from sqlalchemy import Column, String, DateTime,ForeignKey
from sqlalchemy.orm import relationship

from models.base_model import BaseModel, Base, ExtendedBase


class City(BaseModel, Base,ExtendedBase):
    """ The city class, contains state ID and name """
    __tablename__ = 'cities'
    state_id = Column(String(60), ForeignKey('states.id'),
                      nullable=False)
    name = Column(String(128), nullable=False)
    plases = relationship("Place", backref='cities',cascade="delete")