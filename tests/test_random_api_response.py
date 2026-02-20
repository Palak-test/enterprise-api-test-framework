import unittest
from src.random_api_response import random_api_response

class TestRandomAPIResponse(unittest.TestCase):
    def test_random_api_response_keys(self):
        resp = random_api_response()
        self.assertIn("response_id", resp)
        self.assertIn("request", resp)
        self.assertIn("status_code", resp)
        self.assertIn("data", resp)
        self.assertIn("timestamp", resp)
        self.assertTrue(resp["status_code"] in [200, 201, 400, 401, 403, 404, 500])

if __name__ == "__main__":
    unittest.main()
