"""
CREAT: 2017/12/10
AUTHOR:　HEHAHUTU
"""

from flask_cors import CORS

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


migrate = Migrate()

db = SQLAlchemy()

cors = CORS()


