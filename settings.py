"""
CREAT: 2017/12/10
AUTHOR:　HEHAHUTU
"""
import os
import dotenv
from getenv import env

PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))  # This directory
try:
    dotenv_path = os.path.join(PROJECT_ROOT, '.env')
    dotenv.read_dotenv(dotenv_path)
except Exception as e:
    print('没有读取到本地环境变量配置，将使用预置的环境变量')
    print(e)

# 获取当前项目环境
DEFAULT_ENV = env('DEFAULT_ENV')

DB_URL = env('DB_URL')
SECRET_KEY = env('SECRET_KEY')

SERVER_NAME = env('SERVER_NAME', 'f_cloud')

CELERY_BROKER_URL = env('CELERY_BROKER_URL')
CELERY_RESULT_BACKEND = env('CELERY_RESULT_BACKEND')

# 上传文件根地址
UPLOAD_PATH = os.path.abspath(os.path.join(PROJECT_ROOT, 'upload_file'))
LOG_FOLDER = os.path.abspath(os.path.join(PROJECT_ROOT, 'app_log'))
LOG_PATH = os.path.abspath(os.path.join(LOG_FOLDER, 'cloud.log'))
LOG_LEVEL = 'info'
