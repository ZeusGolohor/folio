#!/usr/bin/env python3
"""
A script that contains the base model for application
"""
from datetime import datetime
import uuid
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()

class BaseModel:
    """
    A class that represents the base model
    """
    def __init__(self, *args, **kwargs):
        pass