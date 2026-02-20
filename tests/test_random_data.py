import unittest
from src.random_data import random_string, random_email

class TestRandomData(unittest.TestCase):
    def test_random_string_length(self):
        s = random_string(12)
        self.assertEqual(len(s), 12)

    def test_random_email_format(self):
        email = random_email()
        self.assertIn("@example.com", email)
        self.assertGreater(len(email), 12)

if __name__ == "__main__":
    unittest.main()
