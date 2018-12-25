# -*- coding: UTF-8 -*-

from app.validator.base_validator import BaseValidator

class WordValidator(BaseValidator):
    def __init__(self):
        pass
        
    def get_error_messages(self, word_spell, word_explanation, word_pronunciation, word_is_learned, word_note):
        self.__word_spell = word_spell
        self.__word_explanation = word_explanation
        self.__word_pronunciation = word_pronunciation
        self.__word_is_learned = word_is_learned
        self.__word_note = word_note

        self.__validate()

        return super().get_error_messages()

    def __validate(self):
        if(self.has_empty_error(self.__word_spell)):
            super().error_messages.append('綴りが入力されていません。')
        if(self.has_too_large_number_error(self.__word_spell, 50)):
            super().error_messages.append('綴りは50文字以内で入力してください。')
        if(self.has_empty_error(self.__word_explanation)):
            super().error_messages.append('説明が入力されていません。')
        if(self.has_too_large_number_error(self.__word_explanation, 1000)):
            super().error_messages.append('説明は1000文字以内で入力してください。')
        if(self.has_too_large_number_error(self.__word_pronunciation, 50)):
            super().error_messages.append('発音は50文字以内で入力してください。')
        if(self.has_too_large_number_error(self.__word_note, 1000)):
            super().error_messages.append('備考は1000文字以内で入力してください。')
        pass
    