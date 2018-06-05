"""
Author: Meng
Date: 2018/6/4
"""
from main import f_celery
from .upload_file import upload_file


@f_celery.task
def back_up_task(value_json: dict):
    stat = upload_file(value_json)
    if stat == 'ok':
        pass
    else:
        pass
