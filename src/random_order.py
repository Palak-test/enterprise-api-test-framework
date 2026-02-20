"""
Random order record generator for enterprise-api-test-framework
"""
import random
from src.random_user import random_user_profile
from src.random_product import random_product
from src.random_date import random_date

def random_order():
    return {
        "order_id": random.randint(10000, 99999),
        "user": random_user_profile(),
        "products": [random_product() for _ in range(random.randint(1, 5))],
        "order_date": random_date().isoformat(),
        "status": random.choice(["pending", "shipped", "delivered", "cancelled"])
    }
