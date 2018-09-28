# -*- coding: utf-8 -*-

from app.entity.base_web_entity import BaseWebEntity

class WordEntity(BaseWebEntity):
    __word_id = ''
    __user_id = ''
    __word_name = ''
    
    def set_error_message(self, error_message):
        self.__error_message = error_message
        return self

    def get_error_message(self):
        return self.__error_message  
    
    def set_word_id(self, word_id):
        self.__word_id = word_id
        return self
    
    def get_word_id(self):
        return self.__word_id
    
    def set_user_id(self, user_id):
        self.user_id = user_id
        return self
    
    def get_user_id(self):
        return self.__user_id
    
    def set_word_name(self, word_name):
        self.__word_name = word_name
        return self
    
    def get_word_name(self):
        return self.__word_name
    
    # TODO to array