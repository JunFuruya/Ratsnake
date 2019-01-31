# -*- coding: UTF-8 -*-

from app.repository.idcf_cloud_repository import IdcfCloudRepository
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
        self.__idcf_cloud_repository = IdcfCloudRepository()
        pass
    
    def start(self):
        '''
        start server
        '''
        self.__idcf_cloud_repository.start()
        pass

    def stop():
        '''
        stop server
        '''
        self.__api_idcf_cloud_repository.stop()
        pass
