# -*- coding: UTF-8 -*-

from app.entity.base_web_entity import BaseWebEntity

class LanguageEntity(BaseWebEntity):
    __language_id = ''
    __user_id = ''
    __language_name = ''
    
    def set_error_message(self, error_message):
        self.__error_message = error_message
        return self

    def get_error_message(self):
        return self.__error_message  
    
    def set_language_id(self, language_id):
        self.__language_id = language_id
        return self
    
    def get_language_id(self):
        return self.__language_id
    
    def set_user_id(self, user_id):
        self.user_id = user_id
        return self
    
    def get_user_id(self):
        return self.__user_id
    
    def set_language_name(self, language_name):
        self.__language_name = language_name
        return self
    
    def get_language_name(self):
        return self.__language_name
    
    # TODO to array