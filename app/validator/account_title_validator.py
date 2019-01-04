# -*- coding: UTF-8 -*-

from app.validator.base_validator import BaseValidator

class AccountTitleValidator(BaseValidator):
    def __init__(self):
        pass
        
    def get_error_messages(self, account_title_name, account_title_classification_type):
        self.__account_title_name = account_title_name
        self.__account_title_classification_type = account_title_classification_type

        self.__validate()

        return super().get_error_messages()

    def __validate(self):
        #if(self.has_empty_error(self.__account_title_name)):
            #super().error_messages.append('勘定科目が入力されていません。')
        if(self.has_too_large_number_error(self.__account_title_name, 20)):
            super().error_messages.append('勘定科目は20文字以内で入力してください。')
        #if(self.has_empty_error(self.__account_title_classification_type)):
            #super().error_messages.append('勘定科目分類区分が入力されていません。')
        if(self.has_too_large_number_error(self.__account_title_classification_type, 1)):
            super().error_messages.append('勘定科目分類区分は1文字で入力してください。')
        pass
    