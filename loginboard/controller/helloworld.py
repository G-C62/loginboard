# -*- coding: utf-8 -*-

from loginboard.loginboard_blueprint import loginboard

@loginboard.route('/hello')
def hello_flask():
    return 'hello world'

