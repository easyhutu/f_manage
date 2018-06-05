"""
CREATE: 2018/5/16
AUTHOR:　HEHAHUTU
"""
from lib.database import Base, SurrogatePK
from sqlalchemy import Column, Integer
from app.extension import db


class TaskShip(Base, SurrogatePK):
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer)
    task_id = Column(Integer)
    task_info_id = Column(Integer)

    def __init__(self, user_id, task_id, **kwargs):
        db.Model.__init__(self, user_id=user_id, task_id=task_id, **kwargs)
