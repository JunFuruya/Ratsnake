#-*- UTF-8 -*-

from app.controller.base_controller import BaseController
from app.entity.base_web_entity import BaseWebEntity
from app.entity.login_entity import LoginEntity
from app.service.login_service import LoginService

from app.helper.helper import HashHelper

'''
Admin Login Controller Module
'''
class AdminLoginController(BaseController):
    __should_check_login_status = False
    
    def __init__(self, request):
        super().__init__(request, self.__should_check_login_status)
        self.set_page_info('Hideoutログイン', 'ログイン', 'ログインに必要な情報を入力してください。')
        self.__service = LoginService()
        pass

    def index(self):
        return self.view('./template/admin/login.html', entity=LoginEntity())

    def login(self):
        username = self.get_param('username', '')
        password = self.get_param('password', '')

        self.__user_id = self.__service.findByLoginInfo(username, password)
        if self.__user_id is not None:
            self.set_session(self.LOGIN_SESSION_USER_ID, self.__user_id)
            # TODO cookie 使う
            return self.redirect('/admin')
        else:
            return self.redirect('/admin/login')

    def logout(self):
        self.set_session(self.LOGIN_SESSION_USER_ID, '')
        return self.redirect('/admin/login')