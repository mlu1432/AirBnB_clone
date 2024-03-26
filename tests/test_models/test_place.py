#!/usr/bin/python3
"""Unit test for the Place class."""

import unittest
from models.place import Place
from datetime import datetime, timezone


class TestPlace(unittest.TestCase):
    """Defines test cases for the Place class."""

    def setUp(self):
        """Method called to prepare the test fixture."""
        self.place = Place()

    def tearDown(self):
        """Method called immediately after the test method has been called and the result recorded."""
        del self.place

    def test_init(self):
        """Test initialization of Place instance."""
        self.assertTrue(hasattr(self.place, "city_id"))
        self.assertTrue(hasattr(self.place, "user_id"))
        self.assertTrue(hasattr(self.place, "name"))
        # Continue for other attributes...

    def test_init_with_kwargs(self):
        """Test initialization with kwargs."""
        attrs = {
            "city_id": "city_id",
            "user_id": "user_id",
            "name": "My lovely place",
            "description": "A lovely place",
            "number_rooms": 4,
            "number_bathrooms": 2,
            "max_guest": 4,
            "price_by_night": 100,
            "latitude": 120.0,
            "longitude": -7.0,
            "amenity_ids": ["amenity_id1", "amenity_id2"]
        }
        place = Place(**attrs)
        for key, value in attrs.items():
            self.assertEqual(getattr(place, key), value)

    def test_str(self):
        """Test the __str__ method for Place."""
        expected_str = f"[Place] ({self.place.id}) {self.place.__dict__}"
        self.assertEqual(str(self.place), expected_str)

    def test_to_dict(self):
        """Test conversion of Place instance to dictionary."""
        self.place.name = "Another place"
        place_dict = self.place.to_dict()
        self.assertEqual(place_dict["__class__"], "Place")
        self.assertEqual(place_dict["name"], "Another place")
        # Ensure datetime attributes are correctly converted to string format
        self.assertIsInstance(place_dict["created_at"], str)
        self.assertIsInstance(place_dict["updated_at"], str)

if __name__ == "__main__":
    unittest.main()