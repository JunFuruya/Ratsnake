# -*- coding: UTF-8 -*-

from app.validator.base_validator import BaseValidator

class ClientValidator(BaseValidator):
    def __init__(self):
        pass
        
    def get_error_messages(self, client):
        self.__client_name = client_name

        self.__validate()

        return super().get_error_messages()

    def __validate(self):
        error_messages = []
        if(self.has_empty_error(self.__client_name)):
            error_messages.append('名称が入力されていません。')
        if(self.has_too_large_number_error(self.__client_name, 100)):
            error_messages.append('名称は50文字以内で入力してください。')
            
        super().set_error_messages(error_messages)
        pass
    