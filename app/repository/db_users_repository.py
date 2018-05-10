#-*- UTF-8 -*-

import app.entity
import app.infrastructure.user_db

'''
Repository Module
'''
class DbUsersRepository():
    __db = None

    def __init__(self):
        self.__db = app.infrastructure.user_db.DbUsers()
        pass
    
    def exists(self, username, password):
        if(self.__db.count(username, password) > 0):
            return True
        else:
            return False