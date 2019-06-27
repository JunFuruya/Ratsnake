# -*- coding: UTF-8 -*-

import os

class BaseFile():
    def __init__(self):
        pass

    def get_file_names(self, folder_path):
        return os.listdir(folder_path)
    
    def create(self, folder_path, file_name):
        pass
    
    def delete(self, folder_path, file_name):
        os.remove(os.path.join(folder_path, file_name))
        pass
    
    def copy(self, folder_path_from, folder_path_to, file_name):
        pass
    
    def move(self, folder_path_from, folder_path_to, file_name):
        pass
    
    def rename(self, folder_path_from, file_name_from, file_name_to):
        pass
    