"""
Random product record generator for enterprise-api-test-framework
"""
import random

def random_product():
    names = ["Widget", "Gadget", "Device", "Tool", "Accessory"]
    categories = ["Electronics", "Home", "Outdoor", "Office", "Automotive"]
    return {
        "product_id": random.randint(1000, 9999),
        "name": random.choice(names),
        "category": random.choice(categories),
        "price": round(random.uniform(5, 500), 2),
        "stock": random.randint(0, 100)
    }
