# -*- coding: UTF-8 -*-

from app.entity.base_web_entity import BaseWebEntity

class JournalEntryListEntity(BaseWebEntity):
    __journal_entry_entity_list = []
    
    def set_journal_entry_entity_list(self, journal_entry_entity_list):
        self.__journal_entry_entity_list = journal_entry_entity_list
        return self

    def get_journal_entry_entity_list(self):
        return self.__journal_entry_entity_list  
    
