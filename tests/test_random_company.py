import unittest
from src.random_company import random_company_name

class TestRandomCompany(unittest.TestCase):
    def test_random_company_name_format(self):
        name = random_company_name()
        self.assertTrue(any(prefix in name for prefix in ["Tech", "Data", "Cloud", "Info", "Global"]))
        self.assertTrue(any(suffix in name for suffix in ["Solutions", "Systems", "Networks", "Dynamics", "Enterprises"]))
        self.assertIn(" ", name)

if __name__ == "__main__":
    unittest.main()
