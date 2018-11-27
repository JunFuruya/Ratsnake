# -*- coding: UTF-8 -*-

from app.infrastructure.base_yaml_file import BaseYamlFile

'''
Web Server module
'''
class WebServerConfigYamlFile(BaseYamlFile):
    __FILE_NAME = 'web_server.yaml'
    
    def __init__(self):
        super().__init__(self.__FILE_NAME)
        pass
    
    def get_config(self):
        return super().get_config().values()