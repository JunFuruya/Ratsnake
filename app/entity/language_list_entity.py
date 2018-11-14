# -*- coding: utf-8 -*-

from app.entity.base_web_entity import BaseWebEntity

class LanguageListEntity(BaseWebEntity):
    __language_entity_list = []
    
    def set_language_entity_list(self, language_entity_list):
        self.__language_entity_list = language_entity_list
        return self

    def get_language_entity_list(self):
        return self.__language_entity_list  
    
