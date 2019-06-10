# -*- coding: UTF-8 -*-

from app.entity.base_web_entity import BaseWebEntity

class AccountTitleListEntity(BaseWebEntity):
    __account_title_entity_list = []
    
    def set_account_title_entity_list(self, account_title_entity_list):
        self.__account_title_entity_list = account_title_entity_list
        return self

    def get_account_title_entity_list(self):
        return self.__account_title_entity_list  
    
