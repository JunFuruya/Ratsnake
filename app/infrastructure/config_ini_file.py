# -*- coding: utf-8 -*-

import configparser

'''
file module
'''
class WebServerConfigIniFile():
    __url = './config/web_server.ini'
    __config = None
    
    def __init__(self):
        self.__config = configparser.ConfigParser()
        self.__config.read(self.__url)
        pass
    
    def get_config(self):
        return self.__config
    
class DbServerConfigIniFile():
    __url = './config/db_server.ini'
    __config = None
    
    def __init__(self):
        self.__config = configparser.ConfigParser()
        self.__config.read(self.__url)
        pass
    
    def get_config(self):
        return self.__config

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
