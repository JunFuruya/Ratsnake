#-*- UTF-8 -*-

import app.entity
from app.infrastructure import config_ini_file
from app.infrastructure import user_db

'''
Repository Module
'''
class DbUsersRepository():
    __db = None

    def __init__(self):
        db_config = config_ini_file.DbServerConfigIniFile()
        self.__db = app.infrastructure.user_db.DbUsers(db_config.get_config)
        pass
    
    def exists(self, username, password):
        if(self.__db.count(username, password) > 0):
            return True
        else:
            return False