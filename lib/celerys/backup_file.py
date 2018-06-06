"""
Author: Meng
Date: 2018/6/4
"""
from main import f_celery
from .upload_file import upload_file
from app.models.backup.backup_file import Backup
from app.models.backup.backup_history import BackupHistory


@f_celery.task
def back_up_task(value_json: dict):
    stat = upload_file(value_json)
    backup = Backup.create(**value_json)
    value_json.pop('file_size')
    value_json['backup_id'] = backup.id
    if stat == 'ok':
        value_json['backup_stat'] = 'success'
    else:
        value_json['backup_stat'] = 'failed'
        value_json['failed_msg'] = str(stat)

    BackupHistory.create(**value_json)

