# -*- coding: utf-8 -*-

from flask import render_template, url_for, request, redirect, flash
from flask import session

from . import auth
from flask_login import login_user, logout_user, login_required
from ..model.user import User
from ..database import dao
from ..controller.register import __get_user


# form 정보 유효성검사 함수
def form_validation():
    return True


@auth.route('/login', methods=['POST'])
def login():
    if form_validation():
        user = __get_user(request.form['username'])
        if user is not None and user.verify_password(request.form['password']):

            login_user(user, True)

            # 세션에 id넣기
            session['userid'] = user.id

            return redirect(request.args.get('next') or url_for('loginboard.login_main', userid=user.get_id()))
        flash(u'일치하는 회원정보가 없습니다')
    return render_template(url_for('loginboard.main'))


@auth.route('/logout')
def logout():
    logout_user()
    flash(u'로그아웃 되었습니다')
    return redirect(url_for('loginboard.main'))


