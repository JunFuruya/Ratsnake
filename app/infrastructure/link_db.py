# -*- coding: utf-8 -*-

from app.infrastructure.base_db import DbBase

'''
link database module
'''
class DbLinks(DbBase):
    def __init__(self):
        super().__init__()
        pass
    
    def select(self, user_id, limit, offset):
        sql = 'SELECT m_link_id, m_link_category_id, m_link_site_name, m_link_url FROM m_links WHERE m_user_id = %s ORDER BY m_link_display_order LIMIT %s OFFSET %s'
        bindings = (user_id, limit, offset)
        return super().select(sql, bindings)

    def selectOne(self, user_id, link_id):
        sql = 'SELECT m_link_id, m_link_category_id, m_link_site_name, m_link_url, m_link_display_order FROM m_links WHERE m_user_id = %s AND link_id = %s;'
        bindings = (user_id, link_id)
        return super().selectOne(sql, bindings)

    def insert(self, user_id, link_id, link_category_id, link_site_name, link_url, link_display_order):
        sql = 'INSERT INTO t_links(m_user_id, m_link_id, m_link_category_id, m_link_site_name, m_link_url, m_link_display_order) VALUES(%s, %s, %s, %s, %s, %s);'
        bindings = (user_id, link_id, link_category_id, link_site_name, link_url, link_display_order)
        
        # TODO 全体的に例外処理を入れる
        id = None
        try:
            id = super().insert(sql, bindings)
            super().commit()
        except:
            super().rollback()
        
        super().close_connetion()
        
        return id
    
    def update(self, user_id, link_id, link_category_id, link_site_name, link_url, link_display_order):
        sql = 'UPDATE t_words SET t_word_spell = %s, t_word_explanation = %s, t_word_pronounciation = %s, t_word_is_learned = %s, t_word_note = %s WHERE m_user_id = %s AND m_language_id = %s AND t_word_id = %s;'
        bindings = (user_id, link_id, link_category_id, link_site_name, link_url, link_display_order)

        is_success = False
        # TODO 全体的に例外処理を入れる
        try:
            is_success = super().update(sql, bindings)
            super().commit()
        except:
            super().rollback()
        return is_success
    
    def delete(self, user_id, link_id):
        sql = 'DELETE FROM m_links WHERE m_user_id = %s AND m_link_id = %s;'
        bindings = (user_id, link_id)

        is_success = False
        # TODO 全体的に例外処理を入れる
        try:
            is_success = super().delete(sql, bindings)
            super().commit()
        except:
            super().rollback()
        
        super().close_connetion()

        return is_success
