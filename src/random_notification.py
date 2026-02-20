"""
Random notification generator for enterprise-api-test-framework
"""
import random
from src.random_user import random_user_profile
from src.random_date import random_date

def random_notification():
    return {
        "notification_id": random.randint(100000, 999999),
        "user": random_user_profile(),
        "message": random.choice(["Welcome!", "Your order shipped.", "Password changed.", "New feature released.", "Account updated."]),
        "sent_at": random_date().isoformat(),
        "read": random.choice([True, False])
    }
