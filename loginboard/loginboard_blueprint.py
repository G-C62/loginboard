# -*- coding: utf-8 -*-

from flask import Blueprint

loginboard = Blueprint('loginboard', __name__,
                       template_folder='../templates', static_folder='../static')