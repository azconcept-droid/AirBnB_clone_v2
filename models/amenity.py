#!/usr/bin/python3
""" Amenity Module for HBNB project """
import models
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String


class Amenity(BaseModel, Base):
    """Amenity class with declarative mapping to amenities table"""

    if models.db == 'db':

        __tablename__ = 'amenities'

        name = Column(String(128), nullable=False)
        # place_amenities = ''
    else:
        name = ""
