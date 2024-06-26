#!/usr/bin/python3
"""This module instantiates an object of class FileStorage and DBStorage"""

from os import getenv

db = getenv('HBNB_TYPE_STORAGE')

if db == 'db':
    from models.engine.db_storage import DBStorage
    storage = DBStorage()
else:
    from models.engine.file_storage import FileStorage
    storage = FileStorage()
storage.reload()
