# -*- coding: UTF-8 -*-

from app.repository.api_idcf_cloud_repository import ApiIdcfCloudRepository
from app.service.base_service import BaseService

'''
Service Module
'''
class IdcfCloudService(BaseService):
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

