# -*- coding: utf-8 -*-

from app.entity.base_web_entity import BaseWebEntity

class LinkCategoryEntity(BaseWebEntity):
    __link_category_id = ''
    __user_id = ''
    __link_category_name = ''
    __link_category_display_order = ''
    
    def set_error_message(self, error_message):
        self.__error_message = error_message
        return self

    def get_error_message(self):
        return self.__error_message  
    
    def set_link_category_id(self, link_category_id):
        self.__link_category_id = link_category_id
        return self
    
    def get_link_category_id(self):
        return self.__link_category_id
    
    def set_user_id(self, user_id):
        self.user_id = user_id
        return self
    
    def get_user_id(self):
        return self.__user_id
    
    def set_link_category_name(self, link_category_name):
        self.__link_category_name = link_category_name
        return self
    
    def get_link_category_name(self):
        return self.__link_category_name
    
    def set_link_category_display_order(self, link_category_display_order):
        self.__link_category_display_order = link_category_display_order
        return self

    def get_link_category_display_order(self):
        return self.__link_category_display_order
    # TODO to array
