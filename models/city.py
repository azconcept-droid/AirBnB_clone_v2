#!/usr/bin/python3
""" City Module for HBNB project """

import models
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship


class City(BaseModel, Base):
    """ The city class, contains state ID and name,
    with a declarative mapping to cities table
    """

    if models.db == 'db':
        __tablename__ = 'cities'

        state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
        name = Column(String(128), nullable=False)
        places = relationship('Place', backref='cities',
                            cascade='all, delete, delete-orphan')
    else:
        name = ""
        state_id = ""

    def __init__(self, *args, **kwargs):
        """initializes City"""
        super().__init__(*args, **kwargs)
