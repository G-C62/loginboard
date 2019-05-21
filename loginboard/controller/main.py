# -*- coding: utf-8 -*-

from loginboard.loginboard_blueprint import loginboard
from flask import render_template
from flask_login import login_required


@loginboard.route('/')
def main():
    return render_template('index.html')


@loginboard.route('/member/<userid>')
@login_required
def login_main(userid):
    return render_template('index.html', userid=userid)
