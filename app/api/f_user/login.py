"""
CREATE: 2018/5/13
AUTHOR:　HEHAHUTU
"""
from flask_restful import Resource, reqparse
from app.api import api
from app.models.admin.user import User
from flask import request
from lib.code import Msg


login_parse = reqparse.RequestParser()
login_parse.add_argument('username', type=str, help='username is required', required=True)
login_parse.add_argument('password', type=str, help='password is required', required=True)


def next_is_valid(next: str):
    if next is None:
        return True
    else:
        if next.startswith('http'):
            return True
        else:
            return


class LoginUser(Resource):
    def post(self):
        arg = login_parse.parse_args()

        user = User.query.filter_by(username=arg.get('username')).first()
        if user:
            if user.check_password(arg.get('password')):
                next = request.args.get('next')
                # next_is_valid should check if the user has valid
                # identity_changed.send(current_app._get_current_object(), identity=Identity(user.id))
                # permission to access the `next` url
                if not next_is_valid(next):
                    return {'message': 'next url valid failed'}, 400
                return Msg.success('登录成功', assess_key=user.generate_auth_token())
            else:
                return Msg.login_password_error('用户名和密码不匹配')
        else:
            return Msg.login_username_error('用户名不存在')


class LogoutUser(Resource):

    def post(self):
        return Msg.success('logout success')


api.add_resource(LoginUser, '/login', endpoint='login')
api.add_resource(LogoutUser, '/logout', endpoint='logout')
