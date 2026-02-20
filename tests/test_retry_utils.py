import unittest
import random
from src.retry_utils import retry

class TestRetryUtils(unittest.TestCase):
    def test_retry_success(self):
        calls = []
        @retry(times=3, delay=0.01)
        def flaky():
            calls.append(1)
            if len(calls) < 2:
                raise ValueError("fail")
            return "ok"
        self.assertEqual(flaky(), "ok")
        self.assertEqual(len(calls), 2)

    def test_retry_failure(self):
        @retry(times=2, delay=0.01)
        def always_fail():
            raise RuntimeError("fail")
        with self.assertRaises(RuntimeError):
            always_fail()

if __name__ == "__main__":
    unittest.main()
