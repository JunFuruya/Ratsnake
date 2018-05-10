# -*- coding: utf-8 -*-

import configparser
import pycurl
import requests

'''
Slack module
'''
class Slack():
    '''
    manage slack
    '''
    def __init__(self, url):
        self.target_url = url
    
    def postMessage(self, message):
        headers = {'Content-type': 'application/json'}
        payload = {'text': message}
        response = requests.post(target_url, data=json.dumps(payload), headers=headers)
