#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from models.review import Review
from sqlalchemy import Column, String, Integer, Float, ForeignKey
from sqlalchemy.orm import relationship
from os import getenv


class Place(BaseModel, Base):
    """ A place class with a declarative mapping """

    # DB storage implementation for review
    if getenv('HBNB_TYPE_STORAGE') == 'db':
        __tablename__ = 'places'

        city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
        user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
        name = Column(String(128), nullable=False)
        description = Column(String(1024), nullable=False)
        number_rooms = Column(Integer, nullable=False, default=0)
        number_bathrooms = Column(Integer, nullable=False, default=0)
        max_guest = Column(Integer, nullable=False, default=0)
        price_by_night = Column(Integer, nullable=False, default=0)
        latitude = Column(Float, nullable=False, default=0.0)
        longitude = Column(Float, nullable=False, default=0.0)
        amenity_ids = []
        reviews = relationship('Review', backref='place',
                               cascade='all, delete, delete-orphan')
    else:
        name = ""
        city_id = ""
        user_id = ""
        description = ""
        number_rooms = 0
        number_bathrooms = 0
        max_guest = 0
        price_by_night = 0
        latitude = 0.0
        longitude = 0.0
        amenity_ids = ""

        @property
        def reviews(self):
            """File storage implementation for review"""
            all_reviews = models.storage.all(Review)
            review_list = []
            for review in all_reviews.values():
                if review.place_id == self.id:
                    review_list.append(review)
            return review_list
