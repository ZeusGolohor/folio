#!/usr/bin/env python3
"""
A script to manager users
"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer


class User(BaseModel, Base):
    """
    A class to represent a user
    """
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    email = Column(String(250), nullable=False)
    hashed_password = Column(String(250), nullable=False)
    session_id = Column(String(250))
    reset_token = Column(String(250))

    def __init__(self, email: str, hashed_password: str) -> None:
        """
        A user to initailize a user.
        """
        self.email = email
        self.hashed_password = hashed_password


    def __repr__(self):
        return f"<User(id={self.id}, email={self.email})>"