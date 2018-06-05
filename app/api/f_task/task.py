"""
CREATE: 2018/5/16
AUTHOR:　HEHAHUTU
"""
from flask_restful import Resource
from app.api import api
from flask_login import login_required
from lib.code import Msg


class TaskOperation(Resource):
    @login_required
    def get(self):
        return Msg.success('success')


api.add_resource(TaskOperation, '/task', endpoint='task')
