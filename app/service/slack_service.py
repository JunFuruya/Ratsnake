#-*- UTF-8 -*-

from app.repository.app_slack_repository import AppSlackRepository
from app.service.base_service import BaseService

'''
Service Module
'''
class SlackBotStartService(BaseService):
    __slack_bot_repository = None
    def __init__(self):
        self.__slack_bot_reposiroty = AppSlackRepository()
        
    def run(self):
        self.__slack_bot_reposiroty.run()
