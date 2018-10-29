# -*- coding: utf-8 -*-

from app.infrastructure.base_db import DbBase

'''
word database module
'''
class DbWords(DbBase):
    def __init__(self):
        super().__init__()
        pass
    
    def select(self, user_id, language_id, limit, offset):
        sql = 'SELECT t_word_id, t_word_spell FROM t_words WHERE m_user_id = %s AND m_language_id = %s LIMIT %s OFFSET %s'
        bindings = (user_id, language_id, limit, offset)
        return super().select(sql, bindings)

    def selectOne(self, user_id, language_id, word_id):
        sql = 'SELECT t_word_id, t_word_spell, t_word_explanation, t_word_pronounciation, t_word_is_learned, t_word_note FROM t_words WHERE m_user_id = %s AND m_language_id = %s AND t_word_id = %s;'
        bindings = (user_id, language_id, word_id)
        return super().selectOne(sql, bindings)

    def insert(self, user_id, language_id, word_spell, word_explanation, word_pronounciation, word_is_learned, word_note):
        sql = 'INSERT INTO t_words(m_user_id, m_language_id, t_word_spell, t_word_explanation, t_word_pronounciation, t_word_is_learned, t_word_note) VALUES(%s, %s, %s, %s, %s, %s, %s);'
        bindings = (user_id, language_id, word_spell, word_explanation, word_pronounciation, word_is_learned, word_note)
        
        # TODO 全体的に例外処理を入れる
        id = None
        try:
            id = super().insert(sql, bindings)
            super().commit()
        except:
            super().rollback()
        
        super().close_connetion()
        
        return id
    
    def update(self, user_id, language_id, word_id, word_spell, word_explanation, word_pronounciation, word_is_learned, word_note):
        sql = 'UPDATE t_words SET t_word_spell = %s, t_word_explanation = %s, t_word_pronounciation = %s, t_word_is_learned = %s, t_word_note = %s WHERE m_user_id = %s AND m_language_id = %s AND t_word_id = %s;'
        bindings = (word_spell, word_explanation, word_pronounciation, word_is_learned, word_note, user_id, language_id, word_id)

        is_success = False
        # TODO 全体的に例外処理を入れる
        try:
            is_success = super().update(sql, bindings)
            super().commit()
        except:
            super().rollback()
        return is_success
    
    def delete(self, user_id, language_id, word_id):
        sql = 'DELETE FROM t_words WHERE m_user_id = %s AND m_language_id = %s AND t_word_id = %s;'
        bindings = (user_id, language_id, word_id)

        is_success = False
        # TODO 全体的に例外処理を入れる
        try:
            is_success = super().delete(sql, bindings)
            super().commit()
        except:
            super().rollback()
        
        super().close_connetion()

        return is_success
