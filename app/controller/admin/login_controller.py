# -*- coding: UTF-8 -*-

import g

from app.controller.base_controller import BaseController
from app.entity.login_entity import LoginEntity
from app.service.login_service import LoginService
from app.validator.login_validator import LoginValidator

'''
Login Controller Module
'''
class LoginController(BaseController):
    __should_check_login_status = False
    COOKIE_VALID_PERIOD = 86400
    
    def __init__(self, request):
        super().__init__(request, self.__should_check_login_status)
        self.set_page_info('Hideoutログイン', 'ログイン', 'ログインに必要な情報を入力してください。')
        self.__service = LoginService()
        self.__validator = LoginValidator()
        pass
    
    def index(self):
        entity = LoginEntity()
        entity.set_username('')
        entity.set_error_messages('')
        return self.view('./template/admin/login.html', entity)

    def login(self):
        username = self.get_param('username', '')
        password = self.get_param('password', '')
        
        error_messages = self.__validator.get_error_messages(username, password)
        if len(error_messages) == 0:
            self.__user_id = self.__service.findByLoginInfo(username, password)
            self.set_session(self.LOGIN_SESSION_USER_ID, self.__validator.get_user_id())
            self.set_cookie(HashHelper.hexdigest(self.LOGIN_SESSION_USER_ID), self.__user_id , self.COOKIE_VALID_PERIOD)
            return self.redirect('/admin')
        else:
            entity = LoginEntity()
            entity.set_username(username)
            entity.set_error_messages(error_messages)
            return self.view('./template/admin/login.html', entity)
        
    def logout(self):
        self.set_session(self.LOGIN_SESSION_USER_ID, '')
        self.set_cookie(self.LOGIN_SESSION_USER_ID, 0)

        return self.redirect('/admin/login')