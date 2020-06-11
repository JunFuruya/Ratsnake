# -*- coding: UTF-8 -*-

from app.entity.base_web_entity import BaseWebEntity

class ClientPersonnelEntity(BaseWebEntity):
    __client_id = ''
    __user_id = ''
    __client_name = ''
    
    def set_error_message(self, error_message):
        self.__error_message = error_message
        return self

    def get_error_message(self):
        return self.__error_message  
    
    def set_client_id(self, client_id):
        self.__client_id = client_id
        return self
    
    def get_client_id(self):
        return self.__client_id
    
    def set_user_id(self, user_id):
        self.user_id = user_id
        return self
    
    def get_user_id(self):
        return self.__user_id
    
    def set_client_name(self, client_name):
        self.__client_name = client_name
        return self
    
    def get_client_name(self):
        return self.__client_name
    
    # TODO to array