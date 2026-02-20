import unittest
from src.yaml_config_loader import load_yaml_config

class TestYAMLConfigLoader(unittest.TestCase):
    def test_load_yaml_config(self):
        config = load_yaml_config("config.yaml")
        self.assertEqual(config["api_key"], "yaml-key-xyz")
        self.assertEqual(config["base_url"], "https://yaml.api.example.com")

if __name__ == "__main__":
    unittest.main()
