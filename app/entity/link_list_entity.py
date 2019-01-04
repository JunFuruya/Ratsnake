# -*- coding: UTF-8 -*-

from app.entity.base_web_entity import BaseWebEntity

class LinkListEntity(BaseWebEntity):
    __link_entity_list = []

    def set_link_entity_list(self, link_entity_list):
        self.__link_entity_list = link_entity_list
        return self

    def get_link_entity_list(self):
        return self.__link_entity_list