import unittest
from src.random_api_event import random_api_event

class TestRandomAPIEvent(unittest.TestCase):
    def test_random_api_event_keys(self):
        event = random_api_event()
        self.assertIn("event_id", event)
        self.assertIn("type", event)
        self.assertIn("user", event)
        self.assertIn("timestamp", event)
        self.assertTrue(event["type"] in ["user_created", "order_placed", "product_added", "review_posted", "login_attempt"])

if __name__ == "__main__":
    unittest.main()
