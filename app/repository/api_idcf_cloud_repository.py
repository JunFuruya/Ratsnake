#-*- UTF-8 -*-

from app.infrastructure.idcf_cloud_api import IdcfCloudApi
from app.service.base_service import BaseService

'''
ApiIdcfCloudRepository Module
'''
class ApiIdcfCloudRepository(BaseService):
    '''
    ApiIdcfCloudRepository
    '''
    __idcf_cloud_api = None
    
    def __init__(self):
        '''
        constructor
        '''
        self.__idcf_cloud_api = IdcfCloudApi()

    def start(self):
        '''
        this starts the server
        '''
        self.__idcf_cloud_api.start_server()
        pass
    
    def stop(self):
        '''
        this stops the server
        '''
        self.__idcf_cloud_api.stop_server()
        pass