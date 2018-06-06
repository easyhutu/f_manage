from app.extension import db
from lib.database import Base, SurrogatePK
from datetime import datetime
from sqlalchemy_utils.types import ChoiceType


class BackupHistory(Base, SurrogatePK):
    STAT = (
        ('success', '备份成功'),
        ('failed', '备份失败'),
    )
    __tablename__ = 'f_backup_history'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer)
    backup_stat = db.Column(ChoiceType(STAT), default=STAT[0][0])
    backup_id = db.Column(db.Integer)
    path = db.Column(db.String(500))
    show_name = db.Column(db.String(500))
    file_name = db.Column(db.String(300))
    failed_msg = db.Column(db.String(1000))
    create_time = db.Column(db.DATETIME, default=datetime.now())

    def __init__(self, user_id, backup_stat, backup_id, **kwargs):
        db.Model.__init__(self, user_id=user_id, backup_stat=backup_stat, backup_id=backup_id, **kwargs)