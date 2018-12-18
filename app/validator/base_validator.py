# -*- coding: UTF-8 -*-

class base_validator():
    __data = []
    __error_messages = []

    def __init__(self, data):
        self.__data = data
        pass

    def get_error_messages(self):
        return self.__error_messages

    # 必須入力チェック
    def has_empty_error(self, name):
        return True if (name == '') else False 

    # 文字数超過
    def has_too_large_number_error(self, string, max):
        return True if (name == '') else False 

    # 文字数不足
    def has_too_short_number_error(self, string, min):
        return True if (name == '') else False 

    # 範囲外の文字数
    def has_out_of_number_range_error(self, string, min, max):
        return True if (name == '') else False 

    # 平仮名
    def has_full_width_katakana_characters_error(self, string):
        return True if (name == '') else False 

    # 全角カタカナ
    def has_full_width_katakana_characters_error(self, string):
        return True if (name == '') else False 

    # 半角カタカナ
    def has_half_width_katakana_characters_error(self, string):
        return True if (name == '') else False 

    # 全角英字
    def has_full_width_alphabet_characters_error(self, string):
        return True if (name == '') else False 

    # 半角英字
    def has_half_width_alphabet_characters_error(self, string):
        return True if (name == '') else False 

    # 全角数字
    def has_full_width_number_characters_error(self, string):
        return True if (name == '') else False 

    # 半角数字
    def has_half_width_number_characters_error(self, string):
        return True if (name == '') else False 

    # 全角記号
    def has_full_width_special_characters_error(self, string):
        return True if (name == '') else False 

    # 半角記号
    def has_half_width_special_characters_error(self, string):
        return True if (name == '') else False 

    # 半角記号
    def has_half_width_special_characters_error(self, string):
        return True if (name == '') else False 

    # 半角記号
    def has_half_width_special_characters_error(self, string):
        return True if (name == '') else False 
