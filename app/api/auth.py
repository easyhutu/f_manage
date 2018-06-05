"""
CREAT: 2017/12/22
AUTHOR:　HEHAHUTU
"""
from flask import request, jsonify
from functools import wraps



# 装饰器，token认证
def check_token(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        token = request.headers.get('Authorization')
        # print(f'check: {token}')
        if token == '':
            return f(*args, **kwargs)
        else:
            return jsonify({'error': 'interval token'})

    return wrapper
