#-*- UTF-8 -*-

from bs4 import BeautifulSoup
import configparser
import urllib3

from app.repository.api_idcf_cloud_repository import ApiIdcfCloudRepository
from app.repository.app_slack_repository import AppSlackRepository
from app.repository.db_users_repository import DbUsersRepository
from app.repository.file_web_server_config_repository import FileWebServerConfigRepository

'''
Service Module
'''
class ConfigGetService():
    __repository = None

    def __init__(self):
        self.__repository = FileWebServerConfigRepository()
        pass
    
    def get_web_server_config(self):
        return self.__repository.get_web_server_config()

class LoginService():
    __repository = None
    def __init__(self):
        self.__repository = DbUsersRepository()
        pass
        
    def is_authenticated(self, username, password):
        return self.__repository.exists(username, password)
    
class SlackBotStartService():
    __slack_bot_repository = None
    def __init__(self):
        self.__slack_bot_reposiroty = AppSlackRepository()
        
    def run(self):
        self.__slack_bot_reposiroty.run()

class IdcfCloudStartService():
    __idcf_cloud_repository = None
    
    '''
    constructor
    '''
    def __init__(self):
        self.__api_idcf_cloud_repository = ApiIdcfCloudRepository()
        pass
    
    def start(self):
        '''
        start server
        '''
        self.__api_idcf_cloud_repository.start()
        pass

    def stop():
        '''
        stop server
        '''
        self.__api_idcf_cloud_repository.stop()
        pass

    #controller = None
    #\view = None
    #controllers = []
    #
    #def __init__(self):
    #  self.controllers.insert(values.screenIdValue.DEFAULT(), controller.IndexController())
    #  self.controllers.insert(values.screenIdValue.GOOGLE_SEARCH(), controller.GoogleSearchController())
    #
    #def execute(self):
    #    print('execute')
    #    
    #    self.changeScreen(values.screenIdValue.DEFAULT())
    
    #def changeScreen(self, screenId):
    #    self.controller = self.controllers[screenId]
    #    self.view = self.controller.getView()
    #    self.view.setViewParams(controller.getViewParams())
