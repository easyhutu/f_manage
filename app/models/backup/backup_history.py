from app.extension import db
from lib.database import Base, SurrogatePK
from datetime import datetime


class BackupHistory(Base, SurrogatePK):
    __tablename__ = 'f_backup_history'
