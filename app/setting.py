"""
CREAT: 2017/12/14
AUTHOR:　HEHAHUTU
"""
import os
import yaml
from settings import (PROJECT_ROOT,
                      SECRET_KEY,
                      DEFAULT_ENV,
                      DB_URL,
                      CELERY_RESULT_BACKEND,
                      CELERY_BROKER_URL)

default_env = DEFAULT_ENV
# 拼接绝对路径的配置文件地址
#config_path = os.path.join(PROJECT_ROOT, 'config.yaml')

# 加载配置文件
#config = yaml.load(open(config_path, encoding='utf8'))[default_env]


class Config(object):
    APP_DIR = os.path.abspath(os.path.dirname(__file__))
    PROJECT_ROOT = PROJECT_ROOT

    ERROR_404_HELP = False
    SECRET_KEY = SECRET_KEY
    OPBEAT = {
        'SECRET_TOKEN': SECRET_KEY,
        'INCLUDE_PATHS': ['S_MANAGER']

    }


class ProdConfig(Config):
    """Production configuration."""

    ENV = 'PRODUCTION'
    DEBUG = False


class DevConfig(Config):
    """开发&预发布环境"""
    ENV = 'STAGE'
    DEBUG = True
    # MONGO_URL = 'mongodb://test:test123@39.106.2.119:27017/dev_task'


class UnittestConfig(Config):
    """测试环境配置"""

    ENV = 'UNITTEST'
    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_DATABASE_URI = DB_URL
    CELERY_RESULT_BACKEND = CELERY_RESULT_BACKEND
    CELERY_BROKER_URL = CELERY_BROKER_URL
