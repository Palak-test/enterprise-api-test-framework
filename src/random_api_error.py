"""
Random API error generator for enterprise-api-test-framework
"""
import random
from src.random_date import random_date

def random_api_error():
    return {
        "error_id": random.randint(10000, 99999),
        "code": random.choice(["400", "401", "403", "404", "500"]),
        "message": random.choice(["Bad Request", "Unauthorized", "Forbidden", "Not Found", "Internal Server Error"]),
        "timestamp": random_date().isoformat()
    }
