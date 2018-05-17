# -*- coding: utf-8 -*-

import os
import yaml

class BaseYamlFile():
    __config = None
    __config_file_path = ''

    def __init__(self):
        pass
    
    def get_config(self, file_name):
        config_folder_path = '../../config/'
        app_env = os.getenv('APP_ENV', 'DEVELOPMENT')
        if(app_env == 'PRODUCTION'):
            config_folder_path = '../../config_environment/production/'
        elif(app_env == 'STAGING'):
            config_folder_path = '../../config_environment/staging/'
        elif(app_env == 'DEVELOPMENT'):
            config_folder_path = '../../config_environment/development/'
        elif(app_env == 'TEST'):
            config_folder_path = '../../config_environment/test/'
        self.__config_file_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), config_folder_path + file_name)
        yaml_file = open(self.__config_file_path , "r", encoding="utf-8")
        self.__yaml_data = yaml.load(yaml_file)
        yaml_file.close()
        
        return self.__yaml_data
