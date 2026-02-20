import unittest
from src.jwt_utils import generate_jwt, decode_jwt

class TestJWTUtils(unittest.TestCase):
    def test_generate_and_decode_jwt(self):
        secret = "mysecret"
        payload = {"user_id": 123}
        token = generate_jwt(payload, secret, expires_in=60)
        decoded = decode_jwt(token, secret)
        self.assertEqual(decoded["user_id"], 123)
        self.assertIn("exp", decoded)

if __name__ == "__main__":
    unittest.main()
