"""
Random log entry generator for enterprise-api-test-framework
"""
import random
from src.random_date import random_timestamp

def random_log_entry():
    levels = ["INFO", "DEBUG", "WARNING", "ERROR", "CRITICAL"]
    return {
        "log_id": random.randint(100000, 999999),
        "level": random.choice(levels),
        "message": random.choice(["Operation successful", "User login", "Data updated", "Exception occurred", "Timeout"]),
        "timestamp": random_timestamp()
    }
