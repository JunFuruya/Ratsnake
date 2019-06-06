# -*- coding: UTF-8 -*-

import datetime, os

import g

from app.infrastructure.dbdump_file import DbDumpFile

class DbDumpRepository():
    DB_CONFIG_FILE_NAME = 'db_config.yaml'

    def __init__(self):
        self.__dbdump_file = DbDumpFile()

        self.__db_config = g.get_config(self.DB_CONFIG_FILE_NAME)
        self.__folder_path = self.__db_config['dump']['folder_path']
        pass
    
    def get_dump_file_name(self):
        return self.__dbdump_file.get_file_names(self.__folder_path)
    
    def create(self):
        
        datetime_today = datetime.date.today()
        prefix = self.__db_config['dump']['file_name_prefix']
        extension = self.__db_config['dump']['file_extension']
        file_name = prefix + datetime_today.strftime('%Y%m%d') + extension
        
        self.__dbdump_file.create(self.__folder_path, file_name)
        pass
    
    def delete(self, file_name):
        self.__dbdump_file.delete(self.__folder_path, file_name)
        pass
