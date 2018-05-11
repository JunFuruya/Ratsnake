#-*- UTF-8 -*-

'''
ApiIdcfCloudRepository Module
'''
class ApiIdcfCloudRepository():
    '''
    ApiIdcfCloudRepository
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