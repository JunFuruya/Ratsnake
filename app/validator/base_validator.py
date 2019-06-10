# -*- coding: UTF-8 -*-

import os.path
import re

class BaseValidator():
    error_messages = []
    def __init__(self):
        self.error_messages = []
        pass

    def get_error_messages(self):
        return self.error_messages

    # 必須入力チェック
    def has_empty_error(self, string):
        return True if (len(string) == 0) else False 

    # 文字数超過
    def has_too_large_number_error(self, string, max):
        return True if (len(string) > max) else False 

    # 文字数不足
    def has_too_short_number_error(self, string, min):
        return True if (len(string) < min) else False 

    # 範囲外の文字数
    def has_out_of_number_range_error(self, string, min, max):
        return True if (len(string) < min or len(string) > max) else False 

    # 平仮名
    def has_full_width_katakana_characters_error(self, string):
        return True if (re.search(r'[\u3041-\u3093]+', string)) else False 

    # 全角カタカナ
    def has_full_width_katakana_characters_error(self, string):
        return True if (re.search(r'[\u30A1-\u30F4]+', string)) else False 

    # 半角カタカナ
    def has_half_width_katakana_characters_error(self, string):
        return True if (r'[\u0xA1-\u0xDF]+') else False 

    # 全角英字
    def has_full_width_alphabet_characters_error(self, string):
        return True if (re.search(r'([\uFF21-\uFF3A]|[\uFF41-\uFF5A])+', string)) else False 

    # 半角英字
    def has_half_width_alphabet_characters_error(self, string):
        return True if (re.search(r'[]+', string)) else False 

    # 全角数字
    def has_full_width_number_characters_error(self, string):
        return True if (name == '') else False 

    # 半角数字
    def has_half_width_number_characters_error(self, string):
        return True if (re.search(r'(\d)+', string)) else False 

    # 全角記号
    def has_full_width_special_characters_error(self, string):
        return True if (r'（[\uFF01-\uFF20]|[\uFF01-\uFF20]|[\uFF3B-\uFF40]|[\uFF5B-\uFF5E])+') else False 

    # 半角記号
    def has_half_width_special_characters_error(self, string):
        return True if (name == '') else False 

    # リストにないキーの判定
    def has_half_width_special_characters_error(self, string):
        return True if (name == '') else False 

    # 値の同一性の判定
    def has_half_width_special_characters_error(self, string):
        return True if (name == '') else False 

    # ファイル存在チェック
    def file_exists(self, file_path):
        return os.path.isfile(file_path)

    # 拡張子チェック
    def has_inappropriate_file_extention_error(self, file_path, intended_extention):
        root, input_extention = os.path.splitext(path)
        return False if (input_extention == '.' + intended_extention) else True