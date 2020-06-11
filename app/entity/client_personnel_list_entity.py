# -*- coding: UTF-8 -*-

from app.entity.base_web_entity import BaseWebEntity

class ClientPersonnelListEntity(BaseWebEntity):
    __user_entity_list = []
    
    def set_user_entity_list(self, user_entity_list):
        self.__user_entity_list = user_entity_list
        return self

    def get_user_entity_list(self):
        return self.__user_entity_list