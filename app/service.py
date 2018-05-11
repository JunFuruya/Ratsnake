#-*- UTF-8 -*-

from bs4 import BeautifulSoup
import configparser
import urllib3

from app.repository import api_idcf_cloud_repository
from app.repository import db_users_repository
from app.repository import file_web_server_config_repository

'''
Service Module
'''
class ConfigGetService():
    __repository = None

    def __init__(self):
        self.__repository = file_web_server_config_repository.FileWebServerConfigRepository()
        pass
    
    def get_web_server_config(self):
        return self.__repository.get_web_server_config()

class LoginService():
    __repository = None
    def __init__(self):
        self.__repository = db_users_repository.DbUsersRepository()
        pass
        
    def is_authenticated(self, username, password):
        return self.__repository.exists(username, password)

class IdcfCloudStartService():
    '''
    control IDCF cloud
    '''
    idcf_cloud_repository = None
    
    '''
    constructor
    '''
    def __init__(self):
        self.idcf_cloud_repository = api_idcf_cloud_repository.ApiIdcfCloudRepository()
        pass
    
    def start():
        '''
        start server
        '''
        self.idcf_cloud_repository.start()
        pass

    def stop():
        '''
        stop server
        '''
        self.idcf_cloud_repository.stop()
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
