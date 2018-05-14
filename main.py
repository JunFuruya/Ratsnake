#-*- UTF-8 -*-

# auth_basic を使う場合に、コメントを外す
#from bottle import auth_basic, get, post, redirect, request, response, run, static_file, template, TEMPLATE_PATH
from bottle import get, post, redirect, request, response, run, static_file, template, TEMPLATE_PATH

from app.service import ConfigGetService, SlackBotStartService

@get('/')
def index():
    # if user has not logged in, redirect to /login
    # redirect('/login')
    
    #entity = service.get_index_data
    tempalte_path = './template/index.html'
    #return template(tempalte_path, entity=entity)
    return template(tempalte_path)

@get('/admin')
def link_index():
    tempalte_path = './template/admin/index.html'
    return template(tempalte_path)

@get('/admin/login')
def admin_login():
    tempalte_path = './template/admin/login.html'
    return template(tempalte_path)

@post('/admin/login/complete')
def admin_login_complete():
    username = request.forms.get('username')
    password = request.forms.get('password')

    service = app.service.LoginService()
    if(service.is_authenticated(username, password)):
        redirect('/admin')
    else:
        tempalte_path = './template/admin/login.html'
        #entity
        return template(tempalte_path)
        #return template(tempalte_path, entity=entity) TODO: implement error message

@get('/admin/links')
def link_list():
    
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
    config = ConfigGetService().get_web_server_config()
    run(host=config.get_web_host(), port=config.get_web_port(), debug=config.get_debug(), reloader=config.get_reloader())
