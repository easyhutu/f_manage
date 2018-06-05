"""
Author: Meng
Date: 2018/6/3
"""
from app.models.backup.backup_file import Backup
from app.models.admin.config import FConfig
from flask_restful import Resource, reqparse
from app.api import api
from lib.principal.auth import auth_token, admin_authority
from werkzeug.datastructures import FileStorage
from lib.code import Msg
from flask import g
from settings import SERVER_NAME
import os


class BackupFiles(Resource):
    folder_parse = reqparse.RequestParser()
    # folder_parse.add_argument('event', required=True, type=str)
    folder_parse.add_argument('file_data', required=True, type=FileStorage, location='files')
    folder_parse.add_argument('show_name', required=True, type=int)
    folder_parse.add_argument('file_name', required=True, type=int)
    folder_parse.add_argument('file_size', required=True, type=str)
    folder_parse.add_argument('user_id', required=True, type=str)
    folder_parse.add_argument('is_share', required=True, type=str)

    @admin_authority
    @auth_token
    def post(self):
        arg = self.folder_parse.parse_args()
        ad_config = FConfig.query_one(server_name=SERVER_NAME)
        backup_base_path = ad_config.backup_base_path
        path = os.path.join(backup_base_path, arg['file_name'])
        file = arg['file_data']
        file.save(path)
        arg['path'] = path
        arg.pop('file_data')
        Backup.create(**arg)
        return Msg.success('ok', filename=arg['file_name'])


api.add_resource(BackupFiles, '/backup', endpoint='backup')
