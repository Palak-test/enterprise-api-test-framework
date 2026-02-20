import unittest
from src.test_data_loader import load_test_data

class TestTestDataLoader(unittest.TestCase):
    def test_load_test_data(self):
        data = load_test_data("tests/test_data.json")
        self.assertIsInstance(data, list)
        self.assertEqual(data[0]["username"], "user1")
        self.assertEqual(data[1]["email"], "user2@example.com")

if __name__ == "__main__":
    unittest.main()
