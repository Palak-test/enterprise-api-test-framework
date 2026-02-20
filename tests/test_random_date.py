import unittest
from src.random_date import random_date, random_timestamp
import datetime

class TestRandomDate(unittest.TestCase):
    def test_random_date_range(self):
        d = random_date(2010, 2012)
        self.assertTrue(datetime.date(2010, 1, 1) <= d <= datetime.date(2012, 12, 31))
    def test_random_timestamp_format(self):
        ts = random_timestamp(2015, 2015)
        dt = datetime.datetime.fromisoformat(ts)
        self.assertEqual(dt.year, 2015)

if __name__ == "__main__":
    unittest.main()
