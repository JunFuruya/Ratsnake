# -*- coding: UTF-8 -*-

from bs4 import BeautifulSoup
import configparser
import urllib3

from app.service.base_service import BaseService
from app.repository.idcf_cloud_repository import IdcfCloudRepository
from app.repository.user_repository import UsersRepository
from app.repository.web_server_config_repository import WebServerConfigRepository

'''
Web Server Config Service Module
'''
class ConfigGetService():
    __repository = None

    def __init__(self):
        self.__repository = WebServerConfigRepository()
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

class IdcfCloudStartService():
    __idcf_cloud_repository = None
    
    '''
    constructor
    '''
    def __init__(self):
        self.__api_idcf_cloud_repository = IdcfCloudRepository()
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
