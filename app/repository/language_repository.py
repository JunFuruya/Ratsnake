#-*- UTF-8 -*-

from app.infrastructure.language_db import DbLanguages
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
        entities = []
        for record in records:
            entity = LanguageEntity()
            entity.set_language_id(records['m_language_id'])
            entity.set_language_name(records['m_language_name'])
            entities.append(entity)
        
        return entities

    def insert(self, params):
        return self.__db.insert()

    def update(self, params):
        return self.__db.update()

    def delete(self, params):
        return self.__db.delete()
