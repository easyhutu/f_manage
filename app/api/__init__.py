"""
CREAT: 2017/12/9
AUTHOR:　HEHAHUTU
"""
from flask import Blueprint
from flask_restful import Api, fields

api_blueprint = Blueprint("api", __name__, url_prefix='/x')

errors = {
    'UserAlreadyExistsError': {
        'message': "A user with that username already exists.",
        'status': 409,
    },
    'ResourceDoesNotExist': {
        'message': "A resource with that ID no longer exists.",
        'status': 410,
        'extra': "Any extra information you want.",
    },
}
api = Api(api_blueprint, errors=errors)

from .f_user import *
from .f_task import *
from .f_cloud import *
from .f_backup import *
