#-*- UTF-8 -*-

from app.infrastructure.language_db import DbLanguages
from app.entity.base_web_entity import BaseWebEntity
from app.entity.admin.language_entity import LanguageEntity

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
        page_entity = BaseWebEntity()
        
        entities = []
        for record in records:
            entity = LanguageEntity()
            entity.set_language_id(records['m_language_id'])
            entity.set_language_name(records['m_language_name'])
            entities.append(entity)
            
        page_entity.set_records(entities)
        
        return page_entity

    def insert(self, user_id, language_name):
        entity = LanguageEntity()
        return entity.set_language_id(self.__db.insert(user_id, language_name))

    def update(self, params):
        return self.__db.update()

    def delete(self, params):
        return self.__db.delete()
