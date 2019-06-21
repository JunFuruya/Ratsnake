# -*- coding: UTF-8 -*-

import os, subprocess

import g

from app.infrastructure.base_file import BaseFile

'''
dbdump file module
'''
class DbDumpFile(BaseFile):
    DB_CONFIG_FILE_NAME = 'db_config.yaml'

    def __init__(self):
        super().__init__()
        pass

    def get_file_names(self, folder_path):
        return super().get_file_names(folder_path)

    def create(self, folder_path, file_name):
        db_config = g.get_config(self.DB_CONFIG_FILE_NAME)
        command = 'mysqldump -u' + db_config['dump']['user'] + ' -p ' + db_config['dump']['database'] \
                  + ' > ' + os.path.join(folder_path, file_name)

        try:
            subprocess.call(command)
        except FileNotFoundError:
            g.log.error('No file found or no path to mysqldump command')
            
        pass
    
    def delete(self, folder_path, file_name):
        super().delete(folder_path, file_name)
        pass
    