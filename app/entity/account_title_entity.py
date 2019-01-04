# -*- coding: UTF-8 -*-

from app.entity.base_web_entity import BaseWebEntity
from app.value.values import AccountTitleClassificationTypeValue

class AccountTitleEntity(BaseWebEntity):
    
    def set_error_message(self, error_message):
        self.__error_message = error_message
        return self

    def get_error_message(self):
        return self.__error_message  
    
    def set_account_title_id(self, account_title_id):
        self.__account_title_id = account_title_id
        return self
    
    def get_account_title_id(self):
        return self.__account_title_id
    
    def set_account_title_name(self, account_title_name):
        self.__account_title_name = account_title_name
        return self
    
    def get_account_title_name(self):
        return self.__account_title_name
    
    def set_account_title_classification_type(self, account_title_classification_type):
        self.__account_title_classification_type = AccountTitleClassificationTypeValue(account_title_classification_type)
        return self

    def get_account_title_classification_type(self):
        return self.__account_title_classification_type
    # TODO to array
