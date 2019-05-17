# -*- coding: utf-8 -*-

from loginboard.loginboard_blueprint import loginboard
from flask import render_template

@loginboard.route('/')
@loginboard.route('/<userid>')
def main(userid=None):

    # user_id가 None이 아닌경우 로그인 여부 체크 후 로그인이 안된경우 로그인 페이지로 돌려버림
    return render_template('index.html', userid=userid)

