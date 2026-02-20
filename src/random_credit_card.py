"""
Random credit card number generator for enterprise-api-test-framework
"""
import random

def random_credit_card_number():
    prefix = random.choice(["4", "5", "6"])
    number = prefix + ''.join(str(random.randint(0, 9)) for _ in range(15))
    return number
