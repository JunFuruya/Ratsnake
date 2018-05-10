#-*- UTF-8 -*-

import app.db

'''
Repository Module
'''
class DbUsersRepository():
    __db = None
    
    def __init__(self):
        self.__db = app.db.DbUsers()
        pass
    
    def exists(self, username, password):
        if(self.__db.count(username, password) > 0):
            return True
        else:
            return False
            
class ApiIdcfCloudRepository():
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