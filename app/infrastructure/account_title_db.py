# -*- coding: UTF-8 -*-

from app.infrastructure.base_db import DbBase

'''
account title database module
'''
class DbAccountTitles(DbBase):
    def __init__(self):
        super().__init__()
        pass

    def selectAll(self, user_id, limit, offset):
        sql = 'SELECT m_account_title_id, m_account_title_name, m_account_title_classification_type FROM m_account_titles WHERE m_user_id = %s LIMIT %s OFFSET %s;'
        bindings = (user_id, limit, offset)
        return super().select(sql, bindings)

    def selectOne(self, user_id, account_title_id):
        sql = 'SELECT m_account_title_id, m_account_title_name, m_account_title_classification_type FROM m_account_titles WHERE m_user_id = %s AND m_account_title_id = %s;'
        bindings = (user_id, account_title_id)
        return super().selectOne(sql, bindings)

    def insert(self, user_id, account_title_name, account_title_classification_type):
        sql = 'INSERT INTO m_account_titles(m_user_id, m_account_title_name, m_account_title_classification_type) VALUES(%s, %s, %s);'
        bindings = (user_id, account_title_name, account_title_classification_type)
        
        # TODO 全体的に例外処理を入れる
        #id = ''
        #try:
        id = super().insert(sql, bindings)
        super().commit()
        #except:
        #    super().rollback()
        
        super().close_connetion()
        
        return id
    
    def update(self, account_title_id, user_id, account_title_name, account_title_classification_type):
        sql = 'UPDATE m_account_titles SET m_account_title_name = %s, m_account_title_classification_type = %s WHERE m_account_title_id = %s AND m_user_id = %s;'
        bindings = (account_title_name, account_title_classification_type, account_title_id, user_id)

        is_success = False
        # TODO 全体的に例外処理を入れる
        try:
            is_success = super().update(sql, bindings)
            super().commit()
        except:
            super().rollback()
        return is_success
    
    def delete(self, account_title_id, user_id):
        sql = 'DELETE FROM m_account_titles WHERE m_account_title_id = %s AND m_user_id = %s;'
        bindings = (account_title_id, user_id)

        is_success = False
        # TODO 全体的に例外処理を入れる
        try:
            is_success = super().delete(sql, bindings)
            super().commit()
        except:
            super().rollback()
        
        super().close_connetion()

        return is_success