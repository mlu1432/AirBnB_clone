#!/usr/bin/python3
"""This is the review module"""

from models.base_model import BaseModel


class Review(BaseModel):
    """This is the review class"""
    place_id = ""
    user = ""
    text = ""

    def __init__(self, *args, **kwargs):
        """This is the __init__ method"""
        super().__init__(*args, **kwargs)
