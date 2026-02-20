"""
JWT utility for enterprise-api-test-framework
"""
import jwt
import datetime

def generate_jwt(payload, secret, algorithm="HS256", expires_in=3600):
    payload = payload.copy()
    payload["exp"] = datetime.datetime.utcnow() + datetime.timedelta(seconds=expires_in)
    return jwt.encode(payload, secret, algorithm=algorithm)

def decode_jwt(token, secret, algorithms=["HS256"]):
    return jwt.decode(token, secret, algorithms=algorithms)
