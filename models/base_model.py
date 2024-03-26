#!/usr/bin/python3
"""Defines the BaseModel class."""
import uuid
from dateutil import parser
from datetime import datetime, timezone

class BaseModel:
    """Defines all common attributes/methods for other classes."""

    def __init__(self, *args, **kwargs):
        """Initializes a new BaseModel instance."""
        if kwargs:
            for key, value in kwargs.items():
                if key in ['created_at', 'updated_at']:
                    value = parser.parse(value)
                if key != '__class__':
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = self.updated_at = datetime.now()
        
    def __str__(self):
        """Returns the string representation of the BaseModel instance."""
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """Updates the public instance attribute updated_at with the current datetime."""
        self.updated_at = datetime.now()
        # Delayed import and use of storage
        from models import storage
        storage.save()

    def to_dict(self):
        """Returns a dictionary containing all keys/values of the instance."""
        dictionary = self.__dict__.copy()
        dictionary['__class__'] = self.__class__.__name__
        dictionary['created_at'] = self.created_at.isoformat()
        dictionary['updated_at'] = self.updated_at.isoformat()
        return dictionary

    def _register_instance(self):
        """Registers the instance in storage."""
        from models import storage
        storage.new(self)
