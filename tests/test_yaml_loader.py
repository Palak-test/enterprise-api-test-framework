import unittest
from src.yaml_loader import YAMLLoader
import os

class TestYAMLLoader(unittest.TestCase):
    def setUp(self):
        self.yaml_path = 'tests/sample_data.yaml'
        with open(self.yaml_path, 'w', encoding='utf-8') as f:
            f.write('users:\n  - username: user1\n    email: user1@example.com\n  - username: user2\n    email: user2@example.com\n')

    def tearDown(self):
        os.remove(self.yaml_path)

    def test_load_yaml(self):
        data = YAMLLoader.load_yaml(self.yaml_path)
        self.assertIn('users', data)
        self.assertEqual(len(data['users']), 2)
        self.assertEqual(data['users'][0]['username'], 'user1')
        self.assertEqual(data['users'][1]['email'], 'user2@example.com')

    def test_file_not_found(self):
        with self.assertRaises(FileNotFoundError):
            YAMLLoader.load_yaml('not_exist.yaml')

if __name__ == '__main__':
    unittest.main()
