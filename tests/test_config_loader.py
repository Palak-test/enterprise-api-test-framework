import unittest
from src.config_loader import ConfigLoader
import os

class TestConfigLoader(unittest.TestCase):
    def setUp(self):
        import yaml
        import json
        self.json_path = "tests/sample_config.json"
        self.yaml_path = "tests/sample_config.yaml"
        with open(self.json_path, "w", encoding="utf-8") as f:
            json.dump({"key": "value", "num": 42}, f)
        with open(self.yaml_path, "w", encoding="utf-8") as f:
            yaml.dump({"key": "value", "num": 42}, f)

    def tearDown(self):
        os.remove(self.json_path)
        os.remove(self.yaml_path)

    def test_load_json(self):
        loader = ConfigLoader(self.json_path)
        self.assertEqual(loader.get("key"), "value")
        self.assertEqual(loader.get("num"), 42)

    def test_load_yaml(self):
        loader = ConfigLoader(self.yaml_path)
        self.assertEqual(loader.get("key"), "value")
        self.assertEqual(loader.get("num"), 42)

    def test_file_not_found(self):
        loader = ConfigLoader("not_exist.yaml")
        self.assertEqual(loader.config, {})

    def test_unsupported_type(self):
        path = "tests/sample_config.txt"
        with open(path, "w", encoding="utf-8") as f:
            f.write("unsupported")
        try:
            with self.assertRaises(ValueError):
                ConfigLoader(path)
        finally:
            os.remove(path)

if __name__ == "__main__":
    unittest.main()
