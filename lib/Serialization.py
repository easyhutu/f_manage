"""
Author: Meng
Date: 2018/6/3
"""
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from itsdangerous import BadSignature, SignatureExpired
from settings import SECRET_KEY


def value_dump(data: dict):
    s = Serializer(SECRET_KEY, expires_in=60 * 60 * 24)
    value = s.dumps(data)
    return value


def value_loads(data: str):
    s = Serializer(SECRET_KEY, expires_in=60 * 60 * 24)
    try:
        value = s.loads(data)
    except SignatureExpired:
        return None  # valid token, but expired
    except BadSignature:
        return None  # invalid token
    return value
