# -*- coding: UTF-8 -*-

from bottle import app, error, get, post, request, run, static_file

from app.controller.account_title_controller import AccountTitleController
from app.controller.admin_index_controller import AdminIndexController
from app.controller.admin_login_controller import AdminLoginController
from app.controller.cover_letter_controller import CoverLetterController
from app.controller.error_controller import ErrorController
from app.controller.index_controller import IndexController
from app.controller.language_controller import LanguageController
from app.controller.link_category_controller import LinkCategoryController
from app.controller.link_controller import LinkController
from app.controller.journal_entry_controller import JournalEntryController
from app.controller.user_controller import UserController
from app.controller.word_controller import WordController

# TODO そのうち消す
from app.service.web_service import ConfigGetService
config = ConfigGetService().get_web_server_config()

# TODO メソッド名を全て見直し

###############################################################################
# 非ログインユーザ用画面
###############################################################################
@get('/')
def get_index():
    return IndexController(request).index()

###############################################################################
# 管理画面TOP
###############################################################################
@get('/admin')
def get_link_index():
    return AdminIndexController(request).index()

# TODO 自己紹介インフォグラフィック
# TODO ポートフォリオ

###############################################################################
# ログイン、ログアウト
###############################################################################
@get('/admin/login')
def get_admin_login():
    return AdminLoginController(request).index()

@post('/admin/login')
def post_admin_login_complete():
    return AdminLoginController(request).login()

@get('/admin/logout')
def get_admin_login_complete():
    return AdminLoginController(request).logout()

###############################################################################
# リンクカテゴリマスタ
###############################################################################
@get('/admin/link-categories')
def get_link_category_list():
    return LinkCategoryController(request).index()

@get('/admin/link-categories/create')
def get_link_category_create():
    return LinkCategoryController(request).create()

@get('/admin/link-categories/<link_category_id>')
def post_link_category_detail(link_category_id):
    return LinkCategoryController(request).detail(link_category_id)

@post('/admin/link-categories/<link_category_id>')
def post_link_category_edit(link_category_id):
    return LinkCategoryController(request).edit(link_category_id)

@post('/admin/link-categories/confirm')
def post_link_category_confirm():
    return LinkCategoryController(request).confirm()

@post('/admin/link-categories/insert')
def post_link_category_insert():
    return LinkCategoryController(request).insert()

@post('/admin/link-categories/<link_category_id>/update')
def post_link_category_update(link_category_id):
    return LinkCategoryController(request).update(link_category_id)

@post('/admin/link-categories/<link_category_id>/delete')
def post_link_category_delete(link_category_id):
    return LinkCategoryController(request).delete(link_category_id)

###############################################################################
# リンクマスタ
###############################################################################
@get('/admin/links')
def get_link_list():
    return LinkController(request).index()

@get('/admin/links/create')
def get_link_create():
    return LinkController(request).create()

@get('/admin/links/<link_id>')
def post_link_detail(link_id):
    return LinkController(request).detail(link_id)

@post('/admin/links/<link_id>')
def post_link_edit(link_id):
    return LinkController(request).edit(link_id)

@post('/admin/links/confirm')
def post_link_confirm():
    return LinkController(request).confirm()

@post('/admin/links/insert')
def post_link_complete():
    return LinkController(request).insert()

@post('/admin/links/update')
def post_link_complete():
    return LinkController(request).update()

@post('/admin/links/delete')
def post_link_complete():
    return LinkController(request).delete()

###############################################################################
# 言語マスタ
###############################################################################
@get('/admin/languages')
def get_language_list():
    return LanguageController(request).index()

@get('/admin/languages/create')
def get_language_create():
    return LanguageController(request).create()

@get('/admin/languages/<language_id>')
def post_language_detail(language_id):
    return LanguageController(request).detail(language_id)

@post('/admin/languages/<language_id>')
def post_language_edit(language_id):
    return LanguageController(request).edit(language_id)

@post('/admin/languages/confirm')
def post_language_confirm():
    return LanguageController(request).confirm()

@post('/admin/languages/insert')
def post_language_insert():
    return LanguageController(request).insert()

@post('/admin/languages/update')
def post_language_update():
    return LanguageController(request).update()

@post('/admin/languages/delete')
def post_language_delete():
    return LanguageController(request).delete()

###############################################################################
# 単語帳
###############################################################################
@get('/admin/languages/words')
def get_word_list():
    return WordController(request).index()

@get('/admin/languages/<language_id>/words')
def post_word_list(language_id):
    return WordController(request).index(language_id)

@get('/admin/languages/<language_id>/words/create')
def get_word_create(language_id):
    return WordController(request).create(language_id)

@get('/admin/languages/<language_id>/words/<word_id>')
def post_word_detail(language_id, word_id):
    return WordController(request).detail(language_id, word_id)

@post('/admin/languages/<language_id>/words/confirm')
def post_word_confirm(language_id):
    return WordController(request).confirm(language_id)

@post('/admin/languages/<language_id>/words/<word_id>/confirm')
def post_word_confirm(language_id, word_id):
    return WordController(request).confirm(language_id)

@post('/admin/languages/<language_id>/words/insert')
def post_word_insert(language_id):
    return WordController(request).insert(language_id)

@post('/admin/languages/<language_id>/words/<word_id>')
def post_word_edit(language_id, word_id):
    return WordController(request).edit(language_id, word_id)

@post('/admin/languages/<language_id>/words/<word_id>/update')
def post_word_update(language_id, word_id):
    return WordController(request).update(language_id, word_id)

@post('/admin/languages/<language_id>/words/<word_id>/delete')
def post_word_delete(language_id, word_id):
    return WordController(request).delete(language_id, word_id)

@post('/admin/languages/words/csv')
def post_word_import_csv():
    return WordController(request).import_csv()

###############################################################################
# ユーザマスタ
###############################################################################
@get('/admin/users')
def get_user_list():
    return UserController(request).index()

@get('/admin/users/create')
def get_user_create():
    return UserController(request).create()

@get('/admin/users/<user_id>')
def post_user_detail(user_id):
    return UserController(request).detail(user_id)

@post('/admin/users/<user_id>')
def post_user_edit(user_id):
    return UserController(request).edit(user_id)

@post('/admin/users/confirm')
def post_user_confirm():
    return UserController(request).confirm()

@post('/admin/users/insert')
def post_user_insert():
    return UserController(request).insert()

@post('/admin/users/<user_id>/update')
def post_user_update(user_id):
    return UserController(request).update(user_id)

@post('/admin/users/<user_id>/delete')
def post_user_delete(user_id):
    return UserController(request).delete(user_id)

###############################################################################
# 勘定科目マスタ
###############################################################################
@get('/admin/account-titles')
def get_account_title_list():
    return AccountTitleController(request).index()

@get('/admin/account-titles/create')
def get_account_title_create():
    return AccountTitleController(request).create()

@get('/admin/account-titles/<account_title_id>')
def get_account_title_detail(account_title_id):
    return AccountTitleController(request).detail(account_title_id)

@post('/admin/account-titles/<account_title_id>')
def post_account_title_edit(account_title_id):
    return AccountTitleController(request).edit(account_title_id)

@post('/admin/account-titles/confirm')
def post_account_title_confirm():
    return AccountTitleController(request).confirm()

@post('/admin/account-titles/insert')
def post_account_title_insert():
    return AccountTitleController(request).insert()

@post('/admin/account-titles/<account_title_id>/update')
def post_account_title_update(account_title_id):
    return AccountTitleController(request).update(account_title_id)

@post('/admin/account-titles/<account_title_id>/delete')
def post_account_title_delete(account_title_id):
    return AccountTitleController(request).delete(account_title_id)

###############################################################################
# TODO 取引先マスタ
###############################################################################


###############################################################################
# 仕分元帳画面
###############################################################################
@get('/admin/journal-entries')
def get_journal_entry_list():
    return JournalEntryController(request).index()

@get('/admin/journal-entries/create')
def get_journal_entry_create():
    return JournalEntryController(request).create()

@get('/admin/journal-entries/<journal_entry_id>')
def get_journal_entry_detail(journal_entry_id):
    return JournalEntryController(request).detail(journal_entry_id)

@post('/admin/journal-entries/<journal_entry_id>')
def post_journal_entry_edit(journal_entry_id):
    return JournalEntryController(request).edit(journal_entry_id)

@post('/admin/journal-entries/confirm')
def post_journal_entry_confirm():
    return JournalEntryController(request).confirm()

@post('/admin/journal-entries/insert')
def post_journal_entry_insert():
    return JournalEntryController(request).insert()

@post('/admin/journal-entries/<journal_entry_id>/update')
def post_journal_entry_update(journal_entry_id):
    return JournalEntryController(request).update(journal_entry_id)

@post('/admin/journal-entries/<journal_entry_id>/delete')
def post_journal_entry_delete(journal_entry_id):
    return JournalEntryController(request).delete(journal_entry_id)

###############################################################################
# 受注管理表画面
###############################################################################
# TODO 受注一覧画面
# TODO 送り状PDF出力
# @post('/admin/cover-letter/<cover_letter_id>/pdf')
@get('/admin/cover-letter/<cover_letter_id>/pdf')
def get_cover_letter_pdf(cover_letter_id):
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
# TODO メール送信画面
###############################################################################

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