# -*- coding: UTF-8 -*-

import os

import g

from app.infrastructure.dbdump_file import DbDumpFile

class DbDumpRepository():
    __bot = None
    def __init__(self):
        self.__dbdump_file = DbDumpFile()
        pass
    
    def get_dump_file_name(self):
        db_config = g.get_config('db_config.yaml')
        folder_path = db_config['dump']['folder_path']
        return self.__dbdump_file.get_file_names(folder_path)
    
    def create(self):
        #datetime_today = datetime.date.today()
        #prefix = db_config['dump']['file_name_prefix']
        #extension = db_config['dump']['file_extension']
        #file_name = prefix + datetime_today.strftime('%Y%m%d') + extension
        #self.__dbdump_file.create_file(file_name)
        pass
    
    def delete(self, file_name):
        # TODO config から読み込む
        #folder_name = ''
        #os.remove(os.path.join(folder_name, file_name))
        pass
