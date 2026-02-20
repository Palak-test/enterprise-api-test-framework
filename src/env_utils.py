"""
Environment variable utility for enterprise-api-test-framework
"""
import os

def get_env_variable(key, default=None):
    return os.environ.get(key, default)
