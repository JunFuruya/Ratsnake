# -*- coding: utf-8 -*-

from app.helper.helper import HashHelper

class UserEntity:
    __user_id = None
    __user_username = ''
    __user_hashed_password = ''
    
    def set_user_id(self):
        return self
    
    def get_user_id(self):
        return self.__user_id
    
    def set_user_username(self):
        return self
    
    def get_user_username(self):
        return self.__user_username
    
    def set_user_hashed_password(self):
        return self
    
    def get_user_hashed_password(self):
        return self.__user_hashed_password
    
    def　to_array(self):
        # TODO: implement
        pass