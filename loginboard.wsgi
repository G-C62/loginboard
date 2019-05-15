# -*- coding: utf-8 -*-

import sys
sys.path.insert(0, '/home/c62/test/loginboard')

from loginboard import create_app
application = create_app('/home/c62/test/loginboard/loginboard/resource/config.cfg')