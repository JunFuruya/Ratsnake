# -*- coding: UTF-8 -*-

import logging
import os
from app.infrastructure.base_file import BaseFile


class LogFile(BaseFile):
    file_handler = None

    def __init__(self, folder_path, file_name):
        super().__init__()
        if not os.path.exists(folder_path):
            os.mkdir(folder_path, 0o777)

        self.file_handler = open(file_name, 'w')
        self.__file_handler = logging.FileHandler('./logs/hideout.log')
        self.__file_handler.setFormatter(logging.Formatter("%(asctime)s %(levelname)8s %(message)s"))

    def write(self):
        self.file_handler.write('')

    def get_file_handler(self):
        return self.file_handler

    def close(self):
        self.file_handler.close()
        pass