# -*- coding: utf-8 -*-

import os
from flask import Flask
from flask_session import Session
from datetime import datetime, timedelta
from flask_sqlalchemy import SQLAlchemy


# Flask-login초기화
from flask_login.login_manager import LoginManager


login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'

def create_app():

    loginboard_app = Flask(__name__)

    # 환경설정 파일들 경로 설정
    from loginboard.loginboard_config import LoginboardConfig
    loginboard_app.config.from_object(LoginboardConfig)



    db_filepath = os.path.join(loginboard_app.root_path,
                               loginboard_app.config['DB_FILE_PATH'])
    db_url = loginboard_app.config['DB_URL'] + db_filepath

    # db_url 생성 후 설정변수에 할당
    loginboard_app.config['SQLALCHEMY_DATABASE_URI'] = db_url

    # sqlalchemy 인스턴스를 값으로 할당
    db = SQLAlchemy(loginboard_app)

    # SESSION_SQLALCHEMY 를 SQLAlchemy 인스턴스로 할당
    loginboard_app.config['SESSION_SQLALCHEMY'] = db

    # flask-session객체 생성
    session = Session(loginboard_app)

    # session 유지 시간설정
    loginboard_app.permanent_session_lifetime = timedelta(minutes=10)

    # session 테이블을 생성해줌
    session.app.session_interface.db.create_all()

    # DB연동
    from loginboard.database import DBManager


    DBManager.init(db_url, eval(loginboard_app.config['DB_LOG_FLAG']))
    DBManager.init_db()



    # 뷰함수가 있는 모듈을 임포트
    from loginboard.controller import main
    from loginboard.controller import register
    from loginboard.controller import board

    from loginboard.loginboard_blueprint import loginboard
    loginboard_app.register_blueprint(loginboard)

    # 로그인 매니저 초기화
    login_manager.init_app(loginboard_app)

    # 로그인 관련 블루프린트 부착
    from .auth import auth as auth_blueprint
    loginboard_app.register_blueprint(auth_blueprint, url_prefix='/auth')




    from loginboard.database import dao
    # http respone가 생성된 후 호출
    @loginboard_app.teardown_request
    def db_close(exception=None):
        try:
            dao.remove()
        except Exception as e:
            print e

    return loginboard_app