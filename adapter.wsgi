# coding: utf-8

#def application(environ, start_response):
#
#    start_response('200 OK', [('Content-type', 'text/plain')])
#
#    return 'Hello, world'

#mport sys, os
import bottle

dirpath = os.path.dirname(os.path.abspath(__file__))
sys.path.append(dirpath)
os.chdir(dirpath)

import main
application = bottle.default_app()
