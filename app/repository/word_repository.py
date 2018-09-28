#-*- UTF-8 -*-

from app.infrastructure.word_db import Dbwords
from app.entity.word_entity import WordEntity
from app.entity.word_list_entity import WordListEntity

'''
Word Repository Module
'''
class WordRepository():
    __db = None
    
    def __init__(self):
        self.__db = Dbwords()
        pass

    def find(self, user_id, word_id):
        record = self.__db.selectOne(user_id, word_id)

        entity = WordEntity()
        if record is not None:
            entity.set_word_id(record[0])
            entity.set_word_name(record[1])
            
        return entity

    def findList(self, limit, offset):
        records = self.__db.select(limit, offset)
        list_entity = wordListEntity()
        
        entities = []
        for record in records:
            entity = WordEntity()
            entity.set_word_id(record[0])
            entity.set_word_name(record[1])
            entities.append(entity)
            
        list_entity.set_word_entity_list(entities)
        
        return list_entity

    def insert(self, user_id, word_name):
        entity = WordEntity()
        return entity.set_word_id(self.__db.insert(user_id, word_name))

    def update(self, word_id, user_id, word_name):
        is_success = self.__db.update(word_id, user_id, word_name)
        if is_success == True:
            return word_id
        else:
            return ''

    def delete(self, word_id, user_id):
        is_success = self.__db.delete(word_id, user_id)
        if is_success == True:
            return word_id
        else:
            return ''