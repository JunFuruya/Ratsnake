# -*- coding: utf-8 -*-

import mysql.connector
from app.infrastructure.config_ini_file import DbServerConfigIniFile

'''
database module
'''
class DbBase():
    __connection = None
    
    def __init__(self):
        self.__db_config = DbServerConfigIniFile();
        host, port, db_name, user, password = self.__db_config.get_config();
        self.__connection = mysql.connector.connect(db=db_name, host=host, port=port, user=user, password=password)

        pass

    def count(self, sql, bindings):
        cursor = self.__connection.cursor()
        cursor.execute(sql, bindings)
        row = cursor.fetchone()
        cursor.close()
        self.__connection.close()
        return row[0]

        #fetchall() TODO: implement select all
    
class DbUsers(DbBase):
    def __init__(self):
        super().__init__()
        pass
    
    def count(self, username, password):
        sql = 'SELECT COUNT(m_user_id) FROM m_users where m_user_username = %s and m_user_hashed_password = SHA2(%s, 256)'
        bindings = (username, password)
        return super().count(sql, bindings)
