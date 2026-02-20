import unittest
import os
from src.html_report import generate_html_report

class TestHTMLReport(unittest.TestCase):
    def test_generate_html_report(self):
        results = [
            {"name": "test_one", "passed": True},
            {"name": "test_two", "passed": False}
        ]
        filename = "test_report.html"
        generate_html_report(results, filename)
        self.assertTrue(os.path.exists(filename))
        with open(filename) as f:
            content = f.read()
            self.assertIn("test_one", content)
            self.assertIn("FAIL", content)
        os.remove(filename)

if __name__ == "__main__":
    unittest.main()
