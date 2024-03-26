#!/usr/bin/python3
"""Unit test for the FileStorage class."""

import unittest
import json
import os
from models import storage
from models.base_model import BaseModel
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from models.engine.file_storage import FileStorage

class TestFileStorage(unittest.TestCase):
    """Test cases for the FileStorage class."""
    
    def setUp(self):
        """Set up method called before each test."""
        self.storage = FileStorage()
        self.file_path = FileStorage._FileStorage__file_path

    def tearDown(self):
        """Tear down method called after each test."""
        if os.path.exists(self.file_path):
            os.remove(self.file_path)

    def test_all_returns_dict(self):
        """Test that all returns the __objects dict."""
        self.assertIsInstance(self.storage.all(), dict)

    def test_new_method(self):
        """Test adding new object to storage."""
        original_len = len(self.storage.all())
        obj = BaseModel()
        self.storage.new(obj)
        self.assertEqual(len(self.storage.all()), original_len + 1)

    def test_save_method(self):
        """Test saving objects to file."""
        obj = BaseModel()
        self.storage.new(obj)
        self.storage.save()
        self.assertTrue(os.path.exists(self.file_path))
        with open(self.file_path, 'r') as f:
            objs = json.load(f)
        self.assertIn(f"BaseModel.{obj.id}", objs)

    def test_reload_method(self):
        """Test reloading objects from file."""
        obj = BaseModel()
        obj_id = obj.id
        self.storage.new(obj)
        self.storage.save()
        self.storage.reload()
        objs = self.storage.all()
        self.assertIn(f"BaseModel.{obj_id}", objs)

    def test_reload_with_no_file(self):
        """Test reloading with no file present."""
        if os.path.exists(self.file_path):
            os.remove(self.file_path)
        try:
            self.storage.reload()
            self.assertTrue(True)
        except Exception:
            self.fail("reload() raised an exception with no file present.")

if __name__ == '__main__':
    unittest.main()
