# -*- coding: utf-8 -*-

from app.infrastructure.base_yaml_file import BaseYamlFile

class SlackConfigYamlFile(BaseYamlFile):
    __FILE_NAME = 'slack_config.yaml'
    
    def __init__(self):
        super().__init__()
        pass
    
    def get_config(self):
        return super().get_config(self.__FILE_NAME).values()