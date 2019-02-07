# -*- coding: UTF-8 -*-

from bottle import app, error, get, post, request, run, static_file

from app.controller.admin.account_title_controller import AccountTitleController
from app.controller.admin.index_controller import IndexController as AdminIndexController
from app.controller.admin.login_controller import LoginController
from app.controller.admin.client_controller import ClientController
from app.controller.admin.cover_letter_controller import CoverLetterController
from app.controller.admin.error_controller import ErrorController
from app.controller.admin.language_controller import LanguageController
from app.controller.admin.link_category_controller import LinkCategoryController
from app.controller.admin.link_controller import LinkController
from app.controller.admin.mail_controller import MailController
from app.controller.admin.journal_entry_controller import JournalEntryController
from app.controller.admin.user_controller import UserController
from app.controller.admin.word_controller import WordController
from app.controller.client.index_controller import IndexController

# TODO そのうち消す
from app.service.web_service import ConfigGetService
config = ConfigGetService().get_web_server_config()

###############################################################################
# 非ログインユーザ用画面
###############################################################################
@get('/')
def index():
    return IndexController(request).index()

# TODO 自己紹介インフォグラフィック
# TODO ポートフォリオ

###############################################################################
# 管理画面TOP
###############################################################################
@get('/admin')
def admin_index():
    return AdminIndexController(request).index()

###############################################################################
# ログイン、ログアウト
###############################################################################
@get('/admin/login')
def admin_login():
    return LoginController(request).index()

@post('/admin/login')
def admin_login_complete():
    return LoginController(request).login()

@get('/admin/logout')
def admin_logout():
    return LoginController(request).logout()

###############################################################################
# リンクカテゴリマスタ
###############################################################################
@get('/admin/link-categories')
def link_category_list():
    return LinkCategoryController(request).index()

@get('/admin/link-categories/create')
def link_category_create():
    return LinkCategoryController(request).create()

@get('/admin/link-categories/<link_category_id>')
def link_category_detail(link_category_id):
    return LinkCategoryController(request).detail(link_category_id)

@post('/admin/link-categories/<link_category_id>')
def link_category_edit(link_category_id):
    return LinkCategoryController(request).edit(link_category_id)

@post('/admin/link-categories/confirm')
def link_category_confirm():
    return LinkCategoryController(request).confirm()

@post('/admin/link-categories/insert')
def link_category_insert():
    return LinkCategoryController(request).insert()

@post('/admin/link-categories/<link_category_id>/update')
def link_category_update(link_category_id):
    return LinkCategoryController(request).update(link_category_id)

@post('/admin/link-categories/<link_category_id>/delete')
def link_category_delete(link_category_id):
    return LinkCategoryController(request).delete(link_category_id)

###############################################################################
# リンクマスタ
###############################################################################
@get('/admin/links')
def link_list():
    return LinkController(request).index()

@get('/admin/links/create')
def link_create():
    return LinkController(request).create()

@get('/admin/links/<link_id>')
def link_detail(link_id):
    return LinkController(request).detail(link_id)

@post('/admin/links/<link_id>')
def link_edit(link_id):
    return LinkController(request).edit(link_id)

@post('/admin/links/confirm')
def link_confirm():
    return LinkController(request).confirm()

@post('/admin/links/insert')
def link_insert():
    return LinkController(request).insert()

@post('/admin/links/update')
def link_update():
    return LinkController(request).update()

@post('/admin/links/delete')
def link_delete():
    return LinkController(request).delete()

###############################################################################
# 言語マスタ
###############################################################################
@get('/admin/languages')
def language_list():
    return LanguageController(request).index()

@get('/admin/languages/create')
def language_create():
    return LanguageController(request).create()

@get('/admin/languages/<language_id>')
def language_detail(language_id):
    return LanguageController(request).detail(language_id)

@post('/admin/languages/<language_id>')
def language_edit(language_id):
    return LanguageController(request).edit(language_id)

@post('/admin/languages/confirm')
def language_confirm():
    return LanguageController(request).confirm()

@post('/admin/languages/insert')
def language_insert():
    return LanguageController(request).insert()

@post('/admin/languages/update')
def language_update():
    return LanguageController(request).update()

@post('/admin/languages/delete')
def language_delete():
    return LanguageController(request).delete()

###############################################################################
# 単語帳
###############################################################################
@get('/admin/languages/words')
def word_list():
    return WordController(request).index()

@get('/admin/languages/<language_id>/words')
def word_list(language_id):
    return WordController(request).index(language_id)

@get('/admin/languages/<language_id>/words/create')
def word_create(language_id):
    return WordController(request).create(language_id)

@get('/admin/languages/<language_id>/words/<word_id>')
def word_detail(language_id, word_id):
    return WordController(request).detail(language_id, word_id)

@post('/admin/languages/<language_id>/words/confirm')
def word_confirm(language_id):
    return WordController(request).confirm(language_id)

@post('/admin/languages/<language_id>/words/<word_id>/confirm')
def word_confirm(language_id, word_id):
    return WordController(request).confirm(language_id)

@post('/admin/languages/<language_id>/words/insert')
def word_insert(language_id):
    return WordController(request).insert(language_id)

@post('/admin/languages/<language_id>/words/<word_id>')
def word_edit(language_id, word_id):
    return WordController(request).edit(language_id, word_id)

@post('/admin/languages/<language_id>/words/<word_id>/update')
def word_update(language_id, word_id):
    return WordController(request).update(language_id, word_id)

@post('/admin/languages/<language_id>/words/<word_id>/delete')
def word_delete(language_id, word_id):
    return WordController(request).delete(language_id, word_id)

@post('/admin/languages/words/csv')
def word_import_csv():
    return WordController(request).import_csv()

###############################################################################
# ユーザマスタ
###############################################################################
@get('/admin/users')
def user_list():
    return UserController(request).index()

@get('/admin/users/create')
def user_create():
    return UserController(request).create()

@get('/admin/users/<user_id>')
def user_detail(user_id):
    return UserController(request).detail(user_id)

@post('/admin/users/<user_id>')
def user_edit(user_id):
    return UserController(request).edit(user_id)

@post('/admin/users/confirm')
def user_confirm():
    return UserController(request).confirm()

@post('/admin/users/insert')
def user_insert():
    return UserController(request).insert()

@post('/admin/users/<user_id>/update')
def user_update(user_id):
    return UserController(request).update(user_id)

@post('/admin/users/<user_id>/delete')
def user_delete(user_id):
    return UserController(request).delete(user_id)

###############################################################################
# 勘定科目マスタ
###############################################################################
@get('/admin/account-titles')
def account_title_list():
    return AccountTitleController(request).index()

@get('/admin/account-titles/create')
def account_title_create():
    return AccountTitleController(request).create()

@get('/admin/account-titles/<account_title_id>')
def account_title_detail(account_title_id):
    return AccountTitleController(request).detail(account_title_id)

@post('/admin/account-titles/<account_title_id>')
def account_title_edit(account_title_id):
    return AccountTitleController(request).edit(account_title_id)

@post('/admin/account-titles/confirm')
def account_title_confirm():
    return AccountTitleController(request).confirm()

@post('/admin/account-titles/insert')
def account_title_insert():
    return AccountTitleController(request).insert()

@post('/admin/account-titles/<account_title_id>/update')
def account_title_update(account_title_id):
    return AccountTitleController(request).update(account_title_id)

@post('/admin/account-titles/<account_title_id>/delete')
def account_title_delete(account_title_id):
    return AccountTitleController(request).delete(account_title_id)

###############################################################################
# 取引先マスタ
###############################################################################
@get('/admin/clients')
def client_list():
    return ClientController(request).index()

@get('/admin/clients/create')
def client_create():
    return ClientController(request).create()

@get('/admin/clients/<clients_id>')
def client_detail(clients_id):
    return ClientController(request).detail(clients_id)

@post('/admin/clients/<clients_id>')
def client_edit(clients_id):
    return ClientController(request).edit(clients_id)

@post('/admin/clients/confirm')
def client_confirm():
    return ClientController(request).confirm()

@post('/admin/clients/insert')
def client_insert():
    return ClientController(request).insert()

@post('/admin/clients/<clients_id>/update')
def client_update(clients_id):
    return ClientController(request).update(clients_id)

@post('/admin/clients/<clients_id>/delete')
def client_delete(clients_id):
    return ClientController(request).delete(clients_id)

###############################################################################
# 仕分元帳画面
###############################################################################
@get('/admin/journal-entries')
def journal_entry_list():
    return JournalEntryController(request).index()

@get('/admin/journal-entries/create')
def journal_entry_create():
    return JournalEntryController(request).create()

@get('/admin/journal-entries/<journal_entry_id>')
def journal_entry_detail(journal_entry_id):
    return JournalEntryController(request).detail(journal_entry_id)

@post('/admin/journal-entries/<journal_entry_id>')
def journal_entry_edit(journal_entry_id):
    return JournalEntryController(request).edit(journal_entry_id)

@post('/admin/journal-entries/confirm')
def journal_entry_confirm():
    return JournalEntryController(request).confirm()

@post('/admin/journal-entries/insert')
def journal_entry_insert():
    return JournalEntryController(request).insert()

@post('/admin/journal-entries/<journal_entry_id>/update')
def journal_entry_update(journal_entry_id):
    return JournalEntryController(request).update(journal_entry_id)

@post('/admin/journal-entries/<journal_entry_id>/delete')
def journal_entry_delete(journal_entry_id):
    return JournalEntryController(request).delete(journal_entry_id)

###############################################################################
# 受注管理表画面
###############################################################################
# TODO 受注一覧画面
# TODO 送り状PDF出力
# @post('/admin/cover-letter/<cover_letter_id>/pdf')
@get('/admin/cover-letter/<cover_letter_id>/pdf')
def cover_letter_pdf(cover_letter_id):
    return CoverLetterController(request).get_pdf(cover_letter_id)

# TODO 送り状登録画面
# TODO 送り状詳細画面
# TODO 見積書登録画面
# TODO 見積書PDF出力
# TODO 見積書詳細画面
# TODO 注文書登録画面
# TODO 注文書詳細画面
# TODO 注文請書登録画面
# TODO 注文請書詳細画面
# TODO 請求書登録画面
# TODO 請求書詳細画面

###############################################################################
# TODO B/S画面
###############################################################################

###############################################################################
# TODO P/L画面
###############################################################################

###############################################################################
# TODO C/F画面
###############################################################################

###############################################################################
# TODO 税金シミュレーション画面
###############################################################################

###############################################################################
# メール送信画面
###############################################################################
@get('/admin/mails')
def mail_list():
    return MailController(request).index()

# TODO 送信画面

###############################################################################
# 静的ファイル
###############################################################################
@get('/public/<path:path>')
def static_file(path):
    return static_file(path, root='./public/')

###############################################################################
# エラー画面
###############################################################################
@error(404)
def error404(error):
    return ErrorController(request).error(404)

@error(500)
def error500(error):
    return ErrorController(request).error(500)

if __name__ == "__main__":
    from beaker.middleware import SessionMiddleware
    session_opts = {
        'session.type': 'file',
        'session.cookie_expires': 300,
        'session.data_dir': './data',
        'session.auto': True
    }
    run(app=SessionMiddleware(app(), session_opts), host=config.get_web_host(), port=config.get_web_port(),
        debug=config.get_debug(), reloader=config.get_reloader())