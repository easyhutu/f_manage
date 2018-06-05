"""
Author: Meng
Date: 2018/6/3
"""
from app.models.backup.backup_file import Backup
from flask_restful import Resource, reqparse
from app.api import api
from lib.principal.auth import auth_token
from werkzeug.datastructures import FileStorage
from lib.code import Msg
from flask import g
from settings import UPLOAD_PATH, SERVER_NAME
import os


class BackupFiles(Resource):
    folder_parse = reqparse.RequestParser()
    # folder_parse.add_argument('event', required=True, type=str)
    folder_parse.add_argument('file_data', required=True, type=FileStorage, location='files')
    folder_parse.add_argument('show_name', required=True, type=int)
    folder_parse.add_argument('file_size', required=True, type=str)
    folder_parse.add_argument('user_id', required=True, type=str)
    folder_parse.add_argument('is_share', required=True, type=str)
