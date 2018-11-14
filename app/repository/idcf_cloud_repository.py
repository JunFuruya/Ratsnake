#-*- UTF-8 -*-

from app.infrastructure.idcf_cloud_api import IdcfCloudApi
from app.infrastructure.idcf_cloud_yaml_file import IdcfCloudConfigYamlFile

'''
IdcfCloudRepository Module
'''
class IdcfCloudRepository():
    __idcf_cloud_api = None
    
    def __init__(self):
        '''
        constructor
        '''
        self.__idcf_cloud_api = IdcfCloudApi(IdcfCloudConfigYamlFile())

    def start(self):
        '''
        this starts the server
        '''
        self.__idcf_cloud_api.start_virtual_machine()
        pass
    
    def stop(self):
        '''
        this stops the server
        '''
        self.__idcf_cloud_api.stop_virtual_machine()
        pass
    
    def get_virtual_machine_list(self):
        self.__idcf_cloud_api.get_virtual_machine_list()
        pass