# -*- coding: UTF-8 -*-

import os

class BaseFile():
    def __init__(self):
        pass

    def get_file_names(self, folder_path):
        return os.listdir(folder_path)