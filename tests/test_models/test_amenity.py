import unittest
from models.amenity import Amenity
from datetime import datetime, timezone

#!/usr/bin/python3
"""Unit test for the Amenity class."""


class TestAmenity(unittest.TestCase):
    """Defines test cases for the Amenity class."""

    def test_init_no_args(self):
        """Test Amenity initialization without arguments."""
        amenity = Amenity()
        self.assertIsInstance(amenity, Amenity)
        self.assertTrue(hasattr(amenity, "id"))
        self.assertTrue(hasattr(amenity, "created_at"))
        self.assertTrue(hasattr(amenity, "updated_at"))
        self.assertTrue(hasattr(amenity, "name"))
        self.assertEqual(amenity.name, "")

    def test_init_with_args(self):
        """Test Amenity initialization with args (args should be ignored)."""
        amenity = Amenity("Pool")
        self.assertEqual(amenity.name, "")  # args should be ignored

    def test_init_with_kwargs(self):
        """Test Amenity initialization with kwargs."""
        time_now = datetime.now(timezone.utc)
        amenity = Amenity(name="WiFi", id="1234", created_at=time_now.isoformat(), updated_at=time_now.isoformat())
        self.assertEqual(amenity.name, "WiFi")
        self.assertEqual(amenity.id, "1234")
        self.assertEqual(amenity.created_at, time_now)
        self.assertEqual(amenity.updated_at, time_now)

    def test_str(self):
        """Test the __str__ method for Amenity."""
        amenity = Amenity()
        expected_str = f"[Amenity] ({amenity.id}) {amenity.__dict__}"
        self.assertEqual(str(amenity), expected_str)

    def test_to_dict(self):
        """Test conversion of Amenity instance to dictionary."""
        amenity = Amenity(name="Internet")
        amenity_dict = amenity.to_dict()
        self.assertEqual(amenity_dict["__class__"], "Amenity")
        self.assertEqual(amenity_dict["name"], "Internet")

if __name__ == "__main__":
    unittest.main()