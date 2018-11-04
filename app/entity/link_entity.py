# -*- coding: utf-8 -*-

from app.entity.base_web_entity import BaseWebEntity

class LinkEntity(BaseWebEntity):
    __link_id = ''
    __link_category_id = ''
    __link_site_name = ''
    __link_url = ''
    __link_display_order = ''
    __link_entity_list = []

    def set_link_id(self, link_id):
        self.__link_id = link_id
        return self

    def get_link_id(self):
        return self.__link_id

    def set_url_id(self, link_id):
        self.__link_id = link_id
        return self

    def get_url_id(self):
        return self.__link_id

    def set_link_category_id(self, link_category_id):
        self.__link_category_id = link_category_id
        return self

    def get_link_category_id(self):
        return self.__link_category_id

    def set_link_site_name(self, link_site_name):
        self.__link_site_name = link_site_name
        return self

    def get_link_site_name(self):
        return self.__link_site_name

    def set_link_url(self, link_url):
        self.__link_url = link_url
        return self

    def get_link_url(self):
        return self.__link_url

    def set_link_display_order(self, link_display_order):
        self.__link_display_order = link_display_order
        return self

    def get_link_display_order(self):
        return self.__link_display_order
