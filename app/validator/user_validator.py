# -*- coding: UTF-8 -*-

from app.validator.base_validator import BaseValidator

class UserValidator(BaseValidator):
    def __init__(self):
        pass
        
    def get_error_messages(self, user_username, user_password):
        self.__user_username = user_username
        self.__user_password = user_password

        self.__validate()

        return super().get_error_messages()

    def __validate(self):
        error_messages = []
        if(self.has_empty_error(self.__user_username)):
            error_messages.append('ユーザ名称が入力されていません。')
        if(self.has_too_large_number_error(self.__user_username, 100)):
            error_messages.append('ユーザ名称は100文字以内で入力してください。')
        if(self.has_empty_error(self.__user_password)):
            error_messages.append('パスワードが入力されていません。')
            
        super().set_error_messages(error_messages)
        pass
    