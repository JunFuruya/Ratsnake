# -*- coding: utf-8 -*-

import configparser
import json
import os
import pycurl
import re
import requests

'''
infrastructure module
'''
class Slack:
    '''
    manage slack
    '''
    def __init__(self, url):
        self.target_url = url
    
    def postMessage(self, message):
        headers = {'Content-type': 'application/json'}
        payload = {'text': message}
        response = requests.post(target_url, data=json.dumps(payload), headers=headers)

class File:
    '''
    manage file
    '''
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

# -*- coding: utf-8 -*-

class IdcfCloudApi:
    '''
    manage idcf cloud
    '''
    def __init__():
        self.inifile = configparser.ConfigParser()
        self.inifile.read('/app/config/idcf_cloud.ini', 'UTF-8')
        self.url = self.inifile.get('default', 'url')
        self.server_id = self.inifile.get('default', 'server_id')
        pass
    
    def start_server():
        pass
    
    def stop_server():
        pass

