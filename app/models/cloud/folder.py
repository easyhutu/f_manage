"""
CREATE: 2018/5/26
AUTHOR:　HEHAHUTU
"""
from lib.database import Base, SurrogatePK
from app.extension import db
from datetime import datetime
import uuid
import os

"""
folder_path : 文件路径
group_id： 所属文件夹id
user_id： 所属用户id
user_group：该文件是否向用户组开放
"""


class DiskFolder(Base, SurrogatePK):
    __tablename__ = 'f_folder'
    id = db.Column(db.INTEGER, primary_key=True)
    folder_name = db.Column(db.String(500))
    folder_path = db.Column(db.String(1000))
    group_id = db.Column(db.INTEGER)
    user_id = db.Column(db.INTEGER)
    is_trash = db.Column(db.INTEGER, default=0)
    is_share = db.Column(db.INTEGER, default=0)
    is_user_group = db.Column(db.INTEGER)
    create_time = db.Column(db.DATETIME, default=datetime.now())
    update_time = db.Column(db.DATETIME)

    def __init__(self, folder_name, folder_path, group_id, user_id, **kwargs):
        db.Model.__init__(self, folder_name=folder_name, folder_path=folder_path, group_id=group_id, user_id=user_id,
                          **kwargs)


"""
file_size : K
"""


class DiskFile(Base, SurrogatePK):
    __tablename__ = 'f_file'
    id = db.Column(db.INTEGER, primary_key=True)
    show_name = db.Column(db.String(500))
    file_name = db.Column(db.String(500))
    file_size = db.Column(db.INTEGER)
    group_path = db.Column(db.String(1000))
    group_id = db.Column(db.INTEGER)
    user_id = db.Column(db.INTEGER)
    is_trash = db.Column(db.INTEGER)
    is_share = db.Column(db.INTEGER)
    is_user_group = db.Column(db.INTEGER)
    create_time = db.Column(db.DATETIME, default=datetime.now())
    update_time = db.Column(db.DATETIME)

    def __init__(self, show_name, group_path, group_id, user_id, **kwargs):
        db.Model.__init__(self, show_name=show_name, group_path=group_path, group_id=group_id, user_id=user_id, **kwargs)
        self.set_filename(show_name)

    def set_filename(self, show_name):
        f, ex = os.path.splitext(show_name)
        new_filename = uuid.uuid3(uuid.NAMESPACE_DNS, show_name).hex + ex
        self.file_name = new_filename
