# -*- coding: utf-8 -*-

from sqlalchemy import Column, Integer, Float, String, ForeignKey, DateTime

from loginboard.model.user import User

from loginboard.model import Base


class Post(Base):
    __tablename__ = 'posts'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey(User.id))
    title = Column(String(100), unique=False)
    content = Column(String(400), unique=False)
    upload_date = Column(DateTime, unique=False)

    def __init__(self, user_id, title, content, upload_date):
        """Photo 모델 클래스를 초기화 한다."""

        self.user_id = user_id
        self.title = title
        self.content = content
        self.upload_date = upload_date

    def __repr__(self):
        """모델의 주요 정보를 출력한다."""

        return '<Photo %r %r %r>' % (self.user_id, self.title , self.upload_date)