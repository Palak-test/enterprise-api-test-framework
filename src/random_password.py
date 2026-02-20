"""
Random password generator for enterprise-api-test-framework
"""
import random
import string

def random_password(length=12):
    chars = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choices(chars, k=length))
