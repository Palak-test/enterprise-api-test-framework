import unittest
from src.random_phone import random_phone_number

class TestRandomPhone(unittest.TestCase):
    def test_random_phone_number_format(self):
        phone = random_phone_number()
        self.assertTrue(phone.startswith("+1"))
        self.assertEqual(len(phone), 12)
    def test_random_phone_number_custom_country(self):
        phone = random_phone_number("+91")
        self.assertTrue(phone.startswith("+91"))
        self.assertEqual(len(phone), 13)

if __name__ == "__main__":
    unittest.main()
