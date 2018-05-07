#-*- UTF-8 -*-

'''
Repository Module
'''


class BaseRepository:
    '''
    BaseRepository
    '''


class IdcfCloudRepository:
    '''
    IdcfCloudRepository
    '''
    
    def __init__(self):
        '''
        constructor
        '''
        self.idcf_cloud_api = IdcfCloudApi()

    def start(self):
        '''
        this starts the server
        '''
        self.idcf_cloud_api.start_server()
        pass
    
    def stop(self):
        '''
        this stops the server
        '''
        self.idcf_cloud_api.stop_server()
        pass