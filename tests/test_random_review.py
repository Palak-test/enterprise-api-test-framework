import unittest
from src.random_review import random_review

class TestRandomReview(unittest.TestCase):
    def test_random_review_keys(self):
        review = random_review()
        self.assertIn("review_id", review)
        self.assertIn("user", review)
        self.assertIn("product", review)
        self.assertIn("rating", review)
        self.assertIn("review_date", review)
        self.assertIn("comment", review)
        self.assertTrue(1 <= review["rating"] <= 5)
        self.assertTrue(isinstance(review["comment"], str))

if __name__ == "__main__":
    unittest.main()
