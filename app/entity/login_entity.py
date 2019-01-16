# -*- coding: UTF-8 -*-

from app.entity.base_web_entity import BaseWebEntity

class LoginEntity(BaseWebEntity):
    __user_id = ''
    __username = ''
    
    def __init__(self):
        super().__init__()
        pass
    
    def set_user_id(self, user_id):
        self.__user_id = user_id
        pass
    
    def get_user_id(self):
        return self.__user_id
    
    def set_username(self, username):
        self.__username = username
        pass

    def get_username(self):
        return self.__username
    
    def to_array(self):
        login_entity_list = super().__init__();
        return login_entity_list