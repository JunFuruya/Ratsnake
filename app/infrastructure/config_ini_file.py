# -*- coding: UTF-8 -*-

import configparser
import os

'''
file module
'''
class BaseIniFile():
    __config = None
    __config_file_path = ''

    def __init__(self, file_name):
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

        self.__config = configparser.ConfigParser()
        self.__config.read(self.__config_file_path)

        pass

    def get_config(self, section_name):
        return self.__config[section_name].values()
    
class WebServerConfigIniFile(BaseIniFile):
    def __init__(self):
        super().__init__('web_server.ini')
        pass
    
    def get_config(self):
        return super().get_config('HOST')
    
class DbServerConfigIniFile(BaseIniFile):
    def __init__(self):
        super().__init__('db_server.ini')
        pass
    
    def get_config(self):
        return super().get_config('MySQL')
    
# 読み込みなので、第２引数は「r」とする
#    file = open(file_path, 'r', encoding="utf-8")

#    line_num = 1
#    for line in file:
#      if re.search(pattern, line):
#        text = line.replace('\r', '')
#        text = text.replace('\n', '')
#        self.todo_list[file.name + ':' + str(line_num)] = text

#      line_num += 1
  
#    file.close()

  #################################################
  # ファイルを再起的に調べる
  #################################################
#  def searchFiles(self, dir_path):
#    entries = os.scandir(dir_path)
  
#    for entry in entries:
#      if entry.is_dir():
#        self.searchFiles(entry.path)
    
#      elif entry.is_file():
#        self.searchTodos(entry.path)

#    entries.close()
