#!/urs/bin/python3
""" A BaseModel class """
import models
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

        if len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "created_at" or k == "updated_at":
                    self.__dict__[k] = datetime.strptime(v, tform)
                else:
                    self.__dict__[k] = v
        else:
            models.storage.new(self)
