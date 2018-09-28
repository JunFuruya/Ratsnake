# -*- coding: utf-8 -*-

from app.entity.base_web_entity import BaseWebEntity

class WordListEntity(BaseWebEntity):
    __word_entity_list = []
    
    def set_word_entity_list(self, word_entity_list):
        self.__word_entity_list = word_entity_list
        return self

    def get_word_entity_list(self):
        return self.__word_entity_list  
    
