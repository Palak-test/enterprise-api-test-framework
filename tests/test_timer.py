import unittest
from src.timer import timer
import time

class TestTimerUtility(unittest.TestCase):
    def test_timer_output(self):
        with timer("sleep block"):
            time.sleep(0.1)
        # No assertion, just ensures timer runs without error

if __name__ == "__main__":
    unittest.main()
