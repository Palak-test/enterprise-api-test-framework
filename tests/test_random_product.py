import unittest
from src.random_product import random_product

class TestRandomProduct(unittest.TestCase):
    def test_random_product_keys(self):
        product = random_product()
        self.assertIn("product_id", product)
        self.assertIn("name", product)
        self.assertIn("category", product)
        self.assertIn("price", product)
        self.assertIn("stock", product)
        self.assertTrue(product["price"] >= 5)
        self.assertTrue(product["stock"] >= 0)

if __name__ == "__main__":
    unittest.main()
