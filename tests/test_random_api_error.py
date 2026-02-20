import unittest
from src.random_api_error import random_api_error

class TestRandomAPIError(unittest.TestCase):
    def test_random_api_error_keys(self):
        error = random_api_error()
        self.assertIn("error_id", error)
        self.assertIn("code", error)
        self.assertIn("message", error)
        self.assertIn("timestamp", error)
        self.assertTrue(error["code"] in ["400", "401", "403", "404", "500"])
        self.assertTrue(isinstance(error["message"], str))

if __name__ == "__main__":
    unittest.main()
