#!/usr/bin/python3
"""This is the state module."""

from models.base_model import BaseModel


class State(BaseModel):
    """This is the state class"""
    name = ""

    def __init__(self, *args, **kwargs):
        """This is the __init__ method"""
        super().__init__(*args, **kwargs)
