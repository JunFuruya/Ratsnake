# -*- coding: UTF-8 -*-

from app.infrastructure.base_file import BaseFile

'''
dbdump file module
'''
class DbDumpFile(BaseFile):
    def __init__(self):
        super().__init__()
        pass

    def get_file_names(self, folder_path):
        return super().get_file_names(folder_path)
