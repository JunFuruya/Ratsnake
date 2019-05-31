# -*- coding: UTF-8 -*-

import os

from app.infrastructure.dbdump_file import DbDumpFile

class DbDumpRepository():
    __bot = None
    def __init__(self):
        self.__dbdump_file = DbDumpFile()
        pass
    
    def get_dump_file_name(self, folder_path):
        #return self.__dbdump_file.get_file_names(folder_path)
        pass
    
    def create(self, file_name):
        # TODO config から読み込む
        #folder_name = ''
        #os.path.isfile(os.path.join(folder_name, file_name))
        pass
    
    def delete(self, file_name):
        # TODO config から読み込む
        #folder_name = ''
        #os.remove(os.path.join(folder_name, file_name))
        pass
