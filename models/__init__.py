#!/usr/bin/python3
""" the `__init__.py` module
connects the file storage to the `BaseModel` module
reloads `objects` from storage everytime the program is executed"""
from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
