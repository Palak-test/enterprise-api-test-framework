"""
Random company name generator for enterprise-api-test-framework
"""
import random

def random_company_name():
    prefixes = ["Tech", "Data", "Cloud", "Info", "Global"]
    suffixes = ["Solutions", "Systems", "Networks", "Dynamics", "Enterprises"]
    return f"{random.choice(prefixes)} {random.choice(suffixes)}"
