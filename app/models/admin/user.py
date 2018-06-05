"""
CREATE: 2018/5/6
AUTHOR:　HEHAHUTU
"""
from werkzeug.security import generate_password_hash, check_password_hash
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from itsdangerous import BadSignature, SignatureExpired
from settings import SECRET_KEY
from app.extension import db
from lib.database import Base, SurrogatePK
from sqlalchemy import Column, String, Integer
from sqlalchemy_utils.types.choice import ChoiceType
from flask_login import UserMixin
import time
from lib.hash import hash_sha256


# 定义相关角色
NORMAL = "NORMAL"
GROUP = "GROUP"
ADMIN = "ADMIN"
ROLES = (
    ('LIMIT', "受限用户"),
    ("NORMAL", "普通用户"),
    ("GROUP", "群组用户"),
    ("ADMIN", "管理员"),
)


class User(SurrogatePK, Base):
    __tablename__ = "s_user"
    id = Column(Integer, primary_key=True)
    username = Column(String(16))
    email = db.Column(db.String(200))
    email_stat = db.Column(db.Integer)
    password_hash = db.Column(db.String(500), nullable=False)
    assess_key = db.Column(db.String(500))
    roles = Column(ChoiceType(ROLES), default=NORMAL)
    last_name = db.Column(db.String(100), nullable=True)
    phone = db.Column(db.String(20))
    phone_stat = db.Column(db.Integer)
    use_folder = db.Column(db.String(500))
    max_size = db.Column(db.Integer, default=1024 * 1024 * 1024)
    use_size = db.Column(db.Integer, default=0)

    def __init__(self, username, email, password, **kwargs):
        db.Model.__init__(self, username=username, email=email,
                          password=password, **kwargs)
        self.set_password(password)
        self.set_assess_key(username, password)
        self.set_use_folder(username)

    @property
    def password(self):
        return None

    @password.setter
    def password(self, password):
        self.set_password(password)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, value):
        return check_password_hash(self.password_hash, value)

    def set_assess_key(self, username, password):
        self.assess_key = hash_sha256('{};{};{}'.format(username, password, str(time.time())))

    def set_use_folder(self, username):
        self.use_folder = hash_sha256('{};{}'.format(username, str(time.time())))

    @property
    def full_name(self):
        return '%s %s' % (self.first_name, self.last_name)

    def generate_auth_token(self, expiration=600):
        s = Serializer(SECRET_KEY, expires_in=expiration)
        return s.dumps({'id': self.id}).decode()

    @staticmethod
    def verify_auth_token(token):
        s = Serializer(SECRET_KEY)
        try:
            data = s.loads(token)
        except SignatureExpired:
            return None  # valid token, but expired
        except BadSignature:
            return None  # invalid token
        user = User.query.get(data['id'])
        if user:
            return user
        return None



