import unittest
from src.random_log import random_log_entry

class TestRandomLog(unittest.TestCase):
    def test_random_log_entry_keys(self):
        log = random_log_entry()
        self.assertIn("log_id", log)
        self.assertIn("level", log)
        self.assertIn("message", log)
        self.assertIn("timestamp", log)
        self.assertTrue(log["level"] in ["INFO", "DEBUG", "WARNING", "ERROR", "CRITICAL"])
        self.assertTrue(isinstance(log["message"], str))

if __name__ == "__main__":
    unittest.main()
