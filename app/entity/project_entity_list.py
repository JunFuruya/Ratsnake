# -*- coding: UTF-8 -*-

from app.entity.base_web_entity import BaseWebEntity

class ProjectListEntity(BaseWebEntity):
    __project_entity_list = []

    def set_project_entity_list(self, project_entity_list):
        self.__project_entity_list = project_entity_list
        return self

    def get_project_entity_list(self):
        return self.__project_entity_list