"""
Random data generator utility for enterprise-api-test-framework
"""
import random
import string

def random_string(length=8):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

def random_email():
    return f"{random_string(6)}@example.com"
