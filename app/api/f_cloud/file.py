"""
CREATE: 2018/5/26
AUTHOR:　HEHAHUTU
"""

from app.models.cloud.folder import DiskFile
from flask_restful import Resource, reqparse
from app.api import api
from lib.principal.auth import auth_token
from werkzeug.datastructures import FileStorage
from lib.code import Msg
from flask import g
from settings import UPLOAD_PATH
import os
from lib.celerys.backup_file import back_up_task

class CreateFile(Resource):
    folder_parse = reqparse.RequestParser()
    # folder_parse.add_argument('event', required=True, type=str)
    folder_parse.add_argument('file_data', required=True, type=FileStorage, location='files')
    folder_parse.add_argument('group_id', required=True, type=int)
    folder_parse.add_argument('group_path', required=True, type=str)

    @auth_token
    def post(self):
        user_id = g.user.id
        arg = self.folder_parse.parse_args()
        arg['user_id'] = user_id
        file = arg['file_data']
        arg.pop('file_data')
        file_data = file.read()
        file_size = len(file_data) / 1024
        check_size = True if g.user.max_size > (g.user.use_size + file_size) else False
        if check_size:
            arg['file_size'] = file_size
            arg['show_name'] = file.filename
            file_obj = DiskFile(**arg)
            filename = file_obj.file_name
            save_path = os.path.join(UPLOAD_PATH, g.user.use_folder)
            path = os.path.join(save_path, filename)
            file.save(path)
            file_obj.save()
            arg['path'] = path
            back_up_task.apply_async(args=[arg, ], countdown=60*5)

            return Msg.success('ok')
        else:
            return Msg.failed_dict(1001)


class UpdateFile(Resource):
    parse = reqparse.RequestParser()
    parse.add_argument('show_name')
    parse.add_argument('id')

    @auth_token
    def post(self):
        arg = self.parse.parse_args()
        file = DiskFile.query_one(id=arg['id'], user_id=g.user.id)
        if file:
            file.update(**arg)
            return Msg.success('ok')
        else:
            return Msg.failed_dict(1002)


# 此处删除为逻辑删除
class DeleteFile(Resource):
    parse = reqparse.RequestParser()
    parse.add_argument('id', type=int, required=True)

    @auth_token
    def post(self):
        arg = self.parse.parse_args()
        file = DiskFile.query_one(id=arg['id'], user_id=g.user.id)
        if file:
            file.update(id=arg['id'], is_trash=1)
            return Msg.success('ok')
        else:
            return Msg.failed_dict(1002)


api.add_resource(CreateFile, '/file/add', endpoint='c_file')
api.add_resource(UpdateFile, '/file/update', endpoint='u_file')
api.add_resource(DeleteFile, '/file/delete', endpoint='d_file')
