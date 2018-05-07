#-*- UTF-8 -*-

from abc import abstractmethod
from bs4 import BeautifulSoup
import configparser
import urllib3

'''
Service Module
'''
class Base:
    '''
    Base Class
    '''
    _web_host = ''
    _web_port = ''
    _debug = ''
    _reloader = ''
    #USER='test'
    #PASSWORD='test'

    #google_search_url = 'https://www.google.co.jp/search'
    #query = '%E3%82%AF%E3%83%AD%E3%83%BC%E3%83%AA%E3%83%B3%E3%82%B0'
    
    def __init__(self):
        config = configparser.ConfigParser()
        config.read('./config/web_server.ini')
        self._web_host = config['HOST']['ServerName']
        self._web_port = config['HOST']['Port']
        self._debug = config['HOST']['Debug']
        self._reloader = config['HOST']['Reloader']
        pass

    @abstractmethod
    def before_execute(self):
        pass
    
    @abstractmethod
    def execute(self):
        pass
    
    @abstractmethod
    def after_execute(self):
        pass
    
    #def check(user, password):
        #if (user == USER and password == PASSWORD):
        #    response.get_cookie('login', 'test')
        #pass

    #def check_login():
        #hash = request.get_cookie('login')
        #if(hash != 'aaa'):
        #    redirect('/login')
        #pass

    
    #def getSearchList(self):
        #'''
        #get a search list
        #'''
        #html = urllib3.urlopen(google_search_url + '?q=' + query)
        #soup = BeautifulSoup(html)
        #url_list = soup.find("a")
        
        #for url in url_list:
        #    prit(url)    

class configGetService(Base):
    def __init__(self):
        super().__init__()
        
    def get_web_host(self):
        return super()._web_host
    
    def get_web_port(self):
        return self._web_port
    
    def get_debug(self):
        return self._debug
    
    def get_reloader(self):
        return self._reloader

class IdcfCloudStartService(Base):
    '''
    control IDCF cloud
    '''
    idcf_cloud_repository = None
    
    '''
    constructor
    '''
    def __init__(self):
        self.idcf_cloud_repository = IdcfCloudRepository()
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
