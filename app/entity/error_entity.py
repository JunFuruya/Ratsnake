# -*- coding: UTF-8 -*-

from app.entity.base_web_entity import BaseWebEntity

class ErrorEntity(BaseWebEntity):
    __http_status = ''
    __user_error_message = ''
    __manager_error_message = ''
    
    def set_http_status(self, http_status):
        self.__http_status = http_status
        return self
    
    def get_http_status(self):
        return self.__http_status

    def set_user_error_message(self, user_error_message):
        self.__user_error_message = user_error_message
        return self

    def get_user_error_message(self):
        return self.__user_error_message

    def set_manager_error_message(self, manager_error_message):
        self.__manager_error_message = manager_error_message
        return self

    def get_manager_error_message(self):
        return self.__manager_error_message
    
    def to_array(self):
        list = super().to_array()
        list.append(self.__http_status)
        list.append(self.__user_error_message)
        list.append(self.__manager_error_message)
        return list