#!/urs/bin/python3
""" A BaseModel class """
from uuid import uuid4
from datetime import datatime


class BaseModel:
    """ Defines all common attributes/methods for other classes """

    def __init__(self, *args, **kwargs):
        """ Initialize a new BaseModel

        Args:
            *args (any): Unused
            **kwargs (dict): Key/value pairs of attributes
        """
        self.id = str(uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()
        tform = "%Y-%m-%dT%H:%M:%S.%f"
