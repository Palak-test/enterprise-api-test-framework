import yaml
import os

class YAMLLoader:
    @staticmethod
    def load_yaml(path):
        if not os.path.exists(path):
            raise FileNotFoundError(f"YAML file not found: {path}")
        with open(path, 'r', encoding='utf-8') as f:
            return yaml.safe_load(f)
