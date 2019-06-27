# -*- coding: UTF-8 -*-

import g

class BaseWebEntity():
    __title = ''
    __description = ''
    __notification = ''
    __error_messages = []
    __records = []
    __login_status = False
    __current_page = 1
    __max_page = 1
    __js_files = []

    def __init__(self):
        self.__js_files = []

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
    
    def set_notification(self, notification):
        self.__notification = notification
        return self

    def get_notification(self):
        return self.__notification
    
    def set_error_messages(self, error_messages):
        self.__error_messages = error_messages
        return self

    def get_error_messages(self):
        return self.__error_messages
    
    def set_records(self, records):
        self.__records = records
        return self

    def get_records(self):
        return self.__records
    
    def to_array(self):
        return [
            self.get_title(),
            self.get_description(),
            self.get_explanation(),
            self.get_records(),
            self.get_error_messages()
        ]

    def set_login_status(self, user_id):
        self.__login_status = True if len(str(user_id)) > 0 else False
        pass

    def get_login_status(self):
        return self.__login_status
    
    def set_current_page(self, page):
        self.__current_page = page
        pass
    
    def get_current_page(self):
        return self.__current_page
    
    def set_max_page(self, max_page):
        self.__max_page = max_page
        pass
    
    def get_max_page(self):
        return self.__max_page
    
    def set_js_files(self, js_files):
        self.__js_files.append(js_files)
    
    def get_js_files(self):
        return self.__js_files
