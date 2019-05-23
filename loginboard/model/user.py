# -*- coding: utf-8 -*-

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from loginboard.model import Base
from werkzeug.security import check_password_hash
from ..database import dao
from .. import login_manager



class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String(50), unique=True)
    password = Column(String(55), unique=False)

    posts = relationship('Post',
                          backref='user',
                          cascade='all, delete, delete-orphan')


    def __init__(self, name,  password):
        self.username = name
        self.password = password

    def __repr__(self):
        return '<User %r %r %r>' % (self.id, self.username, self.password)

    # 비밀번호 일치 여부 함수
    def verify_password(self, password):
        return check_password_hash(self.password, password)

    def is_authenticated(self):
        return self.authenticated

    def is_active(self):
        return True

    def is_anonymous(self):
        return False


    def get_id(self):
        return self.username


# 사용자 로더 콜백 함수
@login_manager.user_loader
def load_user(user_id):
    user = dao.query(User).\
        filter_by(username=user_id).\
        first()
    return user
