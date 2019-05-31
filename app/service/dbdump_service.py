# -*- coding: UTF-8 -*-

import datetime

from app.repository.dbdump_repository import DbDumpRepository
from app.service.base_service import BaseService

'''
Service Module
'''
class DbDumpService(BaseService):
    __dbdump_repository = None

    def __init__(self):
        self.__dbdump_repository = DbDumpRepository()
        pass
        
    def create_dump(self):
        #datetime_today = datetime.date.today()
        #file_name = 'dunmp_' + datetime_today.strftime('%Y%m%d')
        #self.__dbdump_repository.create(file_name)
        pass

    def get_dump_names(self, folder_path):
        return self.__dbdump_repository.get_dump_file_name(folder_path)
    
    def delete_dump(self, file_name):
        #self.__dbdump_repository.delete(file_name)
        pass
        