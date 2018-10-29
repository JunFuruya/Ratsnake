# -*- coding: utf-8 -*-

from app.infrastructure.base_db import DbBase

'''
user database module
'''
class DbUsers(DbBase):
    def __init__(self):
        super().__init__()
        pass
    
    def count(self, username, password):
        sql = 'SELECT COUNT(m_user_id) FROM m_users where m_user_username = %s and m_user_hashed_password = SHA2(%s, 256)'
        bindings = (username, password)
        return super().count(sql, bindings)
