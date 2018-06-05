"""
Author: Meng
Date: 2018/6/4
"""
from app.extension import db
from lib.database import Base, SurrogatePK
from datetime import datetime


class Backup(Base, SurrogatePK):
    __tablename__ = 'f_backup'
    id = db.Column(db.Integer, primary_key=True)
    show_name = db.Column(db.String(500))
    file_name = db.Column(db.String(500))
    file_size = db.Column(db.INTEGER)
    user_id = db.Column(db.INTEGER)
    is_trash = db.Column(db.INTEGER)
    is_share = db.Column(db.INTEGER)
    create_time = db.Column(db.DATETIME, default=datetime.now())

    def __init__(self, show_name, file_name, file_size, **kwargs):
        db.Model.__init__(self, show_name=show_name, file_name=file_name, file_size=file_size, **kwargs)
