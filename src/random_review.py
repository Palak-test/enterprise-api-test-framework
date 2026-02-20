"""
Random review record generator for enterprise-api-test-framework
"""
import random
from src.random_user import random_user_profile
from src.random_product import random_product
from src.random_date import random_date

def random_review():
    return {
        "review_id": random.randint(10000, 99999),
        "user": random_user_profile(),
        "product": random_product(),
        "rating": random.randint(1, 5),
        "review_date": random_date().isoformat(),
        "comment": random.choice(["Great product!", "Not satisfied.", "Would buy again.", "Average quality.", "Excellent value."])
    }
