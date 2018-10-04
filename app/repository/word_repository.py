#-*- UTF-8 -*-

from app.infrastructure.language_db import DbLanguages
from app.infrastructure.word_db import DbWords
from app.entity.language_entity import LanguageEntity
from app.entity.word_entity import WordEntity
from app.entity.word_list_entity import WordListEntity

'''
Word Repository Module
'''
class WordRepository():
    __word_db = None
    __language_db = None
    
    def __init__(self):
        self.__word_db = DbWords()
        self.__language_db = DbLanguages()
        pass

    def find(self, user_id, word_id):
        record = self.__word_db.selectOne(user_id, word_id)

        entity = WordEntity()
        if record is not None:
            entity.set_word_id(record[0])
            entity.set_word_name(record[1])
            
        return entity

    def findList(self, user_id, language_id, limit, offset):
        list_entity = WordListEntity()
        
        language_records = self.__language_db.selectAll(user_id) 
        entities = []
        for language_record in language_records:
            entity = LanguageEntity()
            entity.set_language_id(language_record[0])
            entity.set_language_name(language_record[1])
            entities.append(entity)
            
        list_entity.set_language_entity_list(entities)
        
        word_records = self.__word_db.select(user_id, language_id, limit, offset)
        entities = []
        for word_record in word_records:
            entity = WordEntity()
            entity.set_word_id(word_record[0])
            entity.set_word_spell(word_record[1])
            entity.set_word_explanation(word_record[2])
            entity.set_word_pronounciation(word_record[3])
            entity.set_word_is_learned(word_record[4])
            entity.set_word_note(word_record[5])
            entities.append(entity)
            
        list_entity.set_word_entity_list(entities)
        
        return list_entity

    def insert(self, user_id, language_id, word_spell, word_explanation, word_pronanciation, word_is_learned, word_note):
        entity = WordEntity()
        return entity.set_word_id(self.__word_db.insert(user_id, language_id, word_spell, word_explanation, word_pronanciation, word_is_learned, word_note))

    def update(self, word_id, user_id, word_name):
        is_success = self.__word_db.update(word_id, user_id, word_name)
        if is_success == True:
            return word_id
        else:
            return ''

    def delete(self, word_id, user_id):
        is_success = self.__word_db.delete(word_id, user_id)
        if is_success == True:
            return word_id
        else:
            return ''