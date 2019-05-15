# -*- coding: utf-8 -*-

import os
from flask import Flask

def create_app(config_filepath='resource/config.cfg'):

    loginboard_app = Flask(__name__)

    # 환경설정 파일들 경로 설정
    from loginboard.loginboard_config import LoginboardConfig
    loginboard_app.config.from_object(LoginboardConfig)
    loginboard_app.config.from_pyfile(config_filepath, silent=True)

    # 뷰함수가 있는 모듈을 임포트
    from loginboard.controller import helloworld

    from loginboard.loginboard_blueprint import loginboard
    loginboard_app.register_blueprint(loginboard)

    return loginboard_app