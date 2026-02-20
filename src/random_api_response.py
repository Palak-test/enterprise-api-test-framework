"""
Random API response generator for enterprise-api-test-framework
"""
import random
from src.random_api_request import random_api_request
from src.random_date import random_timestamp

def random_api_response():
    status_codes = [200, 201, 400, 401, 403, 404, 500]
    return {
        "response_id": random.randint(100000, 999999),
        "request": random_api_request(),
        "status_code": random.choice(status_codes),
        "data": {},
        "timestamp": random_timestamp()
    }
