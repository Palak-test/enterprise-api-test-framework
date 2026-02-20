"""
Random address generator for enterprise-api-test-framework
"""
import random

def random_address():
    streets = ["Main St", "Oak Ave", "Pine Rd", "Elm St", "Maple Dr"]
    cities = ["Springfield", "Riverside", "Greenville", "Franklin", "Madison"]
    states = ["CA", "TX", "NY", "FL", "IL"]
    zip_code = ''.join(str(random.randint(0, 9)) for _ in range(5))
    street = random.choice(streets)
    city = random.choice(cities)
    state = random.choice(states)
    return f"{random.randint(100, 999)} {street}, {city}, {state} {zip_code}"
