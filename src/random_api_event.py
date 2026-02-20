"""
Random API event generator for enterprise-api-test-framework
"""
import random
from src.random_user import random_user_profile
from src.random_date import random_timestamp

def random_api_event():
    event_types = ["user_created", "order_placed", "product_added", "review_posted", "login_attempt"]
    return {
        "event_id": random.randint(100000, 999999),
        "type": random.choice(event_types),
        "user": random_user_profile(),
        "timestamp": random_timestamp()
    }
