"""
YAML config loader for enterprise-api-test-framework
"""
import yaml
import os

def load_yaml_config(file_path):
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"YAML config file not found: {file_path}")
    with open(file_path, "r") as f:
        return yaml.safe_load(f)
