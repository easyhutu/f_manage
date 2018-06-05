"""
Author: Meng
Date: 2018/6/2
"""
from app.models.admin.user import User, ADMIN, GROUP
from functools import wraps
from lib.code import Msg
import base64
from flask import g
from flask import request


def auth_token(func):
    @wraps(func)
    def decorated_view(*args, **kwargs):
        # first, try to login using the api_key url arg
        api_key = request.args.get('assess_key')
        if api_key:
            user = User.verify_auth_token(api_key)
            if user:
                g.user = user
                return func(*args, **kwargs)

        api_key = request.form.get('assess_key')
        if api_key:
            user = User.verify_auth_token(api_key)
            if user:
                g.user = user
                return func(*args, **kwargs)

        if request.json:
            api_key = request.json.get('assess_key')
            if api_key:
                user = User.verify_auth_token(api_key)
                if user:
                    g.user = user
                    return func(*args, **kwargs)
        # next, try to login using Basic Auth
        api_key = request.headers.get('Authorization')
        if api_key:
            api_key = api_key.replace('Basic ', '', 1)
            try:
                api_key = base64.b64decode(api_key)
            except TypeError:
                pass
            user = User.verify_auth_token(api_key)
            if user:
                g.user = user
                return func(*args, **kwargs)

        # finally, return None if both methods did not login the user
        return Msg.authorized_failed()

    return decorated_view


def group_authority(func):
    @wraps(func)
    def decorated_view(*args, **kwargs):

        roles = g.user.roles
        if roles == ADMIN:
            return func(*args, **kwargs)
        elif roles == GROUP:
            return func(*args, **kwargs)
        else:
            return Msg.failed_dict(2001)

    return decorated_view


def admin_authority(func):
    @wraps(func)
    def decorated_view(*args, **kwargs):
        roles = g.user.roles
        if roles == ADMIN:
            return func(*args, **kwargs)
        else:
            return Msg.failed_dict(2001)

    return decorated_view