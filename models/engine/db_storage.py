#!/usr/bin/python3
"""This module defines a class to manage db storage for hbnb clone"""

from os import getenv
from models.base_model import BaseModel, Base
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session


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

        # Delete all tables in test environment
        if env == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Returns all cls obj currently in db storage"""

        all_cls_obj = {}
        if cls:
            # Querying a specific class
            cls_objs = self.__session.query(cls).all()
            for cls_obj in cls_objs:
                key = '{}.{}'.format(cls_obj.__class__.__name__, cls_obj.id)
                all_cls_obj[key] = cls_obj
            return all_cls_obj
        # Querying all classes
        classes = [User, Place, State, City, Amenity, Review]
        for _class in classes:
            all_obj = self.__session.query(_class).all()
            for obj in all_obj:
                key = '{}.{}'.format(obj.__class__.__name__, obj.id)
                all_cls_obj[key] = obj
        return all_cls_obj

    def new(self, obj):
        """Adds new object to current db session"""
        self.__session.add(obj)

    def save(self):
        """Saves all changes of the current db session"""
        self.__session.commit()

    def reload(self):
        """Loads table from db storage and persist db session"""

        Base.metadata.create_all(self.__engine)

        session_thread = sessionmaker(bind=self.__engine,
                                      expire_on_commit=False)
        Session = scoped_session(session_factory=session_thread)
        self.__session = Session()

    def delete(self, obj=None):
        """ Delete obj from current db session """

        if obj is not None:
            self.__session.delete(obj)
