#-*- UTF-8 -*-

from bottle import auth_basic, get, post, redirect, request, response, run, static_file, template, TEMPLATE_PATH

import mysql.connector
import app.service

config = app.service.configGetService()

@get('/')
def index():
    # if user has not logged in, redirect to /login
    # redirect('/login')
    
    #entity = service.get_index_data
    tempalte_path = './template/index.html'
    #return template(tempalte_path, entity=entity)
    return template(tempalte_path)

@get('/login')
#@auth_basic(check)
def login():
    name = 'login'
    return template('<html><body>{{name}}</body></html>', name=name)

@get('/admin')
def link_index():
    tempalte_path = './template/admin/index.html'
    return template(tempalte_path)

@get('/admin/links')
def link_list():
    #check_login()
    sql = 'SELECT * FROM links limit 10'

    #connect = mysql.connector.connect(db=db_name, host=db_host, port=db_port, user=db_user, passwd=db_pass)
    #cur.execute(sql)
    
    link_list = [
        [1, 'AAA', 'http://aaa.co.jp'],
        [2, 'BBB', 'http://bbb.co.jp'],
        [3, 'CCC', 'http://ccc.co.jp']
    ]
    tempalte_path = './template/admin/links/list.html'
    return template(tempalte_path, link_list=link_list)

@get('/admin/links/create')
def link_create():
    html = '<html><body>create</body></html>'
    tempalte_path = './template/admin/links/list.html'
    return template(html)

@post('/admin/links/update')
def link_update():
    html = '<html><body>update</body></html>'
    return template(html)

@post('/admin/links/confirm')
def link_confirm():
    html = '<html><body>confirm</body></html>'
    return template(html)

@post('/admin/links/complete')
def link_complete():
    html = '<html><body>complete</body></html>'
    return template(html)

@get('/public/<path:path>')
def callback(path):
    return static_file(path, root='./public/')

#@error(404)
#def error(404):
#    return '404error'

#@error(500)
#def error(500):
#    return '500error'

if __name__ == "__main__":
    run(host=config.get_web_host(), port=config.get_web_port(), debug=config.get_debug(), reloader=config.get_reloader())
