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
        self.account_titles = {
            'assets' : 1,
            'net_assets' : 2,
            'liability' : 3,
            'revenue' : 4,
            'expense' : 5,
        }
        
    def has_error()
        if(account_title_value in values(self.account_titles)):
            return False
        else:
            return True

    def get():
        return self.__account_title_value