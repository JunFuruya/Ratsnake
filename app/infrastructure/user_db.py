# -*- coding: utf-8 -*-

import mysql.connector
import pprint

'''
database module
'''
class DbBase():
    _db = ''
    _host = ''
    _port = ''
    _user = ''
    _password = ''
    _configparser = None
    
    
    def __init__(self, config):
        pprint.pprint(vars(config))
        self._db = config['MySQL']['Name']
        self._host = config['MySQL']['Host']
        self._port = config['MySQL']['Port']
        self._user = config['MySQL']['User']
        self._password = config['MySQL']['Password']
        pass

class DbUsers(DbBase):
    def __init__(self, config):
        super().__init__(config)
        pass
    
    def count(self, username, password):
        sql = 'SELECT COUNT(m_user_id) FROM m_users where m_user_username = %s and m_user_hashed_password = SHA2(%s, 256)'

        #TODO: make the parent class
        connection = mysql.connector.connect(db=self._db, host=self._host, port=self._port, user=self._user, password=self._password)
        cursor = connection.cursor()
        cursor.execute(sql, (username, password))
        row = cursor.fetchone()
        cursor.close()
        connection.close()
        #fetchall()
        return row[0]