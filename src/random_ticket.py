"""
Random support ticket generator for enterprise-api-test-framework
"""
import random
from src.random_user import random_user_profile
from src.random_date import random_date

def random_support_ticket():
    return {
        "ticket_id": random.randint(100000, 999999),
        "user": random_user_profile(),
        "issue": random.choice(["Login problem", "Payment failed", "Feature request", "Bug report", "Account locked"]),
        "created_at": random_date().isoformat(),
        "status": random.choice(["open", "closed", "pending", "resolved"])
    }
