#-*- UTF-8 -*-

from app.infrastructure.language_db import DbLanguages
from app.entity.link_category_entity import LinkCategoryEntity
from app.entity.link_category_list_entity import LinkCategoryListEntity

'''
Link Category Repository Module
'''
class LinkCategoryRepository():
    __db = None
    
    def __init__(self):
        self.__db = DbLinkCategories()
        pass

    def find(self, user_id, link_category_id):
        record = self.__db.selectOne(user_id, link_category_id)

        entity = LanguageEntity()
        if record is not None:
            entity.set_language_id(record[0])
            entity.set_language_name(record[1])
            
        return entity

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

    def update(self, language_id, user_id, language_name):
        is_success = self.__db.update(language_id, user_id, language_name)
        if is_success == True:
            return language_id
        else:
            return ''

    def delete(self, language_id, user_id):
        is_success = self.__db.delete(language_id, user_id)
        if is_success == True:
            return language_id
        else:
            return ''