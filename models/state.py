#!/usr/bin/python3
""" State Module for HBNB project """

from models.base_model import BaseModel, Base
from models.city import City
from models import storage
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String
from os import getenv


class State(BaseModel, Base):
    """ State class """

    __table__ = 'states'

    name = Column(String(128), nullable=False)

    # DB storage type implementation
    if getenv('HBNB_TYPE_STORAGE') == 'db':
        cities = relationship('City', backref='states',
                              cascade='all, delete, delete-orphan')
    else:
        @property
        def cities(self):
            """File storage type implementation"""
            all_cities = storage.all(City)
            cities_list = []
            for city in all_cities.values():
                if city.state_id == self.id:
                    cities_list.append(city)
            return cities_list
