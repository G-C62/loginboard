# -*- coding: utf-8 -*-

from loginboard.loginboard_blueprint import loginboard
from flask import render_template, redirect, url_for, request, flash, session, jsonify
from loginboard.model.user import User
from werkzeug import generate_password_hash
from loginboard.database import dao


def user_validation(register_request):

    user = None

    if len(register_request.form['username']) < 4 or len(register_request.form['username']) > 50:
        pass
    # 패스워드가 다른 경우
    elif register_request.form['password'] != register_request.form['checkpassword']:
        pass
    else:
        user = User(name=register_request.form['username'], password=generate_password_hash(register_request.form['password']))

    return user


def __get_user(username):
    try:
        current_user = dao.query(User). \
            filter_by(username=username). \
            first()

        return current_user

    except Exception as e:

        raise e

@loginboard.route('/user/check_name', methods=['POST'])
def check_name():
    username = request.json['username']
    #: DB에서 username 중복 확인
    if __get_user(username):
        return jsonify(result=False)
    else:
        return jsonify(result=True)

@loginboard.route('/register', methods=['POST'])
def register():


    register_user = user_validation(request)

    # 검사 통과시 DB에 insert 후 main으로 redirect
    if register_user:
        # insert
        try:
            dao.add(register_user)
            dao.commit()

        except Exception as e:
            error = "DB error occurs : " + str(e)
            dao.rollback()
            raise e

        else:
            flash(u'회원가입에 성공하였습니다 로그인 해주세요')
            return redirect(url_for('loginboard.main'))

    # 유효성검사 실패시
    flash(u'유효성 검사에 실패하셨습니다 다시 시도해주세요')

    return redirect(url_for('loginboard.main'))

