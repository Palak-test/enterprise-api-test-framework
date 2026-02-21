import requests
import random

class RandomAPIClient:
    @staticmethod
    def get_random_resource(base_url, resource_list):
        resource = random.choice(resource_list)
        url = f"{base_url}/{resource}"
        response = requests.get(url)
        return response.status_code, response.json() if response.headers.get('Content-Type', '').startswith('application/json') else response.text

    @staticmethod
    def post_random_data(base_url, resource, data):
        url = f"{base_url}/{resource}"
        response = requests.post(url, json=data)
        return response.status_code, response.json() if response.headers.get('Content-Type', '').startswith('application/json') else response.text
