#!/usr/bin/python3
""" Module for User class."""

from models.base_model import BaseModel

class User(BaseModel):
    """A User represents an individual who interacts with the AirBnB clone platform.
    The User has the following attributes:
    Email: The user’s email address.
    Password: The user’s password.
    First Name: The user’s first name.
    Last Name: The user’s last name.
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""


