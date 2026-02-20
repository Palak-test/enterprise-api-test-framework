import unittest
from src.config_loader import ConfigLoader

class TestConfigLoader(unittest.TestCase):
    def test_load_config(self):
        loader = ConfigLoader("config.json")
        self.assertEqual(loader.get("base_url"), "https://jsonplaceholder.typicode.com")

    def test_default_value(self):
        loader = ConfigLoader("config.json")
        self.assertEqual(loader.get("nonexistent", "default"), "default")

if __name__ == "__main__":
    unittest.main()
