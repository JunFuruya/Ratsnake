# -*- coding: utf-8 -*-

from app.infrastructure.base_db import DbBase

'''
langauage database module
'''
class DbLinkCategories(DbBase):
    def __init__(self):
        super().__init__()
        pass

    def selectAll(self, user_id, limit, offset):
        sql = 'SELECT m_link_category_id, m_link_category_name FROM m_link_categories WHERE m_user_id = %s ORDER BY m_link_category_display_order LIMIT %s OFFSET %s;'
        bindings = (user_id, limit, offset)
        return super().select(sql, bindings)

    def selectOne(self, user_id, link_category_id):
        sql = 'SELECT m_link_category_id, m_user_id, m_link_category_name, m_link_category_display_order FROM m_link_categories WHERE m_user_id = %s AND m_link_category_id = %s;'
        bindings = (user_id, link_category_id)
        return super().selectOne(sql, bindings)

    def insert(self, user_id, link_category_name, link_category_display_order):
        sql = 'INSERT INTO m_link_categories(m_user_id, m_link_category_name, m_link_category_display_order) VALUES(%s, %s, %s);'
        bindings = (user_id, link_category_name, link_category_display_order)
        
        # TODO 全体的に例外処理を入れる
        #id = ''
        #try:
        id = super().insert(sql, bindings)
        super().commit()
        #except:
        #    super().rollback()
        
        super().close_connetion()
        
        return id
    
    def update(self, link_category_id, user_id, link_category_name, link_category_display_order):
        sql = 'UPDATE m_link_categories SET m_link_category_name = %s, m_link_category_display_order = %s WHERE m_link_category_id = %s AND m_user_id = %s;'
        bindings = (link_category_name, link_category_display_order, link_category_id, user_id)

        is_success = False
        # TODO 全体的に例外処理を入れる
        try:
            is_success = super().update(sql, bindings)
            super().commit()
        except:
            super().rollback()
        return is_success
    
    def delete(self, link_category_id, user_id):
        sql = 'DELETE FROM m_link_categories WHERE m_link_category_id = %s AND m_user_id = %s;'
        bindings = (link_category_id, user_id)

        is_success = False
        # TODO 全体的に例外処理を入れる
        try:
            is_success = super().delete(sql, bindings)
            super().commit()
        except:
            super().rollback()
        
        super().close_connetion()

        return is_success