import unittest
from src.random_user import random_user_profile

class TestRandomUserProfile(unittest.TestCase):
    def test_random_user_profile_keys(self):
        profile = random_user_profile()
        self.assertIn("username", profile)
        self.assertIn("email", profile)
        self.assertIn("phone", profile)
        self.assertIn("address", profile)
        self.assertIn("company", profile)
        self.assertTrue(profile["email"].endswith("@example.com"))
        self.assertTrue(profile["phone"].startswith("+1"))

if __name__ == "__main__":
    unittest.main()
