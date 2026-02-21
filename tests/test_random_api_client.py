import unittest
from src.random_api_client import RandomAPIClient

class TestRandomAPIClient(unittest.TestCase):
    def test_get_random_resource(self):
        base_url = "https://jsonplaceholder.typicode.com"
        resources = ["posts", "comments", "albums"]
        status, data = RandomAPIClient.get_random_resource(base_url, resources)
        self.assertIn(status, [200, 404])
        self.assertTrue(isinstance(data, (list, dict, str)))

    def test_post_random_data(self):
        base_url = "https://jsonplaceholder.typicode.com"
        resource = "posts"
        data = {"title": "foo", "body": "bar", "userId": 1}
        status, resp = RandomAPIClient.post_random_data(base_url, resource, data)
        self.assertIn(status, [201, 200, 404])
        self.assertTrue(isinstance(resp, (dict, str)))

if __name__ == '__main__':
    unittest.main()
