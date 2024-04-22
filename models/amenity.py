#!/usr/bin/python3
""" Amenity Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String


class Amenity(BaseModel, Base):
    """Amenity class with declarative mapping to amenities table"""

    __tablename__ = 'amenities'

    name = Column(String(128), nullable=False)
    place_amenities = ''
