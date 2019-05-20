# -*- coding: utf-8 -*-

class LoginboardConfig(object):
    #: 데이터베이스 연결 URL
    DB_URL= 'sqlite:///'
    #: 데이터베이스 파일 경로
    DB_FILE_PATH = 'resource/database/loginboard.sqlite'
    #: 디폴트 SQLAlchemy trace log 설정
    DB_LOG_FLAG = 'True'
    #: 업로드되는 사진의 최대 크키(3메가)
    MAX_CONTENT_LENGTH = 10 * 1024 * 1024
    #: 세션 타임아웃은 초(second) 단위(60분)
    PERMANENT_SESSION_LIFETIME = 60 * 60
    #: 쿠기에 저장되는 세션 쿠키
    SESSION_COOKIE_NAME = 'loginboard_session'
    #: SESSION SECRET KEY
    SECRET_KEY = 'PG13'
