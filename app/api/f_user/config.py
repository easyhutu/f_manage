"""
Author: Meng
Date: 2018/6/2
"""
from flask_restful import Resource
from app.api import api
from app.models.admin.config import FConfig, config_parse
from lib.principal.auth import admin_authority, auth_token
from flask_login import login_required
from lib.code import Msg
from datetime import datetime
from flask import g


class CrudConfig(Resource):
    @auth_token
    @admin_authority
    def post(self):
        arg = config_parse.parse_args()
        config = FConfig.query_one(server_name=arg['server_name'])
        if config:
            arg['update_time'] = datetime.now()
            config.update(**arg)
            arg['update_time'] = str(config.update_time)
            arg['create_time'] = str(config.create_time)
            return Msg.success('ok', config=arg)
        else:
            FConfig.create(**arg)
            return Msg.success('ok', config=arg)


api.add_resource(CrudConfig, '/config', endpoint='config')
