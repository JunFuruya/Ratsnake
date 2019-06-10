# -*- coding: UTF-8 -*-

from app.validator.base_validator import BaseValidator

class LinkValidator(BaseValidator):
    def __init__(self):
        pass
        
    def get_error_messages(self, link_site_name, link_url, link_display_order):
        self.__link_site_name = link_site_name
        self.__link_url = link_url
        self.__link_display_order = link_display_order

        self.__validate()

        return super().get_error_messages()

    def __validate(self):
        if(self.has_empty_error(self.__link_site_name)):
            super().error_messages.append('リンク名称が入力されていません。')
        if(self.has_too_large_number_error(self.__link_site_name, 100)):
            super().error_messages.append('リンク名称は100文字以内で入力してください。')
        if(self.has_empty_error(self.__link_url)):
            super().error_messages.append('リンクURLが入力されていません。')
        if(self.has_too_large_number_error(self.__link_url, 200)):
            super().error_messages.append('リンクURLは200文字以内で入力してください。')
        if(self.has_empty_error(self.__link_url)):
            super().error_messages.append('リンク表示順序が入力されていません。')
        if(self.has_too_large_number_error(self.__link_display_order, 200)):
            super().error_messages.append('リンク表示順序は3桁以内で入力してください。')
        pass
    