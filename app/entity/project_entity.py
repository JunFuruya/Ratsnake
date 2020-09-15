# -*- coding: UTF-8 -*-

from app.entity.base_web_entity import BaseWebEntity
#from app.value.values import AccountTitleClassificationTypeValue

class ProjectEntity(BaseWebEntity):
    
    def set_error_message(self, error_message):
        self.__error_message = error_message
        return self

    def get_error_message(self):
        return self.__error_message  

    def get_project_id(self):
        return self.__project_id

    def set_project_id(self, project_id):
        self.__project_id
        return self

    def get_project_name(self):
        return self.__project_name

    def set_project_name(self, project_name):
        self.__project_name = project_name
        return self

    def get_project_type(self):
        return self.__project_type

    def set_project_type(self, project_type):
        self.__project_type
        return self

    def get_note(self):
        return self.__note

    def set_note(self, note):
        self.__note = note
        return self

    # TODO to array