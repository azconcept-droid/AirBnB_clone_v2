#!/usr/bin/python3
"""This module instantiates an object of class FileStorage and DBStorage"""

from models.engine.file_storage import FileStorage
from os import getenv

db = getenv('HBNB_TYPE_STORAGE')
try:
    if db == 'db':
        from .engine.db_storage import DBStorage
        storage = DBStorage()
        storage.reload()
except Exception:
    storage = FileStorage()
    storage.reload()
