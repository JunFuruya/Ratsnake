# -*- coding: utf-8 -*-

import configparser
import json
import os
import pycurl
import re
import requests

'''
IDCF Cloud module
'''
class ApiIdcfCloud():
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
