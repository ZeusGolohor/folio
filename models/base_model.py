#!/usr/bin/env python3
"""
A script that contains the base model for application
"""
from datetime import datetime
import uuid


class BaseModel:
    """
    A class that represents the base model
    """
    def __init__(self, *args, **kwargs):
        """
        Initialization of the base model
        """
        if kwargs:
             for key, value in kwargs.items():
                if key != "__class__":
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.utcnow()
            self.updated_at = self.created_at

    def __str__(self):
        """
        A string representation of the base model
        """
        return "[{:s}] ({:s}) {}".format(self.__class__.__name__, self.id,
                                         self.__dict__)
    
    def to_dict(self):
        """
        A method to convert class attributes to a dictionary
        """
        pass