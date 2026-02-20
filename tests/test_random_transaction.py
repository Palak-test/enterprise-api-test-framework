import unittest
from src.random_transaction import random_transaction

class TestRandomTransaction(unittest.TestCase):
    def test_random_transaction_keys(self):
        txn = random_transaction()
        self.assertIn("transaction_id", txn)
        self.assertIn("amount", txn)
        self.assertIn("currency", txn)
        self.assertIn("timestamp", txn)
        self.assertIn("card_number", txn)
        self.assertTrue(txn["currency"] in ["USD", "EUR", "INR", "GBP"])
        self.assertEqual(len(txn["card_number"]), 16)

if __name__ == "__main__":
    unittest.main()
