import unittest
from src.random_api_config import RandomAPIConfig

class TestRandomAPIConfig(unittest.TestCase):
    def test_generate_config(self):
        config = RandomAPIConfig.generate_config()
        self.assertIn("base_url", config)
        self.assertIn("timeout", config)
        self.assertIn("retries", config)
        self.assertIn("headers", config)
        self.assertIn("Authorization", config["headers"])
        self.assertIn(config["headers"]["Content-Type"], ["application/json", "application/xml"])
        self.assertTrue(isinstance(config["timeout"], int))
        self.assertTrue(isinstance(config["retries"], int))

if __name__ == '__main__':
    unittest.main()
