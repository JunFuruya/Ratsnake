# -*- coding: UTF-8 -*-

from app.service.base_service import BaseService
from app.repository.journal_entry_repository import JournalEntryRepository

class JournalEntryService(BaseService):
    def __init__(self):
        self.__reposiroty = JournalEntryRepository()
        pass

    def getList(self, user_id, limit, oiffset):
        return self.__reposiroty.findList(user_id, limit, oiffset)

    def get(self, user_id, journal_entry_id):
        return self.__reposiroty.find(user_id, journal_entry_id)

    def create(self, user_id, account_title_id, journal_entry_transaction_date, journal_entry_note):
        return self.__reposiroty.insert(user_id, account_title_id, journal_entry_transaction_date, journal_entry_note)

    def update(self, journal_entry_id, user_id, account_title_id, journal_entry_transaction_date, journal_entry_note):
        return self.__reposiroty.update(journal_entry_id, user_id, account_title_id, journal_entry_transaction_date, journal_entry_note)

    def delete(self, journal_entry_id, user_id):
        return self.__reposiroty.delete(journal_entry_id, user_id)
