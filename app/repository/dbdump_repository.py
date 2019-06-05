# -*- coding: UTF-8 -*-

import datetime, os

import g

from app.infrastructure.dbdump_file import DbDumpFile

class DbDumpRepository():
    DB_CONFIG_FILE_NAME = 'db_config.yaml'

    def __init__(self):
        self.__dbdump_file = DbDumpFile()
        pass
    
    def get_dump_file_name(self):
        db_config = g.get_config(self.DB_CONFIG_FILE_NAME)
        folder_path = db_config['dump']['folder_path']
        return self.__dbdump_file.get_file_names(folder_path)
    
    def create(self):
        db_config = g.get_config(self.DB_CONFIG_FILE_NAME)
        
        datetime_today = datetime.date.today()
        prefix = db_config['dump']['file_name_prefix']
        extension = db_config['dump']['file_extension']
        file_name = prefix + datetime_today.strftime('%Y%m%d') + extension
        folder_path = db_config['dump']['folder_path']
        
        self.__dbdump_file.create(folder_path, file_name)
        pass
    
    def delete(self, file_name):
        # TODO config から読み込む
        #folder_name = ''
        #os.remove(os.path.join(folder_name, file_name))
        pass
