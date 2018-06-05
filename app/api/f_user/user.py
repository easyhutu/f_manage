"""
CREATE: 2018/5/12
AUTHOR:　HEHAHUTU
"""
from flask_restful import Resource, reqparse, fields, marshal_with
from app.api import api
from app.models.admin.user import User
from lib.code import Msg
from settings import UPLOAD_PATH
import os


class HelloWorld(Resource):
    def get(self):
        return Msg.success('hello word')


user_parser = reqparse.RequestParser()
user_parser.add_argument('username')
user_parser.add_argument('email', type=str, required=True)
user_parser.add_argument('password', type=str, required=True)
user_get_parser = reqparse.RequestParser()
user_get_parser.add_argument('uid', help='uid is required', type=int, required=True)

user_fields = {
    'id': fields.Integer,
    'username': fields.String,
    'email': fields.String,
}


class CtlUser(Resource):
    @marshal_with(user_fields)
    def get(self, uid=None):
        arg = user_get_parser.parse_args()
        id = arg.get('uid')
        user = User.get_by_id(id)
        return user

    @marshal_with(user_fields)
    def post(self):
        arg = user_parser.parse_args()
        user = User.create(**arg)
        use_folder = user.use_folder
        os.mkdir(os.path.join(UPLOAD_PATH, use_folder))
        return user


class UpdateUser(Resource):
    @marshal_with(user_fields)
    def post(self):
        arg = user_parser.parse_args()
        user = User.update(**arg)
        return user


api.add_resource(HelloWorld, '/hello', endpoint='hello')
api.add_resource(CtlUser, '/user', endpoint='user')
