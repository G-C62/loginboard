from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from loginboard.model import Base

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String(50), unique=True)
    password = Column(String(55), unique=False)

    def __init__(self, name,  password):
        self.username = name
        self.password = password

    def __repr__(self):
        return '<User %r %r %r>' % (self.id, self.username, self.password)