import unittest
from src.sample_module import sample_function

class TestSampleFunction(unittest.TestCase):
    def test_sample_function(self):
        self.assertEqual(sample_function(), "Hello, Enterprise API!")

if __name__ == "__main__":
    unittest.main()
