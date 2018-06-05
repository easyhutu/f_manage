"""
CREAT: 2017/12/9
AUTHOR:　HEHAHUTU
"""
from app.models.admin.user import User
from flask import Flask
from app.setting import (ProdConfig,
                         DevConfig,
                         UnittestConfig,
                         Config,
                         default_env)
from app.extension import (
    cors,
    db,
    migrate)
from app.api import api_blueprint
import flask_restful
from lib.resp_util import custom_abord
from settings import UPLOAD_PATH, LOG_FOLDER, CELERY_BROKER_URL, CELERY_RESULT_BACKEND
import os

if default_env == 'PRODUCTION':
    defaultConfig = ProdConfig
elif default_env == 'STAGE':
    defaultConfig = DevConfig
elif default_env == 'UNITTEST':
    defaultConfig = UnittestConfig
else:
    raise Exception('未成功读取配置信息！')


# print(defaultConfig.DEBUG)


# 构建核心对象app 函数
def create_app(config_object=defaultConfig):
    init_setting()
    app = Flask(__name__)

    app.config.from_object(config_object)
    # print(app.config)
    register_extensions(app)
    register_blueprints(app)
    # init_service(app)
    flask_restful.abort = custom_abord

    return app


# 注册辅助工具
def register_extensions(app):
    migrate.init_app(app, db)
    db.init_app(app)
    cors.init_app(app)


# 注册蓝图函数
def register_blueprints(app):
    app.register_blueprint(api_blueprint)


# 初始化配置信息
def init_setting():
    if not os.path.exists(UPLOAD_PATH):
        print('now mkdir {}'.format(UPLOAD_PATH))
        os.mkdir(UPLOAD_PATH)

    if not os.path.exists(LOG_FOLDER):
        print('now mkdir {}'.format(LOG_FOLDER))
        os.mkdir(LOG_FOLDER)

