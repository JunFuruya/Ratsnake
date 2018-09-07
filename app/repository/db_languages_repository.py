#-*- UTF-8 -*-

from app.infrastructure.user_db import DbUsers

'''
Repository Module
'''
class DbUsersRepository():
    __db = None
    
    def __init__(self):
        self.__db = DbUsers()
        pass

    def selectOne(self, params):
        pass

    def selectAll(self, params):
        pass

    def insert(self, params):
        pass

    def update(self, params):
        pass

    def delete(self, params):
        pass
