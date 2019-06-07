# -*- coding: UTF-8 -*-

from app.validator.base_validator import BaseValidator

class LinkCategoryValidator(BaseValidator):
    def __init__(self):
        pass
        
    def get_error_messages(self, link_category_name, link_category_display_order):
        self.__link_category_name = link_category_name
        self.__link_category_display_order = link_category_display_order

        self.__validate()

        return super().get_error_messages()

    def __validate(self):
        error_messages = []
        if(self.has_empty_error(self.__link_category_name)):
            error_messages.append('リンクカテゴリ名称が入力されていません。')
        if(self.has_too_large_number_error(self.__link_category_name, 100)):
            error_messages.append('リンクカテゴリ名称は100文字以内で入力してください。')
        if(self.has_empty_error(self.__link_category_display_order)):
            error_messages.append('リンクカテゴリ表示順序が入力されていません。')
        if(self.has_too_large_number_error(self.__link_category_display_order, 3)):
            error_messages.append('リンクカテゴリ名称は3文字以内で入力してください。')
        if(self.has_full_width_hiragana_characters_error(self.__link_category_display_order)):
            error_messages.append('リンクカテゴリ名称は半角数値で入力してください。')
        if(self.has_full_width_katakana_characters_error(self.__link_category_display_order)):
            error_messages.append('リンクカテゴリ名称は半角数値で入力してください。')
        if(self.has_full_width_number_characters_error(self.__link_category_display_order)):
            error_messages.append('リンクカテゴリ名称は半角数値で入力してください。')
        if(self.has_full_width_alphabet_characters_error(self.__link_category_display_order)):
            error_messages.append('リンクカテゴリ名称は半角数値で入力してください。')
        if(self.has_full_width_special_characters_error(self.__link_category_display_order)):
            error_messages.append('リンクカテゴリ名称は半角数値で入力してください。')
        
        super().set_error_messages(error_messages)
        pass
    