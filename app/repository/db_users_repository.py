#-*- UTF-8 -*-

from app.infrastructure.config_ini_file import DbServerConfigIniFile
from app.infrastructure.user_db import DbUsers

'''
Repository Module
'''
class DbUsersRepository():
    __db = None
    
    def __init__(self):
        db_config = DbServerConfigIniFile()
        self.__db = DbUsers(db_config.get_config())
        pass

    def exists(self, username, password):
        if(self.__db.count(username, password) > 0):
            return True
        else:
            return False