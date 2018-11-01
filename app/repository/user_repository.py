#-*- UTF-8 -*-

from app.infrastructure.user_db import DbUsers

'''
User Repository Module
'''
class UsersRepository():
    __db = None
    
    def __init__(self):
        self.__db = DbUsers()
        pass

    def exists(self, username, password):
        if(self.__db.count(username, password) > 0):
            return True
        else:
            return False
