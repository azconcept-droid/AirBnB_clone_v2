#!/usr/bin/python3
"""This module defines a class to manage db storage for hbnb clone"""

import json
from os import getenv
from models.base_model import BaseModel, Base
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine, Column, String, Datetime


class DBStorage:
    """This class manages db storage of hbnb models in JSON format"""
    __engine = None
    __session = None

    def __init__(self):
        """initialize db storage class"""
        # Get the environmental variables
        user = getenv('HBNB_MYSL_USER')
        passwd = getenv('HBNB_MYSQL_PWD')
        host = getenv('HBNB_MYSQL_HOST', 'localhost')
        db = getenv('HBNB_MYSQL_DB')
        env = getenv('HBNB_ENV')

        url = 'mysql+mysqldb://{}:{}@{}/{}'.format(user, passwd, host, db)
        self.__engine = create_engine(url, pool_pre_ping=True)
        Base.metadata.create_all(self.__engine)

        # Delete all tables in test mode
        if env == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Returns a dictionary of models currently in db storage"""
        Session = sessionmaker(bind=self.__engine)
        self.__session = Session()
        if cls:
            # Querying
            cls_obj = self.__session.query(cls).all()
        all_obj = self.__session.query(
            User, Place, State, City, Amenity, Review).all()

    def new(self, obj):
        """Adds new object to storage dictionary"""
        self.all().update({obj.to_dict()['__class__'] + '.' + obj.id: obj})

    def save(self):
        """Saves storage dictionary to file"""
        pass

    def reload(self):
        """Loads storage dictionary from file"""
        from models.base_model import BaseModel
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review

        classes = {
                    'BaseModel': BaseModel, 'User': User, 'Place': Place,
                    'State': State, 'City': City, 'Amenity': Amenity,
                    'Review': Review
                  }
        try:
            temp = {}
            with open(FileStorage.__file_path, 'r') as f:
                temp = json.load(f)
                for key, val in temp.items():
                    self.all()[key] = classes[val['__class__']](**val)
        except FileNotFoundError:
            pass

    def delete(self, obj=None):
        """ Delete obj from __objects """

        if obj is not None:
            key = "{}.{}".format(obj.__class__.__name__, obj.id)

            if key in FileStorage.__objects:
                del FileStorage.__objects[key]

            self.save()
