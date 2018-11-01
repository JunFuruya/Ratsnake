# -*- coding: utf-8 -*-

from app.entity.base_web_entity import BaseWebEntity

class LinkEntity(BaseWebEntity):
    __user_id = ''
    __language_id = ''
    __language_name = ''
    __word_id = ''
    __word_spell = ''
    __word_explanation = ''
    __word_pronounciation = ''
    __word_is_learned = ''
    __word_note = ''
    __word_created_at = ''
    
    def set_error_message(self, error_message):
        self.__error_message = error_message
        return self

    def get_error_message(self):
        return self.__error_message  
    
    def set_user_id(self, user_id):
        self.user_id = user_id
        return self
    
    def get_user_id(self):
        return self.__user_id
    
    def set_language_id(self, language_id):
        self.__language_id = language_id
        return self

    def get_language_id(self):
        return self.__language_id
    
    def set_language_name(self, language_name):
        self.__language_name = language_name
        return self

    def get_language_name(self):
        return self.__language_name
    
    def set_word_id(self, word_id):
        self.__word_id = word_id
        return self
    
    def get_word_id(self):
        return self.__word_id
    
    def set_word_spell(self, word_spell):
        self.__word_spell = word_spell
        return self

    def get_word_spell(self):
        return self.__word_spell

    def set_word_explanation(self, word_explanation):
        self.__word_explanation = word_explanation
        return self

    def get_word_explanation(self):
        return self.__word_explanation

    def set_word_pronounciation(self, word_pronounciation):
        self.__word_pronounciation = word_pronounciation
        return self

    def get_word_pronounciation(self):
        return self.__word_pronounciation

    def set_word_is_learned(self, word_is_learned):
        self.__word_is_learned = word_is_learned
        return self

    def get_word_is_learned(self):
        return self.__word_is_learned

    def set_word_note(self, word_note):
        self.__word_note = word_note
        return self

    def get_word_note(self):
        return self.__word_note

    def set_word_note(self, word_note):
        self.__word_created_at = word_note
        return self

    def get_word_note(self):
        return self.__word_created_at

    # TODO to array