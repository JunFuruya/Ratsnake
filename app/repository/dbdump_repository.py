# -*- coding: UTF-8 -*-

import os

from vendor.slackbot.bot import Bot

class SlackRepository():
    __bot = None
    def __init__(self):
        self.__bot = Bot()
        pass
    
    def create(self, file_name):
        # TODO config から読み込む
        folder_name = ''
        os.path.isfile(os.path.join(folder_name, file_name))
        pass
    
    def delete(self, file_name):
        # TODO config から読み込む
        folder_name = ''
        os.remove(os.path.join(folder_name, file_name))