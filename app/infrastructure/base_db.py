# -*- coding: UTF-8 -*-

import mysql.connector
from app.infrastructure.config_ini_file import DbServerConfigIniFile

# TODO デバッグ方法調べる
#import pdb; pdb.set_trace()

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

    def select(self, sql, bindings):
        cursor = self.__connection.cursor()
        cursor.execute(sql, bindings)
        rows = cursor.fetchall()
        cursor.close()
        self.__connection.close()
        return rows

    def selectOne(self, sql, bindings):
        cursor = self.__connection.cursor()
        cursor.execute(sql, bindings)
        row = cursor.fetchone()
        cursor.close()

        return row

    def insert(self, sql, bindings):
        cursor = self.__connection.cursor()
        id = cursor.execute(sql, bindings)
        cursor.close()
        return id

    def update(self, sql, bindings):
        cursor = self.__connection.cursor()
        success_flg = cursor.execute(sql, bindings)
        cursor.close()
        return success_flg

    def delete(self, sql, bindings):
        cursor = self.__connection.cursor()
        success_flg = cursor.execute(sql, bindings)
        cursor.close()
        return success_flg
    
    def commit(self):
        self.__connection.commit()
        pass
        
    def rollback(self):
        self.__connection.rollback()
        pass
    
    def close_connetion(self):
        self.__connection.close()
        pass
