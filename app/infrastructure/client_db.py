# -*- coding: UTF-8 -*-

from app.infrastructure.base_db import DbBase

'''
client database module
'''
class DbClients(DbBase):
    def __init__(self):
        super().__init__()
        pass
    
    def selectByLoginInfo(self, username, password):
        sql = 'SELECT m_user_id FROM m_users where m_user_username = %s and m_user_hashed_password = SHA2(%s, 256)'
        bindings = (username, password)
        return super().selectOne(sql, bindings)

    def selectAll(self, limit, offset):
        sql = 'SELECT m_user_id, m_user_username, m_user_hashed_password FROM m_users LIMIT %s OFFSET %s;'
        bindings = (limit, offset)
        return super().select(sql, bindings)

    def selectOne(self, user_id):
        sql = 'SELECT m_user_id, m_user_username, m_user_hashed_password FROM m_users WHERE m_user_id = %s;'
        bindings = (user_id,)
        return super().selectOne(sql, bindings)

    def insert(self, user_username, user_hashed_password):
        sql = 'INSERT INTO m_users(m_user_username, m_user_hashed_password) VALUES(%s, SHA2(%s, 256));'
        bindings = (user_username, user_hashed_password)
        
        # TODO 全体的に例外処理を入れる
        id = ''
        try:
            id = super().insert(sql, bindings)
            super().commit()
        except:
            super().rollback()
        
        super().close_connetion()
        
        return id
    
    def update(self, user_id, user_username, user_hashed_password):
        sql = 'UPDATE m_users SET m_user_username = %s, m_user_hashed_password = SHA2(%s, 256) WHERE m_user_id = %s;'
        bindings = (user_username, user_hashed_password, user_id)

        is_success = False
        # TODO 全体的に例外処理を入れる
        try:
            is_success = super().update(sql, bindings)
            super().commit()
        except:
            super().rollback()
        return is_success
    
    def delete(self, user_id):
        sql = 'DELETE FROM m_users WHERE m_user_id = %s;'
        bindings = (user_id,)

        is_success = False
        # TODO 全体的に例外処理を入れる
        try:
            is_success = super().delete(sql, bindings)
            super().commit()
        except:
            super().rollback()
        
        super().close_connetion()

        return is_success
