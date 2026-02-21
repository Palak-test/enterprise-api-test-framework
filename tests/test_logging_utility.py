import unittest
import os
import logging
from src.logging_utility import LoggingUtility

class TestLoggingUtility(unittest.TestCase):
    def setUp(self):
        self.log_file = "tests/test_app.log"
        if os.path.exists(self.log_file):
            os.remove(self.log_file)
        LoggingUtility.setup_logging(self.log_file, level=logging.DEBUG)

    def tearDown(self):
        for handler in logging.root.handlers[:]:
            handler.close()
            logging.root.removeHandler(handler)
        if os.path.exists(self.log_file):
            os.remove(self.log_file)

    def test_log_info(self):
        LoggingUtility.log_info("Info message")
        with open(self.log_file, 'r', encoding='utf-8') as f:
            content = f.read()
        self.assertIn("Info message", content)
        self.assertIn("INFO", content)

    def test_log_error(self):
        LoggingUtility.log_error("Error message")
        with open(self.log_file, 'r', encoding='utf-8') as f:
            content = f.read()
        self.assertIn("Error message", content)
        self.assertIn("ERROR", content)

    def test_log_debug(self):
        LoggingUtility.log_debug("Debug message")
        with open(self.log_file, 'r', encoding='utf-8') as f:
            content = f.read()
        self.assertIn("Debug message", content)
        self.assertIn("DEBUG", content)

if __name__ == '__main__':
    unittest.main()
