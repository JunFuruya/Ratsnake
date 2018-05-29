# -*- coding: utf-8 -*-

from beaker.middleware import SessionMiddleware
from bottle import app, error, get, jinja2_template, post, redirect, request, response, run, static_file, TEMPLATE_PATH

from app.helper.helper import HashHelper
from app.service.web_service import ConfigGetService
from app.service.web_service import LoginService
from app.service.web_service import SlackBotStartService

config = ConfigGetService().get_web_server_config()

@get('/')
def get_index():
    # TODO: username取得
    check_login_status('admin')
        
    #entity = service.get_index_data
    tempalte_path = './template/index.html'
    #return jinja2_template(tempalte_path, entity=entity)
    return jinja2_template(tempalte_path)
    
@get('/admin')
def get_link_index():
    # TODO: username取得
    check_login_status('admin')
    
    from app.entity.admin.index_entity import IndexEntity
    index_entity = IndexEntity()
    index_entity.set_title('Hideout Login')
    index_entity.set_description('Hideout Main Page')
    index_entity.set_notification('This is the index page.')
    tempalte_path = './template/admin/index.html'
    return jinja2_template(tempalte_path, entity=index_entity)

@get('/admin/login')
def get_admin_login():
    service = LoginService()
    # TODO: a factory class should return entity through a service class 
    from app.entity.admin.login_entity import LoginEntity
    login_entity = LoginEntity()
    login_entity.set_title('Hideout Main Page')
    login_entity.set_description('Hideout Login Page')
    login_entity.set_notification('Please enter your id and password.')
    tempalte_path = './template/admin/login.html'
    return jinja2_template(tempalte_path, entity=login_entity)

@get('/admin/login/complete')
def get_admin_login_complete():
    redirect('/admin/index') # In case that users press F5 key
    pass

@get('/admin/logout')
def get_admin_login_complete():
    session = request.environ.get('beaker.session')
    session[HashHelper.hexdigest('login')] = ''
    session.save()
    return redirect('/admin/login')

@post('/admin/login/complete')
def post_admin_login_complete():
    username = request.forms.get('username')
    password = request.forms.get('password')

    # TODO:validate the parameters
    
    service = LoginService()
    if(service.is_authenticated(username, password)):
        session = request.environ.get('beaker.session')
        session['login'] = HashHelper.hexdigest(username)
        session[HashHelper.hexdigest('login')] = HashHelper.hexdigest(username)
        session.save()

        # TODO: move max_age to config file
        #max_age = 60 * 60 * 24 * 30 # 1Month
        #response.set_cookie(cookie_key, cookie_value, max_age=max_age)
        return redirect('/admin')
        
    else:
        from app.entity.admin.login_entity import LoginEntity
        login_entity = LoginEntity()
        login_entity.set_title('Hideout Login')
        login_entity.set_description('Hideout Login Page')
        login_entity.set_notification('Please enter your id and password.')
        login_entity.set_error_message('The information is incorrect. Please check the input.')
        
        tempalte_path = './template/admin/login.html'
        return jinja2_template(tempalte_path, entity=login_entity)

@get('/admin/links')
def get_link_list():
    check_login_status('admins')
    link_list = [
        [1, 'AAA', 'http://aaa.co.jp'],
        [2, 'BBB', 'http://bbb.co.jp'],
        [3, 'CCC', 'http://ccc.co.jp']
    ]
    tempalte_path = './template/admin/links/list.html'
    return jinja2_template(tempalte_path, link_list=link_list)

@get('/admin/links/create')
def get_link_create():
    html = '<html><body>create</body></html>'
    tempalte_path = './template/admin/links/list.html'
    return jinja2_template(html)

@post('/admin/links/update')
def post_link_update():
    html = '<html><body>update</body></html>'
    return jinja2_template(html)

@post('/admin/links/confirm')
def post_link_confirm():
    html = '<html><body>confirm</body></html>'
    return jinja2_template(html)

@post('/admin/links/complete')
def post_link_complete():
    html = '<html><body>complete</body></html>'
    return jinja2_template(html)

@get('/public/<path:path>')
def get_static_file(path):
    return static_file(path, root='./public/')

@error(404)
def error404(error):
    from app.entity.error_entity import ErrorEntity
    error_entity = ErrorEntity()
    error_entity.set_http_status(404)
    error_entity.set_user_error_message('')
    error_entity.set_title('404 Error')
    error_entity.set_description('We can\'t find the page. Please check the URL.')
    
    tempalte_path = './template/front/error.html'
    return jinja2_template(tempalte_path, entity=error_entity)
    
@error(500)
def error500(error):
    from app.entity.error_entity import ErrorEntity
    error_entity = ErrorEntity()
    error_entity.set_http_status(500)
    error_entity.set_user_error_message('')
    error_entity.set_title('500 Error')
    error_entity.set_description('Something is wrong. We\'ll fix it as soon as possible.')
    
    tempalte_path = './template/front/error.html'
    return jinja2_template(tempalte_path, entity=error_entity)

def check_login_status(username):
    session = request.environ.get('beaker.session')
    session_value = session[HashHelper.hexdigest('login')]
    hashed_value = HashHelper.hexdigest(username)
    if(session_value != hashed_value):
        return redirect('/admin/login')
    pass

if __name__ == "__main__":
    # TODO: create controller classes
    session_opts = {
        'session.type': 'file',
        'session.cookie_expires': 300,
        'session.data_dir': './data',
        'session.auto': True
    }
    run(app=SessionMiddleware(app(), session_opts), host=config.get_web_host(), port=config.get_web_port(), debug=config.get_debug(), reloader=config.get_reloader())
