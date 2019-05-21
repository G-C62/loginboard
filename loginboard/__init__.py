# -*- coding: utf-8 -*-

import os
from flask import Flask

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

    # DB연동
    from loginboard.database import DBManager
    db_filepath = os.path.join(loginboard_app.root_path,
                               loginboard_app.config['DB_FILE_PATH'])
    db_url = loginboard_app.config['DB_URL'] + db_filepath

    # sqlarchemy path
    db_path = os.path.join(os.path.dirname(__file__), 'app.db')
    db_uri = 'sqlite:///{}'.format(db_path)
    loginboard_app.config['SQLALCHEMY_DATABASE_URI'] = db_uri

    DBManager.init(db_url, eval(loginboard_app.config['DB_LOG_FLAG']))
    DBManager.init_db()

    # 뷰함수가 있는 모듈을 임포트
    from loginboard.controller import main
    from loginboard.controller import register

    from loginboard.loginboard_blueprint import loginboard
    loginboard_app.register_blueprint(loginboard)

    # 로그인 매니저 초기화
    login_manager.init_app(loginboard_app)

    # 로그인 관련 블루프린트 부착
    from .auth import auth as auth_blueprint
    loginboard_app.register_blueprint(auth_blueprint, url_prefix='/auth')

    return loginboard_app