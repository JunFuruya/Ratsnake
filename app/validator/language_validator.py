# -*- coding: UTF-8 -*-

from app.validator.base_validator import BaseValidator

class LanguageValidator(BaseValidator):
    def __init__(self):
        pass
        
    def get_error_messages(self, language_name):
        self.__language_name = language_name

        self.__validate()

        return super().get_error_messages()

    def __validate(self):
        if(self.has_empty_error(self.__language_name)):
            super().error_messages.append('名称が入力されていません。')
        if(self.has_too_large_number_error(self.__language_name, 100)):
            super().error_messages.append('名称は50文字以内で入力してください。')
        pass
    