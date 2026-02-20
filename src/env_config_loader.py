"""
Environment-specific config loader for enterprise-api-test-framework
"""
import json
import os

def load_env_config(env="dev"):
    config_file = f"config.{env}.json"
    if not os.path.exists(config_file):
        raise FileNotFoundError(f"Config file not found: {config_file}")
    with open(config_file, "r") as f:
        return json.load(f)
