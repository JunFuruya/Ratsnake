# -*- coding: utf-8 -*-

from beaker.middleware import SessionMiddleware
# TODO jinja2_template はBaseController に移したので消す
from bottle import app, error, get, jinja2_template, post, redirect, request, response, run, static_file, TEMPLATE_PATH

from app.helper.helper import HashHelper
from app.controller.language_controller import LanguageController

# TODO そのうち消す
from app.service.web_service import ConfigGetService, LoginService, SlackBotStartService

from app.infrastructure.config_ini_file import DbServerConfigIniFile

config = ConfigGetService().get_web_server_config()

@get('/')
def get_index():
    # TODO: username取得
    #check_login_status('admin')
        
    #entity = service.get_index_data
    tempalte_path = './template/index.html'
    #return jinja2_template(tempalte_path, entity=entity)
    return jinja2_template(tempalte_path)
    
@get('/admin')
def get_link_index():
    # TODO: username取得
    check_login_status('admin')
    
    from app.entity.index_entity import IndexEntity
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
    from app.entity.login_entity import LoginEntity
    login_entity = LoginEntity()
    login_entity.set_title('Hideout Main Page')
    login_entity.set_description('Hideout Login Page')
    login_entity.set_notification('Please enter your id and password.')
    tempalte_path = './template/admin/login.html'
    return jinja2_template(tempalte_path, entity=login_entity)

@post('/admin/login')
def post_admin_login_complete():
    username = request.forms.get('username')
    password = request.forms.get('password')

    service = LoginService()
    if(service.is_authenticated(username, password)):
        session = request.environ.get('beaker.session')
        session[HashHelper.hexdigest('login')] = HashHelper.hexdigest(username)
        session.save()

        # TODO: move max_age to config file
        max_age = 60 * 60 * 24 * 30 # 1Month
        response.set_cookie(HashHelper.hexdigest('login'), session[HashHelper.hexdigest('login')], max_age=max_age)
        # TODO cookie 使えてる?
        return redirect('/admin')
        
    else:
        return redirect('/admin/login')

@get('/admin/logout')
def get_admin_login_complete():
    session = request.environ.get('beaker.session')
    session[HashHelper.hexdigest('login')] = ''
    session.save()
    return redirect('/admin/login')

@get('/admin/links')
def get_link_list():
    check_login_status('admin')
    link_list = [
        [1, 'AAA', 'http://aaa.co.jp'],
        [2, 'BBB', 'http://bbb.co.jp'],
        [3, 'CCC', 'http://ccc.co.jp']
    ]
    # TODO テンプレート用意する
    tempalte_path = './template/admin/links/list.html'
    return jinja2_template(tempalte_path, link_list=link_list)

@get('/admin/links/create')
def get_link_create():
    return jinja2_template('./template/admin/links/create.html', entity=LinkController().create(request))

@get('/admin/links/<link_id>')
def post_link_update(link_id):
    # TODO テンプレート用意する
    html = '<html><body>update</body></html>'
    return jinja2_template(html)

@post('/admin/links/<link_id>')
def post_link_update(link_id):
    # TODO テンプレート用意する
    html = '<html><body>update</body></html>'
    return jinja2_template(html)

@post('/admin/links/confirm')
def post_link_confirm():
    # TODO テンプレート用意する
    html = '<html><body>confirm</body></html>'
    return jinja2_template(html)

@post('/admin/links/complete')
def post_link_complete():
    # TODO テンプレート用意する
    html = '<html><body>complete</body></html>'
    return jinja2_template(html)

@get('/admin/languages')
def get_language_list():
    check_login_status('admin')
    return LanguageController().index(request)

@get('/admin/languages/create')
def get_language_create():
    check_login_status('admin')
    return LanguageController().create(request)

@get('/admin/languages/<language_id>')
def post_language_detail(language_id):
    check_login_status('admin')
    return LanguageController().detail(request, language_id)

@post('/admin/languages/<language_id>')
def post_language_edit(language_id):
    check_login_status('admin')
    return LanguageController().edit(request, language_id)

@post('/admin/languages/confirm')
def post_language_confirm():
    check_login_status('admin')
    return LanguageController().confirm(request)

@post('/admin/languages/insert')
def post_language_insert():
    check_login_status('admin')
    return LanguageController().insert(request)

@post('/admin/languages/update')
def post_language_update():
    check_login_status('admin')
    return LanguageController().update(request)

@post('/admin/languages/delete')
def post_language_delete():
    check_login_status('admin')
    return LanguageController().delete(request)

@get('/admin/words')
def get_word_list():
    check_login_status('admin')
    return jinja2_template('./template/admin/words/list.html', entity=LinkController().index(request))

@get('/admin/words/create')
def get_word_create():
    html = '<html><body>create</body></html>'
    tempalte_path = './template/admin/words/create.html'
    return jinja2_template(tempalte_path)

@get('/admin/words/<word_id>')
def post_word_update(word_id):
    # TODO テンプレート用意する
    html = '<html><body>update</body></html>'
    return jinja2_template(tempalte_path)

@post('/admin/words/<word_id>')
def post_word_update(word_id):
    # TODO テンプレート用意する
    html = '<html><body>update</body></html>'
    return jinja2_template(html)

@post('/admin/words/confirm')
def post_word_confirm():
    # TODO テンプレート用意する
    html = '<html><body>confirm</body></html>'
    return jinja2_template(html)

@post('/admin/words/complete')
def post_word_complete():
    # TODO テンプレート用意する
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
    
error(500)
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
    session_value = session.get(HashHelper.hexdigest('login'), False)
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
