import unittest
from types import SimpleNamespace
from src.response_utils import parse_json_response, validate_status_code

class FakeResponse:
    def __init__(self, json_data, status_code=200):
        self._json = json_data
        self.status_code = status_code
    def json(self):
        if self._json == "error":
            raise ValueError("bad json")
        return self._json

class TestResponseUtils(unittest.TestCase):
    def test_parse_json_response_success(self):
        resp = FakeResponse({"foo": "bar"})
        self.assertEqual(parse_json_response(resp), {"foo": "bar"})
    def test_parse_json_response_failure(self):
        resp = FakeResponse("error")
        with self.assertRaises(ValueError):
            parse_json_response(resp)
    def test_validate_status_code_success(self):
        resp = FakeResponse({}, 201)
        validate_status_code(resp, 201)
    def test_validate_status_code_failure(self):
        resp = FakeResponse({}, 404)
        with self.assertRaises(AssertionError):
            validate_status_code(resp, 200)

if __name__ == "__main__":
    unittest.main()
