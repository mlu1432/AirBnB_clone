import unittest
from models.city import City
from datetime import datetime, timezone

#!/usr/bin/python3
"""Unit test for the City class."""


class TestCity(unittest.TestCase):
    """Test cases for the City class."""

    def test_init_no_args(self):
        """Test City initialization without arguments."""
        city = City()
        self.assertIsInstance(city, City)
        self.assertTrue(hasattr(city, "id"))
        self.assertTrue(hasattr(city, "created_at"))
        self.assertTrue(hasattr(city, "updated_at"))
        self.assertTrue(hasattr(city, "state_id"))
        self.assertTrue(hasattr(city, "name"))
        self.assertEqual(city.state_id, "")
        self.assertEqual(city.name, "")

    def test_init_with_args(self):
        """Test City initialization with args (should ignore args)."""
        city = City("New York")
        self.assertEqual(city.state_id, "")  # args should be ignored
        self.assertEqual(city.name, "")      # args should be ignored

    def test_init_with_kwargs(self):
        """Test City initialization with kwargs."""
        time_now = datetime.now(timezone.utc)
        city = City(state_id="1234", name="San Francisco", id="5678", created_at=time_now.isoformat(), updated_at=time_now.isoformat())
        self.assertEqual(city.state_id, "1234")
        self.assertEqual(city.name, "San Francisco")
        self.assertEqual(city.id, "5678")
        self.assertEqual(city.created_at, time_now)
        self.assertEqual(city.updated_at, time_now)

    def test_str(self):
        """Test the __str__ method for City."""
        city = City()
        expected_str = f"[City] ({city.id}) {city.__dict__}"
        self.assertEqual(str(city), expected_str)

    def test_to_dict(self):
        """Test conversion of City instance to dictionary."""
        city = City(name="Los Angeles", state_id="CA")
        city_dict = city.to_dict()
        self.assertEqual(city_dict["__class__"], "City")
        self.assertEqual(city_dict["name"], "Los Angeles")
        self.assertEqual(city_dict["state_id"], "CA")

if __name__ == "__main__":
    unittest.main()