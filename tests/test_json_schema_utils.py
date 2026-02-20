import unittest
import json
from src.json_schema_utils import validate_json_schema

class TestJSONSchemaUtils(unittest.TestCase):
    def test_validate_json_schema(self):
        schema = json.load(open("tests/user_schema.json"))
        valid_instance = {"username": "user1", "email": "user1@example.com"}
        # Should not raise
        validate_json_schema(valid_instance, schema)
        invalid_instance = {"username": "user2"}
        with self.assertRaises(Exception):
            validate_json_schema(invalid_instance, schema)

if __name__ == "__main__":
    unittest.main()
