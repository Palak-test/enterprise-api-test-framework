import unittest
from src.random_order import random_order

class TestRandomOrder(unittest.TestCase):
    def test_random_order_keys(self):
        order = random_order()
        self.assertIn("order_id", order)
        self.assertIn("user", order)
        self.assertIn("products", order)
        self.assertIn("order_date", order)
        self.assertIn("status", order)
        self.assertTrue(len(order["products"]) >= 1)
        self.assertTrue(order["status"] in ["pending", "shipped", "delivered", "cancelled"])

if __name__ == "__main__":
    unittest.main()
