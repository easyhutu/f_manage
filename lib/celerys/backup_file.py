"""
Author: Meng
Date: 2018/6/4
"""
from main import f_celery


@f_celery.task()
def back_up():
    return
