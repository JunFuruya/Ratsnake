# -*- coding: UTF-8 -*-

import os, yaml

# CONFIG
app_env = os.getenv('APP_ENV', 'DEVELOPMENT')
if(app_env == 'PRODUCTION'):
    config_folder_path = './config_environment/production/'
elif(app_env == 'STAGING'):
    config_folder_path = './config_environment/staging/'
elif(app_env == 'DEVELOPMENT'):
    config_folder_path = './config_environment/development/'
elif(app_env == 'TEST'):
    config_folder_path = './config_environment/test/'

def get_config(file_name):
    config_file_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), config_folder_path + file_name)
    yaml_file = open(config_file_path , "r", encoding="utf-8")
    yaml_data = yaml.load(yaml_file)
    yaml_file.close()
    return yaml_data

# LOG
from app.helper.log_helper import LogHelper
log = LogHelper().get_instance()

# WEB 
from app.service.web_service import ConfigGetService
config = ConfigGetService().get_web_server_config()

    