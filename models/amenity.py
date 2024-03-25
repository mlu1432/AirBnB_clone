#!/usr/bin/python3
"""This is the amenity module"""

from models.base_model import BaseModel


class Amenity(BaseModel):
    """This is the amenity class"""
    name = ""

    def __init__(self, *args, **kwargs):
        """This is the __init__ method"""
        super().__init__(*args, **kwargs)
