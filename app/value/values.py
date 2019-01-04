# -*- coding: UTF-8 -*-

class Values():
    def __init__(self):
        return None

class ScreenIdValue():
    def DEFAULT():
        return 0
    
    def GOOGLE_SEARCH():
        return 1
    
class AccountTitleClassificationTypeValue():
    def __init__(self, account_title_value):
        self.__account_title_value = account_title_value
        self.__account_titles = {
            1: '資産',
            2: '負債',
            3: '資本',
            4: '費用',
            5: '収益',
        }

    def has_error(self):
        if(self.__account_title_value in values(self.__account_titles)):
            return False
        else:
            return True

    def get(self):
        return self.__account_title_value
    
    def get_name(self):
        return self.__account_titles[int(self.__account_title_value)]