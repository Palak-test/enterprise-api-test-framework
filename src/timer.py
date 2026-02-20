"""
Timing utility for enterprise-api-test-framework
"""
import time
from contextlib import contextmanager

@contextmanager
def timer(name="block"):
    start = time.time()
    yield
    end = time.time()
    print(f"{name} took {end - start:.4f} seconds")
