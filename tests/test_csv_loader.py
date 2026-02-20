import unittest
from src.csv_loader import load_csv_data

class TestCSVLoader(unittest.TestCase):
    def test_load_csv_data(self):
        data = load_csv_data("tests/test_data.csv")
        self.assertEqual(len(data), 2)
        self.assertEqual(data[0]["username"], "user1")
        self.assertEqual(data[1]["email"], "user2@example.com")

if __name__ == "__main__":
    unittest.main()
