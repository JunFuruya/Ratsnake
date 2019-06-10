# -*- coding: UTF-8 -*-

from app.infrastructure.journal_entry_db import DbJournalEntries
from app.entity.journal_entry_entity import JournalEntryEntity
from app.entity.journal_entry_list_entity import JournalEntryListEntity

'''
Repository Module
'''
class JournalEntryRepository():
    __db = None
    
    def __init__(self):
        self.__db = DbJournalEntries()
        pass

    def find(self, user_id, journal_entry_id):
        record = self.__db.selectOne(user_id, journal_entry_id)

        entity = JournalEntryEntity()
        if record is not None:
            entity.set_journal_entry_id(record[0])
            entity.set_account_title_id(record[1])
            entity.set_journal_entry_transaction_date(record[2])
            entity.set_journal_entry_note(record[3])
            
        return entity

    def findList(self, user_id, limit, offset):
        records = self.__db.selectList(user_id, limit, offset)
        list_entity = JournalEntryListEntity()
        
        entities = []
        for record in records:
            entity = JournalEntryEntity()
            entity.set_journal_entry_id(record[0])
            entity.set_account_title_id(record[1])
            entity.set_journal_entry_transaction_date(record[2])
            entity.set_journal_entry_note(record[3])
            entities.append(entity)
            
        list_entity.set_journal_entry_list(entities)
        
        return list_entity

    def insert(self, user_id, account_title_id, journal_entry_transaction_date, journal_entry_note):
        entity = JournalEntryEntity()
        return entity.set_language_id(self.__db.insert(user_id, account_title_id, journal_entry_transaction_date, journal_entry_note))

    def update(self, journal_entry_id, user_id, account_title_id, journal_entry_transaction_date, journal_entry_note):
        is_success = self.__db.update(journal_entry_id, user_id, account_title_id, journal_entry_transaction_date, journal_entry_note)
        if is_success == True:
            return journal_entry_id
        else:
            return ''

    def delete(self, journal_entry_id, user_id):
        is_success = self.__db.delete(journal_entry_id, user_id)
        if is_success == True:
            return journal_entry_id
        else:
            return ''