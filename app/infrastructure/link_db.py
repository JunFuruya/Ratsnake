# -*- coding: UTF-8 -*-

from app.infrastructure.base_db import DbBase

'''
link database module
'''
class DbLinks(DbBase):
    def __init__(self):
        super().__init__()
        pass
    
    def selectAll(self, user_id, limit, offset):
        sql = 'SELECT m_link_id, m_link_category_id, m_link_category_name, m_link_site_name, m_link_url ' \
              'FROM m_links ' \
              'INNER JOIN m_link_categories USING(m_link_category_id) ' \
              'WHERE m_links.m_user_id = %s ' \
              'ORDER BY m_link_category_display_order, m_link_display_order, m_link_id ' \
              'LIMIT %s OFFSET %s'
        bindings = (user_id, limit, offset)
        return super().select(sql, bindings)

    def selectOne(self, user_id, link_id):
        sql = 'SELECT m_link_id, m_link_category_id, m_link_category_name, m_link_site_name, m_link_url, m_link_display_order ' \
              'FROM m_links ' \
              'INNER JOIN m_link_categories USING(m_link_category_id) ' \
              'WHERE m_links.m_user_id = %s AND m_link_id = %s;'
        bindings = (user_id, link_id)
        return super().selectOne(sql, bindings)

    def count(self, user_id):
        sql = 'SELECT COUNT(m_link_id) AS count ' \
              'FROM m_links ' \
              'WHERE m_links.m_user_id = %s;'
        bindings = (user_id,)
        return super().count(sql, bindings)

    def insert(self, user_id, link_category_id, link_site_name, link_url, link_display_order):
        sql = 'INSERT INTO m_links(m_user_id, m_link_category_id, m_link_site_name, m_link_url, m_link_display_order) VALUES (%s, %s, %s, %s, %s);'
        bindings = (user_id, link_category_id, link_site_name, link_url, link_display_order)
        
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
        sql = 'UPDATE m_links SET m_link_category_id = %s, m_link_site_name = %s, m_link_url = %s, m_link_display_order = %s WHERE m_user_id = %s AND m_link_id = %s;'
        bindings = (link_category_id, link_site_name, link_url, link_display_order, user_id, link_id)

        is_success = False
        # TODO 全体的に例外処理を入れる
        #try:
        is_success = super().update(sql, bindings)
        super().commit()
        #except:
        #    super().rollback()
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
