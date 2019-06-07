# -*- coding: UTF-8 -*-

from app.validator.base_validator import BaseValidator

class JournalEntryValidator(BaseValidator):
    def __init__(self):
        pass
        
    def get_error_messages(self, account_title_id, journal_entry_transaction_date, journal_entry_note):
        self.__account_title_id = account_title_id
        self.__journal_entry_transaction_date = journal_entry_transaction_date
        self.__journal_entry_note = journal_entry_note

        self.__validate()

        return super().get_error_messages()

    def __validate(self):
        error_messages = []
        if(self.has_too_large_number_error(self.__journal_entry_note, 1000)):
            error_messages.append('備考は1000文字以内で入力してください。')
            
        super().set_error_messages(error_messages)
        pass
    