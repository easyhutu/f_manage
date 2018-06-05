"""
CREATE: 2018/5/26
AUTHOR:　HEHAHUTU
"""

from app.models.cloud.folder import DiskFolder
from flask_restful import Resource, reqparse
from app.api import api
from lib.principal.auth import auth_token

from lib.code import Msg
from flask import g


class CreateFolder(Resource):
    folder_parse = reqparse.RequestParser()
    # folder_parse.add_argument('event', required=True, type=str)
    folder_parse.add_argument('folder_name', required=True, type=str)
    folder_parse.add_argument('group_id', required=True, type=int)
    folder_parse.add_argument('folder_path', required=True, type=str)

    @auth_token
    def post(self):
        user_id = g.user.id
        arg = self.folder_parse.parse_args()
        arg['user_id'] = user_id
        print(arg)
        folder = DiskFolder.create(**arg)
        return Msg.success('ok', id=folder.id)


class UpdateFolder(Resource):
    parse = reqparse.RequestParser()
    parse.add_argument('folder_name')
    parse.add_argument('id')

    @auth_token
    def post(self):
        arg = self.parse.parse_args()
        folder = DiskFolder.get_by_id(arg['id'])
        if folder:
            print(arg)
            folder.update(**arg)
            return Msg.success('ok')
        else:
            return Msg.failed_dict(1002)


class DeleteFolder(Resource):
    parse = reqparse.RequestParser()
    parse.add_argument('id', type=int, required=True)

    @auth_token
    def post(self):
        arg = self.parse.parse_args()
        folder = DiskFolder.get_by_id(**arg)
        if folder:
            folder.delete()
            return Msg.success('ok')
        else:
            return Msg.failed_dict(1002)


api.add_resource(CreateFolder, '/folder/add', endpoint='c_folder')
api.add_resource(UpdateFolder, '/folder/update', endpoint='u_folder')
api.add_resource(DeleteFolder, '/folder/delete', endpoint='d_folder')
