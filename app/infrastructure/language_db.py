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

    def selectOne(self, user_id, language_id):
        sql = 'SELECT m_language_id, m_language_name FROM m_languages WHERE m_user_id = %s AND m_language_id = %s;'
        bindings = (user_id, language_id)
        return super().selectOne(sql, bindings)

    def insert(self, user_id, language_name):
        sql = 'INSERT INTO m_languages(m_user_id, m_language_name) VALUES(%s, %s);'
        bindings = (user_id, language_name)
        
        # TODO 全体的に例外処理を入れる
        try:
            id = super().insert(sql, bindings)
            super().commit()
        except:
            super().rollback()
        
        super().close_connetion()
        
        return id
    
    def update(self, language_id, user_id, language_name):
        sql = 'UPDATE m_languages SET m_language_name = %s WHERE m_language_id = %s AND m_user_id = %s;'
        bindings = (language_name, language_id, user_id)

        is_success = False
        # TODO 全体的に例外処理を入れる
        try:
            is_success = super().update(sql, bindings)
            super().commit()
        except:
            super().rollback()
        return is_success
    
    def delete(self, language_id, user_id):
        sql = 'DELETE FROM m_languages WHERE m_language_id = %s AND m_user_id = %s;'
        bindings = (language_id, user_id)

        is_success = False
        # TODO 全体的に例外処理を入れる
        try:
            is_success = super().delete(sql, bindings)
            super().commit()
        except:
            super().rollback()
        
        super().close_connetion()

        return is_success
