# -*- coding: utf-8 -*-

class BaseWebEntity():
    __title = ''
    __description = ''

    def set_title(self, title):
        self.__title = title
        return self

    def get_title(self):
        return self.__title

    def set_description(self, description):
        self.__description = description
        return self

    def get_description(self):
        return self.__description
    
    def to_array(self):
        base_web_list = [
            self.get_title(),
            self.get_description()
        ]
        return base_web_list