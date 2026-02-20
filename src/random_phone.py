"""
Random phone number generator for enterprise-api-test-framework
"""
import random

def random_phone_number(country_code="+1"):
    number = ''.join(str(random.randint(0, 9)) for _ in range(10))
    return f"{country_code}{number}"
