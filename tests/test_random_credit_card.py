import unittest
from src.random_credit_card import random_credit_card_number

class TestRandomCreditCard(unittest.TestCase):
    def test_random_credit_card_number_format(self):
        cc = random_credit_card_number()
        self.assertIn(cc[0], ["4", "5", "6"])
        self.assertEqual(len(cc), 16)
        self.assertTrue(cc.isdigit())

if __name__ == "__main__":
    unittest.main()
