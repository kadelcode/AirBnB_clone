#!/usr/bin/python3
""" A State class that inherits from BaseModel """
from  models.base_model import BaseModel


class State(BaseModel):
    """ Defines a State class

        Public class attribute:
            name (str): The name of the State.
    """
    name = ""
