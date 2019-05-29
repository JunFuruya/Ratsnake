# -*- coding: UTF-8 -*-

import datetime

from app.repository.dbdump_repository import DbdumpRepository
from app.service.base_service import BaseService

'''
Service Module
'''
class DbDumpService(BaseService):
    __dbdump_repository = None

    def __init__(self):
        self.__dbdump_repository = DbdumpRepository()
        pass
        
    def create_dump(self):
        datetime_today = datetime.date.today()
        file_name = 'dunmp_' + datetime_today.strftime('%Y%m%d')
        self.__dbdump_repository.create(file_name)
        pass

    def get_dump_names(self):
        return file_names

    def delete_dump(self, file_name):
        self.__dbdump_repository.delete(file_name)
        pass
        