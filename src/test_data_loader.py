"""
Test data loader utility for enterprise-api-test-framework
"""
import json
import os

def load_test_data(file_path):
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Test data file not found: {file_path}")
    with open(file_path, "r") as f:
        return json.load(f)
