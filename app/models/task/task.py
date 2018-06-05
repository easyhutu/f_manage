"""
CREATE: 2018/5/16
AUTHOR:　HEHAHUTU
"""
from lib.database import Base, SurrogatePK
from sqlalchemy import Column, String, Integer, BOOLEAN, DATETIME
from sqlalchemy_utils.types.choice import ChoiceType
from app.extension import db
import uuid


class Tasks(Base, SurrogatePK):
    STATUS = (
        ('waiting', '等待中'),
        ('running', '执行中'),
        ('success', '成功'),
        ('failed', '失败'),

    )
    __tablename__ = 'f_task'
    id = Column(Integer, primary_key=True)
    task_name = Column(String(200), nullable=False)
    task_title = Column(String(1000))
    task_key = Column(String(100))
    is_run = Column(BOOLEAN, default=False)
    status = Column(ChoiceType(STATUS), default='waiting')
    user_id = Column(Integer)
    start_time = Column(DATETIME)
    end_time = Column(DATETIME)
    run_interval = Column(Integer)
    max_time = Column(Integer)

    def __init__(self, task_name, user_id, status, **kwargs):
        db.Model.__init__(self, task_name=task_name, user_id=user_id, status=status, **kwargs)
        self.set_task_key(task_name)

    def set_task_key(self, task_name):
        uid = uuid.uuid3(uuid.NAMESPACE_DNS, task_name)
        self.task_key = uid.hex
