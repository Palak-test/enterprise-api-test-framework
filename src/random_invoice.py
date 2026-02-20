"""
Random invoice record generator for enterprise-api-test-framework
"""
import random
from src.random_date import random_date
from src.random_company import random_company_name

def random_invoice():
    return {
        "invoice_id": random.randint(10000, 99999),
        "company": random_company_name(),
        "date": random_date().isoformat(),
        "total": round(random.uniform(100, 5000), 2),
        "paid": random.choice([True, False])
    }
