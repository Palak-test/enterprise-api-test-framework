import unittest
from src.random_invoice import random_invoice

class TestRandomInvoice(unittest.TestCase):
    def test_random_invoice_keys(self):
        invoice = random_invoice()
        self.assertIn("invoice_id", invoice)
        self.assertIn("company", invoice)
        self.assertIn("date", invoice)
        self.assertIn("total", invoice)
        self.assertIn("paid", invoice)
        self.assertIsInstance(invoice["paid"], bool)
        self.assertTrue(invoice["total"] >= 100)

if __name__ == "__main__":
    unittest.main()
