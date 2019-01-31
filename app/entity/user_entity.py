# -*- coding: UTF-8 -*-

from app.entity.base_web_entity import BaseWebEntity

from app.helper.hash_helper import HashHelper

class UserEntity(BaseWebEntity):
    __user_id = None
    __user_username = ''
    __user_hashed_password = ''
    
    def set_user_id(self, user_id):
        self.__user_id = user_id
        return self
    
    def get_user_id(self):
        return self.__user_id
    
    def set_user_username(self, user_username):
        self.__user_username = user_username
        return self
    
    def get_user_username(self):
        return self.__user_username
    
    def set_user_hashed_password(self, user_hashed_password):
        self.__user_hashed_password = user_hashed_password
        return self
    
    def get_user_hashed_password(self):
        return self.__user_hashed_password
    
    #def　to_array(self):
        # TODO: implement
        #pass