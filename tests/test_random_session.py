import unittest
from src.random_session import random_session

class TestRandomSession(unittest.TestCase):
    def test_random_session_keys(self):
        session = random_session()
        self.assertIn("session_id", session)
        self.assertIn("user", session)
        self.assertIn("start_time", session)
        self.assertIn("end_time", session)
        self.assertIn("active", session)
        self.assertTrue(isinstance(session["active"], bool))

if __name__ == "__main__":
    unittest.main()
