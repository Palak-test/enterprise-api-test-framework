import unittest
from src.auth_utils import get_auth_headers

class TestAuthUtils(unittest.TestCase):
    def test_get_auth_headers(self):
        api_key = "test-key-abc"
        headers = get_auth_headers(api_key)
        self.assertEqual(headers["Authorization"], f"Bearer {api_key}")

if __name__ == "__main__":
    unittest.main()
