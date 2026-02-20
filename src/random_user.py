"""
Random user profile generator for enterprise-api-test-framework
"""
from src.random_data import random_string, random_email
from src.random_phone import random_phone_number
from src.random_address import random_address
from src.random_company import random_company_name

def random_user_profile():
    return {
        "username": random_string(8),
        "email": random_email(),
        "phone": random_phone_number(),
        "address": random_address(),
        "company": random_company_name()
    }
