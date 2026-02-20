"""
Random API request generator for enterprise-api-test-framework
"""
import random
from src.random_user import random_user_profile
from src.random_product import random_product
from src.random_date import random_timestamp

def random_api_request():
    methods = ["GET", "POST", "PUT", "DELETE"]
    endpoints = ["/users", "/products", "/orders", "/reviews", "/login"]
    return {
        "request_id": random.randint(100000, 999999),
        "method": random.choice(methods),
        "endpoint": random.choice(endpoints),
        "payload": random.choice([random_user_profile(), random_product()]),
        "timestamp": random_timestamp()
    }
