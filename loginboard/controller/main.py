# -*- coding: utf-8 -*-

from loginboard.loginboard_blueprint import loginboard
from flask import render_template, redirect, url_for
from flask_login import login_required, current_user

@loginboard.route('/')
def main():
    if hasattr(current_user, 'username'):
        return redirect(url_for('loginboard.login_main', userid=current_user.username))
    return render_template('index.html')


@loginboard.route('/member/<userid>')
@login_required
def login_main(userid):
    return render_template('index.html', userid=userid)

