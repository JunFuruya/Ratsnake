# -*- coding: UTF-8 -*-

import g

from app.validator.base_validator import BaseValidator
from app.service.login_service import LoginService

class LoginValidator(BaseValidator):
    def __init__(self):
        super().__init__()
        pass
        
    def get_error_messages(self, username, password):
        self.__username = username
        self.__password = password        
        self.__user_id = LoginService().findByLoginInfo(self.__username, self.__password)
        self.__validate()

        return super().get_error_messages()
    
    def __validate(self):
        error_messages = []
        if(self.has_empty_error(self.__username)):
            error_messages.append('ログインIDが入力されていません。')
        if(self.has_empty_error(self.__password)):
            error_messages.append('パスワードが入力されていません。')

        if self.__user_id is None:
            error_messages.append('ログインIDかパスワードが間違っています。')
            
        super().set_error_messages(error_messages)
        pass
    
    def get_user_id(self):
        return self.__user_id