# -*- coding: UTF-8 -*-

import subprocess

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
        #db_config = g.get_config(DB_CONFIG_FILE_NAME)
        #command = 'mysqldump -u' + db_config['dump']['user'] + ' -p ' + db_config['dump']['database'] \
        #          + ' > ' + os.path.join(folder_path, file_name)
        # サンプル mysqldump -uroot -p hideout > /var/dbdump/hideout_201905022.dump
        subprocess.call(command)
        pass
    
    def delete(self, folder_path, file_name):
        pass
    