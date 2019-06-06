# -*- coding: UTF-8 -*-

from app.repository.slack_repository import SlackRepository
from app.service.base_service import BaseService

'''
Service Module
'''
class SlackService(BaseService):
    __slack_repository = None

    def __init__(self):
        self.__slack_reposiroty = SlackRepository()
        
    def run(self):
        self.__slack_reposiroty.run()
    