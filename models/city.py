#!/usr/bin/python3
"""This is the city model"""

from models.base_model import BaseModel


class City(BaseModel):
    """This is the city class"""
    state_id = ""
    name = ""
    
    def __init__(self, *args, **kwargs):
        """This is the init method"""
        super().__init__(*args, **kwargs)
