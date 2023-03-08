#!/usr/bin/python3
"""The FileStorage class"""
import json

class FileStorage:
    """ Represent an abstracted storage engine

    Attributes:
        __file_path (str): The name of the file to save objects to
        __objects (dict): A dictionary of instantiated objects
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ Return the dictionary __objects. """
        return FileStorage.__objects
