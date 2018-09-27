#-*- UTF-8 -*-

from app.infrastructure.language_db import DbLanguages
from app.entity.base_web_entity import BaseWebEntity
from app.entity.language_entity import LanguageEntity
from app.entity.language_list_entity import LanguageListEntity

'''
Repository Module
'''
class LanguageRepository():
    __db = None
    
    def __init__(self):
        self.__db = DbLanguages()
        pass

    def find(self, params):
        return self.__db.selectOne()

    def findList(self, limit, offset):
        records = self.__db.select(limit, offset)
        list_entity = LanguageListEntity()
        
        entities = []
        for record in records:
            entity = LanguageEntity()
            entity.set_language_id(record[0])
            entity.set_language_name(record[1])
            entities.append(entity)
            
        list_entity.set_language_entity_list(entities)
        
        return list_entity

    def insert(self, user_id, language_name):
        entity = LanguageEntity()
        return entity.set_language_id(self.__db.insert(user_id, language_name))

    def update(self, params):
        return self.__db.update()

    def delete(self, params):
        return self.__db.delete()
