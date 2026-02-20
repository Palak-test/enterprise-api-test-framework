import unittest
from src.random_address import random_address

class TestRandomAddress(unittest.TestCase):
    def test_random_address_format(self):
        address = random_address()
        self.assertIn(",", address)
        self.assertTrue(any(city in address for city in ["Springfield", "Riverside", "Greenville", "Franklin", "Madison"]))
        self.assertTrue(any(state in address for state in ["CA", "TX", "NY", "FL", "IL"]))
        self.assertRegex(address, r"\d{5}$")

if __name__ == "__main__":
    unittest.main()
