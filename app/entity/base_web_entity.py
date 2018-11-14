# -*- coding: utf-8 -*-

class BaseWebEntity():
    __title = ''
    __description = ''
    __notification = ''
    __error_message = ''
    __records = []

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
    
    def set_error_message(self, error_message):
        self.__error_message = error_message
        return self

    def get_error_message(self):
        return self.__error_message
    
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
            self.get_error_message()
        ]
