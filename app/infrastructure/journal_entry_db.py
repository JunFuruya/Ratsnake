# -*- coding: UTF-8 -*-

from app.infrastructure.base_db import DbBase

'''
journal entry database module
'''
class DbJournalEntries(DbBase):
    def __init__(self):
        super().__init__()
        pass
    
    def selectAll(self, user_id):
        sql = 'SELECT t_journal_entry_id, m_account_title_id, t_journal_entry_transaction_date, t_journal_entry_note, t_journal_entry_created_at FROM t_journal_entries WHERE m_user_id = %s;'
        bindings = (user_id,)
        return super().select(sql, bindings)
    
    def selectList(self, user_id, limit, offset):
        sql = 'SELECT t_journal_entry_id, m_account_title_id, t_journal_entry_transaction_date, t_journal_entry_note, t_journal_entry_created_at FROM t_journal_entries WHERE m_user_id = %s limit %s offset %s;'
        bindings = (user_id, limit, offset)
        return super().select(sql, bindings)

    def selectOne(self, user_id, account_title_id, journal_entry_transaction_date, journal_entry_note):
        sql = 'SELECT t_journal_entry_id, m_account_title_id, t_journal_entry_transaction_date, t_journal_entry_note FROM t_journal_entries WHERE m_user_id = %s AND t_journal_entry_id = %s;'
        bindings = (user_id, language_id)
        return super().selectOne(sql, bindings)

    def insert(self, user_id, account_title_id, journal_entry_transaction_date, journal_entry_note):
        sql = 'INSERT INTO t_journal_entries(m_user_id, m_account_title_id, t_journal_entry_transaction_date, t_journal_entry_note) VALUES(%s, %s, %s, %s);'
        bindings = (user_id, account_title_id, journal_entry_transaction_date, journal_entry_note)
        
        # TODO 全体的に例外処理を入れる
        try:
            id = super().insert(sql, bindings)
            super().commit()
        except:
            super().rollback()
        
        super().close_connetion()
        
        return id
    
    def update(self, journal_entry_id, user_id, account_title_id, journal_entry_transaction_date, journal_entry_note):
        sql = 'UPDATE t_journal_entries SET account_title_id = %s AND journal_entry_transaction_date = %s AND journal_entry_note = %s WHERE t_journal_entry_id = %s AND m_user_id = %s;'
        bindings = (language_name, account_title_id, journal_entry_transaction_date, journal_entry_note, journal_entry_id, user_id)

        is_success = False
        # TODO 全体的に例外処理を入れる
        try:
            is_success = super().update(sql, bindings)
            super().commit()
        except:
            super().rollback()
        return is_success
    
    def delete(self, journal_entry_id, user_id):
        sql = 'DELETE FROM t_journal_entries WHERE t_journal_entry_id = %s AND m_user_id = %s;'
        bindings = (journal_entry_id, user_id)

        is_success = False
        # TODO 全体的に例外処理を入れる
        try:
            is_success = super().delete(sql, bindings)
            super().commit()
        except:
            super().rollback()
        
        super().close_connetion()

        return is_success
