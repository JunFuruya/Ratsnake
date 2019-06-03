# -*- coding: utf-8 -*-

import unittest
import sys, os

dirpath = os.path.dirname(os.path.abspath(__file__))
sys.path.append(dirpath)

from app.service.dbdump_service import DbDumpService

class DbDumpServiceTest(unittest.TestCase):
    def __init__(self):
        self.__service = DbDumpService()
        pass
    
    def test_create_dump(self):
        #self.__service.create_dump()
        pass
    
    def test_get_dump_names(self):
        folder_path = ''
        self.__service.get_dump_names(folder_path)
        pass

    def test_delete_dump(self, file_name):
        #self.__service.delete_dump()
        pass
