import unittest
from src.api_client import APIClient

class TestAPIClient(unittest.TestCase):
    def setUp(self):
        self.client = APIClient("https://jsonplaceholder.typicode.com")

    def test_get_posts(self):
        posts = self.client.get("posts")
        self.assertIsInstance(posts, list)
        self.assertGreater(len(posts), 0)

if __name__ == "__main__":
    unittest.main()
