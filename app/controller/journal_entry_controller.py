# -*- coding: UTF-8 -*-

from app.controller.base_controller import BaseController
from app.validator.journal_entry_validator import JournalEntryValidator
from app.service.journal_entry_service import JournalEntryService
from app.entity.journal_entry_entity import JournalEntryEntity

from app.helper.helper import HashHelper

'''
Journal Entry Controller Controller Module
'''
class JournalEntryController(BaseController):
    def __init__(self, request):
        super().__init__(request)
        self.set_page_info('仕分元帳', '入出金明細を登録します。', '')
        self.__user_id = self.get_login_user()
        self.__service = JournalEntryService()
        self.__validator = JournalEntryValidator()
        pass

    def index(self):
        limit = self.get_param('limit', 10)
        offset = self.get_param('offset', 0)

        # session をクリアする
        self.set_session('journal_entry_id', '')
        self.set_session('account_title_id', '')
        self.set_session('journal_entry_transaction_date', '')
        self.set_session('journal_entry_note', '')
        
        return self.view('./template/admin/journal-entries/list.html', self.__service.getList(self.__user_id, limit, offset))
    
    def create(self):
        return self.view('./template/admin/journal-entries/create.html', JournalEntryEntity())

    def detail(self, journal_entry_id):
        # TODO validation
        
        self.set_session('journal_entry_id', language_id)
        
        return self.view('./template/admin/journal-entries/detail.html', self.__service.get(self.__user_id, journal_entry_id))

    def edit(self, journal_entry_id):
        language_id = self.get_session('journal_entry_id')
        # TODO validation        
        return self.view('./template/admin/journal-entries/edit.html', self.__service.get(self.__user_id, journal_entry_id))
    
    def confirm(self):
        journal_entry_id = self.get_session('journal_entry_id')
        account_title_id = self.get_session('account_title_id')
        journal_entry_transaction_date = self.get_param('journal_entry_transaction_date')
        journal_entry_note = self.get_param('journal_entry_note')

        error_messages = self.__validator.get_error_messages(account_title_id, journal_entry_transaction_date, journal_entry_note)
        if(len(error_messages) == 0):
            self.set_session('journal_entry_id', '')
            self.set_session('account_title_id', '')
            self.set_session('journal_entry_transaction_date', '')
            self.set_session('journal_entry_note', '')

            template = './template/admin/journal-entries/confirm.html'
        else:
            template = './template/admin/journal-entries/create.html'
        
        # TODO Factory Class
        entity = JournalEntryEntity()
        entity.set_journal_entry_id(journal_entry_id)
        entity.set_account_title_id(account_title_id)
        entity.set_journal_entry_transaction_date(journal_entry_transaction_date)
        entity.set_journal_entry_note(journal_entry_note)
        entity.set_error_message(error_messages)
        return self.view(template, entity)

    def insert(self):
        journal_entry_name = self.get_session('journal_entry_name')
        
        # TODO validation
        
        # session をクリアする
        self.set_session('journal_entry_id', '')
        self.set_session('account_title_id', '')
        self.set_session('journal_entry_transaction_date', '')
        self.set_session('journal_entry_note', '')

        return self.view('./template/admin/journal-entries/complete.html', self.__service.create(self.__user_id, account_title_id, journal_entry_transaction_date, journal_entry_note))

    def update(self):
        journal_entry_id = self.get_session('journal_entry_id')
        account_title_id = self.get_session('account_title_id')
        journal_entry_transaction_date = self.get_session('journal_entry_transaction_date')
        journal_entry_note = self.get_session('journal_entry_note')
        
        # session をクリアする
        self.set_session('journal_entry_id', '')
        self.set_session('account_title_id', '')
        self.set_session('journal_entry_transaction_date', '')
        self.set_session('journal_entry_note', '')

        entity = JournalEntryEntity()
        entity.set_language_id(self.__service.update(journal_entry_id, self.__user_id, account_title_id, journal_entry_transaction_date, journal_entry_note))
        return self.view('./template/admin/journal-entries/complete.html', entity)
    
    def delete(self):
        journal_entry_id = self.get_param('journal_entry_id')

        # session をクリアする
        self.set_session('journal_entry_id', '')
        self.set_session('account_title_id', '')
        self.set_session('journal_entry_transaction_date', '')
        self.set_session('journal_entry_note', '')

        entity = JournalEntryEntity()
        entity.set_journal_entry_id(self.__service.delete(journal_entry_id, self.__user_id))
        return self.view('./template/admin/journal-entries/complete.html', entity)