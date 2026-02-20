"""
Retry utility for enterprise-api-test-framework
"""
import time
from functools import wraps

def retry(times=3, delay=1, exceptions=(Exception,)):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(1, times + 1):
                try:
                    return func(*args, **kwargs)
                except exceptions as e:
                    if attempt == times:
                        raise
                    time.sleep(delay)
        return wrapper
    return decorator
