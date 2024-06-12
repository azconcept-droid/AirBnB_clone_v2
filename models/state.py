#!/usr/bin/python3
""" State Module for HBNB project """

from models.base_model import BaseModel, Base
from models.city import City
import models
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String


class State(BaseModel, Base):
    """ State class """

    # DB storage type implementation
    if models.db == 'db':

        __tablename__ = 'states'

        name = Column(String(128), nullable=False)
        cities = relationship('City', backref='state',
                              cascade='all, delete, delete-orphan')
    else:
        name = ""

    if models.db != 'db':
        @property
        def cities(self):
            """Getter for list city related to state"""
            all_cities = models.storage.all(City)
            cities_list = []
            for city in all_cities.values():
                if city.state_id == self.id:
                    cities_list.append(city)
            return cities_list
