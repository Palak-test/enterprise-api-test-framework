import unittest
from src.jwt_utility import JWTUtility, SECRET_KEY
import jwt

class TestJWTUtility(unittest.TestCase):
    def test_encode_and_decode(self):
        payload = {'user_id': 123, 'role': 'admin'}
        token = JWTUtility.encode(payload)
        decoded = JWTUtility.decode(token)
        self.assertEqual(decoded['user_id'], 123)
        self.assertEqual(decoded['role'], 'admin')

    def test_expired_token(self):
        payload = {'user_id': 456}
        token = JWTUtility.encode(payload, exp_minutes=-1)  # Already expired
        decoded = JWTUtility.decode(token)
        self.assertIn('error', decoded)
        self.assertEqual(decoded['error'], 'Token expired')

    def test_invalid_token(self):
        decoded = JWTUtility.decode('invalid.token')
        self.assertIn('error', decoded)
        self.assertEqual(decoded['error'], 'Invalid token')

if __name__ == '__main__':
    unittest.main()
