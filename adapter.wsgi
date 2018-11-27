# -*- coding: UTF-8 -*-

import sys, os, import bottle

dirpath = os.path.dirname(os.path.abspath(__file__))
sys.path.append(dirpath)
os.chdir(dirpath)

import main
from app import *
from beaker.middleware import SessionMiddleware


session_opts = {
    'session.type': 'file',
    'session.cookie_expires': 300,
    'session.data_dir': './data',
    'session.auto': True
}
application = SessionMiddleware(bottle.default_app(), session_opts)