"""
Random API webhook generator for enterprise-api-test-framework
"""
import random
from src.random_api_event import random_api_event
from src.random_date import random_timestamp

def random_api_webhook():
    webhook_types = ["order_update", "user_notification", "payment_status", "shipment_tracking"]
    return {
        "webhook_id": random.randint(100000, 999999),
        "type": random.choice(webhook_types),
        "event": random_api_event(),
        "timestamp": random_timestamp()
    }
