# -*- coding: UTF-8 -*-

import datetime

from app.repository.dbdump_repository import DbDumpRepository
from app.service.base_service import BaseService

'''
Service Module
'''
class DbDumpService(BaseService):
    MESSAGE_NO_FILE = 'バックアップファイルはないよ。'

    def __init__(self):
        self.__dbdump_repository = DbDumpRepository()
        
    def create_dump(self, message):
        #self.__dbdump_repository.create()
        pass

    def get_dump_names(self, message):
        file_names = self.__dbdump_repository.get_dump_file_name()
        if file_names is None or len(file_names) == 0:
            message.send(self.MESSAGE_NO_FILE)
        else:
            message.send('\n'.join(file_names))
        pass
    
    def delete_dump(self, message, file_name):
        #self.__dbdump_repository.delete(file_name)

        #file_names = self.get_dump_names(folder_path)
        #if file_names is None:
        #    message.send(message_no_files)

        pass
        