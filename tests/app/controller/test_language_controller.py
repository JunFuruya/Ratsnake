# -*- coding: utf-8 -*-

import unittest
import main

class TestLanguageController(unittest.TestCase):
    def __init__(self):
        
        pass
    
    def test_index_レコードが0件の場合(self):
        limit = self.get_param('limit', 10)
        offset = self.get_param('offset', 0)
        #entities = self.__service.getList(self.__user_id, limit, offset))
        assert(len([]), 0)
    #def test_create(self):
    #def test_detail(self, language_id):
    #def test_edit(self, language_id):
    #def test_confirm(self):
    #def test_insert(self):
    #def test_update(self):
    #def test_delete(self):
    
if __name__ == '__main__':
    unittest.main()