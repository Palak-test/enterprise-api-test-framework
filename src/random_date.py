"""
Random date and timestamp generator for enterprise-api-test-framework
"""
import random
import datetime

def random_date(start_year=2000, end_year=2025):
    start = datetime.date(start_year, 1, 1)
    end = datetime.date(end_year, 12, 31)
    delta = end - start
    random_days = random.randint(0, delta.days)
    return start + datetime.timedelta(days=random_days)

def random_timestamp(start_year=2000, end_year=2025):
    date = random_date(start_year, end_year)
    random_time = datetime.timedelta(
        hours=random.randint(0, 23),
        minutes=random.randint(0, 59),
        seconds=random.randint(0, 59)
    )
    dt = datetime.datetime.combine(date, datetime.time()) + random_time
    return dt.isoformat()
