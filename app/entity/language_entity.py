# -*- coding: utf-8 -*-

class LanguageEntity():
    __language_id = ''
    __user_id = ''
    __language_name = ''
    
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
    
    def　to_dict(self):
        return {
            "language_id" : self.__language_id,
            "user_id" : self.__user_id,
            "language_name" : self.__language_name
        }