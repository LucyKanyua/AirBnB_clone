#!/usr/bin/python3
"""
Initialization module for the models package.

This module initializes the models package by
creating an instance of the FileStorage class
and loading stored data into memory.
The FileStorage instance, named 'storage', serves as the
interface for data management and retrieval throughout the application.

Attributes:
    storage (FileStorage): An instance of the FileStorage class
    responsible for managing data storage
    and retrieval for the models package.
"""

from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
