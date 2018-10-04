# -*- coding: utf-8 -*-

from app.entity.base_web_entity import BaseWebEntity

class WordListEntity(BaseWebEntity):
    __word_entity_list = []
    __language_id = ''
    __language_entity_list = []
    
    def set_word_entity_list(self, word_entity_list):
        self.__word_entity_list = word_entity_list
        return self

    def get_word_entity_list(self):
        return self.__word_entity_list  
    
    def set_language_id(self, language_id):
        self.__language_id = language_id
        return self

    def get_language_id(self):
        return self.__language_id
    
    def set_language_entity_list(self, language_entity_list):
        self.__language_entity_list = language_entity_list
        return self

    def get_language_entity_list(self):
        return self.__language_entity_list
