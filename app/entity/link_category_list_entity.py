# -*- coding: utf-8 -*-

from app.entity.base_web_entity import BaseWebEntity

class LinkCategoryListEntity(BaseWebEntity):
    __link_category_entity_list = []
    
    def set_link_category_entity_list(self, link_category_entity_list):
        self.__link_category_entity_list = link_category_entity_list
        return self

    def get_link_category_entity_list(self):
        return self.__link_category_entity_list