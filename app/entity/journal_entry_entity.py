# -*- coding: UTF-8 -*-

from app.entity.base_web_entity import BaseWebEntity

class JournalEntryEntity(BaseWebEntity):
    __journal_entry_id = ''
    __user_id = ''
    __account_title_id = ''
    __journal_entry_transaction_date = ''
    __journal_entry_note = ''
    
    def set_error_message(self, error_message):
        self.__error_message = error_message
        return self

    def get_error_message(self):
        return self.__error_message  
    
    def set_journal_entry_id(self, journal_entry_id):
        self.__journal_entry_id = journal_entry_id
        return self
    
    def get_journal_entry_id(self):
        return self.__journal_entry_id
    
    def set_user_id(self, user_id):
        self.user_id = user_id
        return self
    
    def get_user_id(self):
        return self.__user_id
    
    def set_account_title_id(self, account_title_id):
        self.__account_title_id = account_title_id
        return self
    
    def get_account_title_id(self):
        return self.__account_title_id
    
    def set_journal_entry_transaction_date(self, journal_entry_transaction_date):
        self.__journal_entry_transaction_date = journal_entry_transaction_date
        return self
    
    def get_journal_entry_transaction_date(self):
        return self.__journal_entry_transaction_date
    
    def set_journal_entry_note(self, journal_entry_note):
        self.__journal_entry_note = journal_entry_note
        return self
    
    def get_journal_entry_note(self):
        return self.__journal_entry_note
    
        # TODO to array