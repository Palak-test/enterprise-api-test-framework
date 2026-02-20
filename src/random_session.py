"""
Random session record generator for enterprise-api-test-framework
"""
import random
from src.random_user import random_user_profile
from src.random_date import random_timestamp

def random_session():
    return {
        "session_id": random.randint(100000, 999999),
        "user": random_user_profile(),
        "start_time": random_timestamp(),
        "end_time": random_timestamp(),
        "active": random.choice([True, False])
    }
