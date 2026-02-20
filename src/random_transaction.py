"""
Random transaction record generator for enterprise-api-test-framework
"""
import random
from src.random_credit_card import random_credit_card_number
from src.random_date import random_timestamp

def random_transaction():
    return {
        "transaction_id": random.randint(100000, 999999),
        "amount": round(random.uniform(10, 1000), 2),
        "currency": random.choice(["USD", "EUR", "INR", "GBP"]),
        "timestamp": random_timestamp(),
        "card_number": random_credit_card_number()
    }
