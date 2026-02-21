"""
Configuration loader for enterprise-api-test-framework
"""
import json
import os

class ConfigLoader:
    def __init__(self, config_path="config.json"):
        self.config_path = config_path
        self.config = self.load_config()

    def load_config(self):
        import yaml
        if not os.path.exists(self.config_path):
            return {}
        ext = os.path.splitext(self.config_path)[1].lower()
        with open(self.config_path, "r", encoding="utf-8") as f:
            if ext in [".yaml", ".yml"]:
                return yaml.safe_load(f)
            elif ext == ".json":
                return json.load(f)
            else:
                raise ValueError(f"Unsupported config file type: {ext}")

    def get(self, key, default=None):
        return self.config.get(key, default)
