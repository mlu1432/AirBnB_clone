#!/usr/bin/python3
"""Unit test for the Review class."""

import unittest
from models.review import Review
from datetime import datetime, timezone


class TestReview(unittest.TestCase):
    """Defines tests for the Review class."""
    
    def setUp(self):
        """Set up method called before each test."""
        self.review = Review()

    def test_init_no_args(self):
        """Test Review initialization without arguments."""
        self.assertIsInstance(self.review, Review)
        self.assertTrue(hasattr(self.review, "id"))
        self.assertTrue(hasattr(self.review, "created_at"))
        self.assertTrue(hasattr(self.review, "updated_at"))
        self.assertTrue(hasattr(self.review, "place_id"))
        self.assertTrue(hasattr(self.review, "user_id"))
        self.assertTrue(hasattr(self.review, "text"))
        self.assertEqual(self.review.place_id, "")
        self.assertEqual(self.review.user_id, "")
        self.assertEqual(self.review.text, "")

    def test_init_with_kwargs(self):
        """Test Review initialization with kwargs."""
        time_now = datetime.now(timezone.utc)
        review = Review(place_id="place_123", user_id="user_123", text="Great place!", created_at=time_now.isoformat(), updated_at=time_now.isoformat())
        self.assertEqual(review.place_id, "place_123")
        self.assertEqual(review.user_id, "user_123")
        self.assertEqual(review.text, "Great place!")
        self.assertEqual(review.created_at, time_now)
        self.assertEqual(review.updated_at, time_now)

    def test_str(self):
        """Test the __str__ method for Review."""
        expected_str = f"[Review] ({self.review.id}) {self.review.__dict__}"
        self.assertEqual(str(self.review), expected_str)

    def test_to_dict(self):
        """Test conversion of Review instance to dictionary."""
        self.review.place_id = "place_1234"
        self.review.user_id = "user_1234"
        self.review.text = "Lovely spot!"
        review_dict = self.review.to_dict()
        self.assertEqual(review_dict["__class__"], "Review")
        self.assertEqual(review_dict["place_id"], "place_1234")
        self.assertEqual(review_dict["user_id"], "user_1234")
        self.assertEqual(review_dict["text"], "Lovely spot!")

if __name__ == "__main__":
    unittest.main()