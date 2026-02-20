import unittest
from src.random_password import random_password

class TestRandomPassword(unittest.TestCase):
    def test_random_password_length(self):
        pwd = random_password(16)
        self.assertEqual(len(pwd), 16)
    def test_random_password_complexity(self):
        pwd = random_password(20)
        self.assertTrue(any(c.islower() for c in pwd))
        self.assertTrue(any(c.isupper() for c in pwd))
        self.assertTrue(any(c.isdigit() for c in pwd))
        self.assertTrue(any(c in '!@#$%^&*()_+-=' for c in pwd))

if __name__ == "__main__":
    unittest.main()
