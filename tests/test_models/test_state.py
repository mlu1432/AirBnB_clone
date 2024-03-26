#!/usr/bin/python3
"""Unit tests for the State class."""
import unittest
from models.state import State
from datetime import datetime, timezone


class TestState(unittest.TestCase):
    """Defines tests for the State class."""
    
    def test_init_no_args(self):
        """Test State initialization without arguments."""
        state = State()
        self.assertIsInstance(state, State)
        self.assertTrue(hasattr(state, "id"))
        self.assertTrue(hasattr(state, "created_at"))
        self.assertTrue(hasattr(state, "updated_at"))
        self.assertTrue(hasattr(state, "name"))
        self.assertEqual(state.name, "")

    def test_init_with_args(self):
        """Test State initialization with args (should ignore args)."""
        state = State("New York")
        self.assertEqual(state.name, "")  # args should be ignored

    def test_init_with_kwargs(self):
        """Test State initialization with kwargs."""
        time_now = datetime.now(timezone.utc)
        state = State(name="California", id="1234", created_at=time_now.isoformat(), updated_at=time_now.isoformat())
        self.assertEqual(state.name, "California")
        self.assertEqual(state.id, "1234")
        self.assertEqual(state.created_at, time_now)
        self.assertEqual(state.updated_at, time_now)

    def test_str(self):
        """Test the __str__ method for State."""
        state = State()
        expected_str = f"[State] ({state.id}) {state.__dict__}"
        self.assertEqual(str(state), expected_str)

    def test_to_dict(self):
        """Test conversion of State instance to dictionary."""
        state = State(name="Texas")
        state_dict = state.to_dict()
        expected_keys = {"id", "created_at", "updated_at", "name", "__class__"}
        self.assertTrue(expected_keys.issubset(state_dict.keys()))
        self.assertEqual(state_dict["__class__"], "State")
        self.assertEqual(state_dict["name"], "Texas")

if __name__ == "__main__":
    unittest.main()
