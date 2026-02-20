"""
Random audit record generator for enterprise-api-test-framework
"""
import random
from src.random_user import random_user_profile
from src.random_date import random_timestamp

def random_audit_record():
    actions = ["create", "update", "delete", "access", "login"]
    return {
        "audit_id": random.randint(100000, 999999),
        "user": random_user_profile(),
        "action": random.choice(actions),
        "timestamp": random_timestamp()
    }
