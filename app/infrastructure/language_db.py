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

    def insert(self, user_id, language_name):
        sql = 'INSERT INTO m_user_id, m_language_name VALUES(%s, %s);'
        bindings = (user_id, language_name)
        return super().insert(sql, bindings)
    
    def update(self, language_id, user_id, language_name):
        sql = 'UPDATE m_languages SET m_user_id = %s, m_language_name = %s WHERE m_language_id = %s AND user_id = %s;'
        bindings = (user_id, language_name, language_id, user_id)
        return super().update(sql, bindings)
    
    def delete(self, language_id, user_id):
        sql = 'DELETE FROM m_languages WHERE m_language_id = %s AND user_id = %s;'
        bindings = (language_id, user_id)
        return super().delete(sql, bindings)
