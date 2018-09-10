# -*- coding: utf-8 -*-

from app.infrastructure.base_db import DbBase

'''
langauage database module
'''
class DbLanguages(DbBase):
    def __init__(self):
        super().__init__()
        pass
    
    def select(self, limit, offset):
        sql = 'SELECT m_language_id, m_language_name FROM m_languages limit %s offset %s'
        bindings = (limit, offset)
        return super().select(sql, bindings)

    def selectOne(self, language_id):
        sql = 'SELECT m_language_id, m_language_name FROM m_languages WHERE m_language_id = %s;'
        bindings = (language_id)
        return super().selectOne(sql, bindings)

    def insert(self, language_id, user_id, m_language_name):
        sql = 'INSERT INTO m_language_id, m_user_id, m_language_name VALUES(%s);'
        bindings = (language_id, )
        return super().selectOne(sql, bindings)
    
    def update(self, language_id, user_id, language_name):
        sql = 'UPDATE m_languages SET m_user_id = %s, m_language_name = %s WHERE m_language_id = %s AND user_id = %s;'
        bindings = (user_id, language_name, language_id, user_id)
        return super().selectOne(sql, bindings)
    
    def delete(self, language_id, user_id):
        sql = 'DELETE FROM m_languages WHERE m_language_id = %s AND user_id = %s;'
        bindings = (language_id, user_id)
        return super().selectOne(sql, bindings)
