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
        self.__connection.close()
        return row[0]

    def insert(self, sql, bindings):
        cursor = self.__connection.cursor()
        cursor.execute(sql, bindings)
        row = cursor.fetchone()
        cursor.close()
        self.__connection.close()
        return row[0]

    def update(self, sql, bindings):
        cursor = self.__connection.cursor()
        cursor.execute(sql, bindings)
        row = cursor.fetchone()
        cursor.close()
        self.__connection.close()
        return row[0]

    def delete(self, sql, bindings):
        cursor = self.__connection.cursor()
        cursor.execute(sql, bindings)
        row = cursor.fetchone()
        cursor.close()
        self.__connection.close()
        return row[0]
