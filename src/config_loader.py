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
        if not os.path.exists(self.config_path):
            return {}
        with open(self.config_path, "r") as f:
            return json.load(f)

    def get(self, key, default=None):
        return self.config.get(key, default)
