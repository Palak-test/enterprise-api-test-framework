import unittest
from src.random_api_request import random_api_request

class TestRandomAPIRequest(unittest.TestCase):
    def test_random_api_request_keys(self):
        req = random_api_request()
        self.assertIn("request_id", req)
        self.assertIn("method", req)
        self.assertIn("endpoint", req)
        self.assertIn("payload", req)
        self.assertIn("timestamp", req)
        self.assertTrue(req["method"] in ["GET", "POST", "PUT", "DELETE"])
        self.assertTrue(req["endpoint"] in ["/users", "/products", "/orders", "/reviews", "/login"])

if __name__ == "__main__":
    unittest.main()
