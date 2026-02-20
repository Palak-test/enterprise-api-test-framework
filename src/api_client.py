"""
API client for enterprise-api-test-framework
"""

import requests
from src.logger import setup_logger


class APIClient:
    def __init__(self, base_url):
        self.base_url = base_url
        self.logger = setup_logger("APIClient")

    def get(self, endpoint, params=None):
        url = f"{self.base_url}/{endpoint.lstrip('/')}"
        self.logger.info(f"GET {url} params={params}")
        response = requests.get(url, params=params)
        self.logger.info(f"Response: {response.status_code}")
        response.raise_for_status()
        return response.json()

    def post(self, endpoint, data=None, json=None):
        url = f"{self.base_url}/{endpoint.lstrip('/')}"
        self.logger.info(f"POST {url} data={data} json={json}")
        response = requests.post(url, data=data, json=json)
        self.logger.info(f"Response: {response.status_code}")
        response.raise_for_status()
        return response.json()
