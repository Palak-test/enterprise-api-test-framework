import unittest
from src.env_config_loader import load_env_config

class TestEnvConfigLoader(unittest.TestCase):
    def test_load_dev_config(self):
        config = load_env_config("dev")
        self.assertEqual(config["api_key"], "dev-key-123")
    def test_load_staging_config(self):
        config = load_env_config("staging")
        self.assertEqual(config["base_url"], "https://staging.api.example.com")
    def test_load_prod_config(self):
        config = load_env_config("prod")
        self.assertEqual(config["api_key"], "prod-key-789")

if __name__ == "__main__":
    unittest.main()
