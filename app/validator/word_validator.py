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
        error_messages = []
        if(self.has_empty_error(self.__word_spell)):
            error_messages.append('綴りが入力されていません。')
        if(self.has_too_large_number_error(self.__word_spell, 50)):
            error_messages.append('綴りは50文字以内で入力してください。')
        if(self.has_empty_error(self.__word_explanation)):
            error_messages.append('説明が入力されていません。')
        if(self.has_too_large_number_error(self.__word_explanation, 1000)):
            error_messages.append('説明は1000文字以内で入力してください。')
        if(self.has_too_large_number_error(self.__word_pronunciation, 50)):
            error_messages.append('発音は50文字以内で入力してください。')
        if(self.has_too_large_number_error(self.__word_note, 1000)):
            error_messages.append('備考は1000文字以内で入力してください。')
            
        super().set_error_messages(error_messages)
        pass

    def get_csv_error_messages(self, file_path):
        error_messages = []
        if (self.__has_inappropriate_file_extention_error(file_path, 'csv')):
            error_messages.append('拡張子がCSVのファイルを指定してください。')
        if not file_exists(file_path):
            error_messages.append('指定したファイルが存在しません。')
        
        if (len(super().get_error_messages()) > 0):
            csv_lines = open(file_path, 'r')
            for csv_line in csv_lines:
                if(self.has_empty_error(csv_line[1])):
                    error_messages.append('綴りが入力されていません。')
                if(self.has_too_large_number_error(csv_line[1], 50)):
                    error_messages.append('綴りは50文字以内で入力してください。')
                if(self.has_empty_error(csv_line[2])):
                    error_messages.append('説明が入力されていません。')
                if(self.has_too_large_number_error(csv_line[2], 1000)):
                    error_messages.append('説明は1000文字以内で入力してください。')
                if(self.has_too_large_number_error(csv_line[3], 50)):
                    error_messages.append('発音は50文字以内で入力してください。')
                if(self.has_too_large_number_error(csv_line[4], 1000)):
                    error_messages.append('備考は1000文字以内で入力してください。')
            csv_lines.close()

        super().set_error_messages(error_messages)

        return super().get_error_messages()

