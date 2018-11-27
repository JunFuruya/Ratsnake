# -*- coding: UTF-8 -*-

# TODO move to another folder
import pycurl
import requests

'''
Slack module
'''
class SlackConfigIniFile():
    __yml_file
    '''
    manage slack
    '''
    def __init__(self):
        # TODO move to another folder
        #self.target_url = url
        super().__init__("slack_config.yaml")

    # TODO move to another folder
    #def post_message(self, message):
        #headers = {'Content-type': 'application/json'}
        #payload = {'text': message}
        #response = requests.post(target_url, data=json.dumps(payload), headers=headers)
