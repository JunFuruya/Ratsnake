# -*- coding: UTF-8 -*-

from vendor.slackbot.bot import Bot

class SlackRepository():
    __bot = None
    def __init__(self):
        self.__bot = Bot()
        pass
    
    def run(self):
        self.__bot.run()
        pass