import jwt
import datetime

SECRET_KEY = 'your-secret-key'

class JWTUtility:
    @staticmethod
    def encode(payload, secret=SECRET_KEY, algorithm='HS256', exp_minutes=30):
        payload = payload.copy()
        payload['exp'] = datetime.datetime.utcnow() + datetime.timedelta(minutes=exp_minutes)
        return jwt.encode(payload, secret, algorithm=algorithm)

    @staticmethod
    def decode(token, secret=SECRET_KEY, algorithms=['HS256']):
        try:
            return jwt.decode(token, secret, algorithms=algorithms)
        except jwt.ExpiredSignatureError:
            return {'error': 'Token expired'}
        except jwt.InvalidTokenError:
            return {'error': 'Invalid token'}
