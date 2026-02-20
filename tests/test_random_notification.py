import unittest
from src.random_notification import random_notification

class TestRandomNotification(unittest.TestCase):
    def test_random_notification_keys(self):
        notification = random_notification()
        self.assertIn("notification_id", notification)
        self.assertIn("user", notification)
        self.assertIn("message", notification)
        self.assertIn("sent_at", notification)
        self.assertIn("read", notification)
        self.assertTrue(isinstance(notification["message"], str))
        self.assertTrue(isinstance(notification["read"], bool))

if __name__ == "__main__":
    unittest.main()
