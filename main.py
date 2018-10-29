# -*- coding: utf-8 -*-

from beaker.middleware import SessionMiddleware

from bottle import app, error, get, jinja2_template, post, request, run, static_file

from app.controller.admin_index_controller import AdminIndexController
from app.controller.admin_login_controller import AdminLoginController
from app.controller.error_controller import ErrorController
from app.controller.index_controller import IndexController
from app.controller.language_controller import LanguageController
from app.controller.link_category_controller import LinkCategoryController
from app.controller.link_controller import LinkController
from app.controller.word_controller import WordController

# TODO そのうち消す
from app.service.web_service import ConfigGetService
config = ConfigGetService().get_web_server_config()

###############################################################################
# 非ログインユーザ用画面
###############################################################################
@get('/')
def get_index():
    return IndexController().index(request)

###############################################################################
# 管理画面TOP
###############################################################################
@get('/admin')
def get_link_index():
    AdminLoginController.check_login_status()
    return AdminIndexController().index(request)

###############################################################################
# ログイン、ログアウト
###############################################################################
@get('/admin/login')
def get_admin_login():
    return AdminLoginController().index(request)

@post('/admin/login')
def post_admin_login_complete():
    return AdminLoginController().login(request)

@get('/admin/logout')
def get_admin_login_complete():
    return AdminLoginController().logout(request)

###############################################################################
# リンクカテゴリマスタ
###############################################################################
@get('/admin/link-categories')
def get_link_category_list():
    AdminLoginController.check_login_status()
    return LinkCategoryController().index(request)

@get('/admin/link-categories/create')
def get_link_category_create():
    AdminLoginController.check_login_status()
    return LinkCategoryController().create(request)

@get('/admin/link-categories/<link_category_id>')
def post_link_category_detail(link_category_id):
    AdminLoginController.check_login_status()
    return LinkCategoryController().detail(request, link_category_id)

@post('/admin/link-categories/<link_category_id>')
def post_link_category_edit(link_category_id):
    AdminLoginController.check_login_status()
    return LinkCategoryController().edit(request, link_category_id)

@post('/admin/link-categories/confirm')
def post_link_category_confirm():
    AdminLoginController.check_login_status()
    return LinkCategoryController().confirm(request)

@post('/admin/link-categories/insert')
def post_link_category_insert():
    AdminLoginController.check_login_status()
    return LinkCategoryController().insert(request)

@post('/admin/link-categories/<link_category_id>/update')
def post_link_category_update(link_category_id):
    AdminLoginController.check_login_status()
    return LinkCategoryController().update(request, link_category_id)

@post('/admin/link-categories/<link_category_id>/delete')
def post_link_category_delete(link_category_id):
    AdminLoginController.check_login_status()
    return LinkCategoryController().delete(request, link_category_id)

###############################################################################
# リンクマスタ
###############################################################################
@get('/admin/links')
def get_link_list():
    AdminLoginController.check_login_status()
    return LinkController.index(request)

@get('/admin/links/create')
def get_link_create():
    AdminLoginController.check_login_status()
    return LinkController.create(request)

@get('/admin/links/<link_id>')
def post_link_update(link_id):
    AdminLoginController.check_login_status()
    return LinkController.update(request, link_id)

@post('/admin/links/<link_id>')
def post_link_update(link_id):
    AdminLoginController.check_login_status()
    return LinkController.index(request, link_id)

@post('/admin/links/confirm')
def post_link_confirm():
    AdminLoginController.check_login_status()
    return LinkController.confirm(request)

@post('/admin/links/insert')
def post_link_complete():
    AdminLoginController.check_login_status()
    return LinkController.insert(request)

@post('/admin/links/update')
def post_link_complete():
    AdminLoginController.check_login_status()
    return LinkController.update(request)

@post('/admin/links/delete')
def post_link_complete():
    AdminLoginController.check_login_status()
    return LinkController.delete(request)

###############################################################################
# 言語マスタ
###############################################################################
@get('/admin/languages')
def get_language_list():
    AdminLoginController.check_login_status()
    return LanguageController().index(request)

@get('/admin/languages/create')
def get_language_create():
    AdminLoginController.check_login_status()
    return LanguageController().create(request)

@get('/admin/languages/<language_id>')
def post_language_detail(language_id):
    AdminLoginController.check_login_status()
    return LanguageController().detail(request, language_id)

@post('/admin/languages/<language_id>')
def post_language_edit(language_id):
    AdminLoginController.check_login_status()
    return LanguageController().edit(request, language_id)

@post('/admin/languages/confirm')
def post_language_confirm():
    AdminLoginController.check_login_status()
    return LanguageController().confirm(request)

@post('/admin/languages/insert')
def post_language_insert():
    AdminLoginController.check_login_status()
    return LanguageController().insert(request)

@post('/admin/languages/update')
def post_language_update():
    AdminLoginController.check_login_status()
    return LanguageController().update(request)

@post('/admin/languages/delete')
def post_language_delete():
    AdminLoginController.check_login_status()
    return LanguageController().delete(request)

###############################################################################
# 単語帳
###############################################################################
@get('/admin/languages/words')
def get_word_list():
    AdminLoginController.check_login_status()
    return WordController().index(request)

@get('/admin/languages/<language_id>/words')
def post_word_list(language_id):
    AdminLoginController.check_login_status()
    return WordController().index(request, language_id)

@get('/admin/languages/<language_id>/words/create')
def get_word_create(language_id):
    AdminLoginController.check_login_status()
    return WordController().create(request, language_id)

@get('/admin/languages/<language_id>/words/<word_id>')
def post_word_detail(language_id, word_id):
    AdminLoginController.check_login_status()
    return WordController().detail(request, language_id, word_id)

@post('/admin/languages/<language_id>/words/confirm')
def post_word_confirm(language_id):
    AdminLoginController.check_login_status()
    return WordController().confirm(request, language_id)

@post('/admin/languages/<language_id>/words/<word_id>/confirm')
def post_word_confirm(language_id, word_id):
    AdminLoginController.check_login_status()
    return WordController().confirm(request, language_id)

@post('/admin/languages/<language_id>/words/insert')
def post_word_insert(language_id):
    AdminLoginController.check_login_status()
    return WordController().insert(request, language_id)

@post('/admin/languages/<language_id>/words/<word_id>')
def post_word_edit(language_id, word_id):
    AdminLoginController.check_login_status()
    return WordController().edit(request, language_id, word_id)

@post('/admin/languages/<language_id>/words/<word_id>/update')
def post_word_update(language_id, word_id):
    AdminLoginController.check_login_status()
    return WordController().update(request, language_id, word_id)

@post('/admin/languages/<language_id>/words/<word_id>/delete')
def post_word_delete(language_id, word_id):
    AdminLoginController.check_login_status()
    return WordController().delete(request, language_id, word_id)

###############################################################################
# 静的ファイル
###############################################################################
@get('/public/<path:path>')
def get_static_file(path):
    return static_file(path, root='./public/')

###############################################################################
# エラー画面
###############################################################################
@error(404)
def error404(error):
    return ErrorController.error(404)

error(500)
def error500(error):
    return ErrorController.error(500)

if __name__ == "__main__":
    # TODO: create controller classes
    session_opts = {
        'session.type': 'file',
        'session.cookie_expires': 300,
        'session.data_dir': './data',
        'session.auto': True
    }

    run(app=SessionMiddleware(app(), session_opts), host=config.get_web_host(), port=config.get_web_port(), debug=config.get_debug(), reloader=config.get_reloader())
