# -*- coding: utf-8 -*-

import os
from flask import Flask

def create_app(config_filepath='resource/config.cfg'):

    loginboard_app = Flask(__name__)

    # 환경설정 파일들 경로 설정
    from loginboard.loginboard_config import LoginboardConfig
    loginboard_app.config.from_object(LoginboardConfig)
    loginboard_app.config.from_pyfile(config_filepath, silent=True)

    # DB연동
    from loginboard.database import DBManager
    db_filepath = os.path.join(loginboard_app.root_path,
                               loginboard_app.config['DB_FILE_PATH'])
    db_url = loginboard_app.config['DB_URL'] + db_filepath
    DBManager.init(db_url, eval(loginboard_app.config['DB_LOG_FLAG']))
    DBManager.init_db()

    # 뷰함수가 있는 모듈을 임포트
    from loginboard.controller import main
    from loginboard.controller import register

    from loginboard.loginboard_blueprint import loginboard
    loginboard_app.register_blueprint(loginboard)

    return loginboard_app