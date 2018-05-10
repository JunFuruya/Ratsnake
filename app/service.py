#-*- UTF-8 -*-

from bs4 import BeautifulSoup
import configparser
import urllib3
import app.repository

'''
Service Module
'''
class configGetService():
    __web_host = ''
    __web_port = ''
    __debug = ''
    __reloader = ''
    #USER='test'
    #PASSWORD='test'

    def __init__(self):
        config = configparser.ConfigParser()
        config.read('./config/web_server.ini')
        self.__web_host = config['HOST']['ServerName']
        self.__web_port = config['HOST']['Port']
        self.__debug = config['HOST']['Debug']
        self.__reloader = config['HOST']['Reloader']
        pass
    
    def get_web_host(self):
        return self.__web_host
    
    def get_web_port(self):
        return self.__web_port
    
    def get_debug(self):
        return self.__debug
    
    def get_reloader(self):
        return self.__reloader

class LoginService():
    __repository = None
    def __init__(self):
        self.__repository = app.repository.DbUsersRepository()
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
        self.idcf_cloud_repository = ApiIdcfCloudRepository()
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
