"""
CREATE: 2018/5/29
AUTHOR:　HEHAHUTU
"""
from lib.database import Base, SurrogatePK
from sqlalchemy_utils.types.choice import ChoiceType
from app.extension import db
from .user import ROLES, NORMAL
from flask_restful import reqparse
from datetime import datetime
import os


class FConfig(Base, SurrogatePK):
    __tablename__ = 'f_config'

    id = db.Column(db.Integer, primary_key=True)
    server_name = db.Column(db.String(100))
    is_register = db.Column(db.Integer)
    default_reg_role = db.Column(ChoiceType(ROLES), default=NORMAL)
    backup_ip = db.Column(db.String(100))
    backup_port = db.Column(db.Integer)
    backup_base_path = db.Column(db.String(500))
    update_time = db.Column(db.DATETIME)
    create_time = db.Column(db.DATETIME, default=datetime.now())

    def __init__(self, server_name, is_register, **kwargs):
        db.Model.__init__(self, server_name=server_name, is_register=is_register, **kwargs)

    def __repr__(self):
        return f"""
        config register: {self.is_register}\n 
        default reg role: {self.default_reg_role}\n
        backup ip: {self.backup_ip}:{self.backup_port}
        """

    def set_backup_base_path(self):
        if not os.path.exists(self.backup_base_path):
            try:
                os.mkdir(self.backup_base_path)
            except:
                raise IOError(f'mkdir {self.backup_base_path} failed')


config_parse = reqparse.RequestParser()
config_parse.add_argument('server_name', type=str, required=True)
config_parse.add_argument('is_register', type=int, required=True)
config_parse.add_argument('default_reg_role', type=str, choices=[key[0] for key in ROLES])
config_parse.add_argument('backup_ip', type=str)
config_parse.add_argument('backup_port', type=str)
config_parse.add_argument('backup_base_path', type=str)
