#-*- UTF-8 -*-

from app.infrastructure.link_category_db import DbLinkCategories
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

        entity = LinkCategoryEntity()
        if record is not None:
            entity.set_link_category_id(record[0])
            entity.set_user_id(record[1])
            entity.set_link_category_name(record[2])
            entity.set_link_category_display_order(record[3])
            
        return entity

    def findList(self, user_id, limit, offset):
        records = self.__db.selectAll(user_id, limit, offset)
        list_entity = LinkCategoryListEntity()
        
        entities = []
        for record in records:
            entity = LinkCategoryEntity()
            entity.set_link_category_id(record[0])
            entity.set_link_category_name(record[1])
            entities.append(entity)
            
        list_entity.set_link_category_entity_list(entities)
        
        return list_entity

    def insert(self, user_id, link_category_name, link_category_display_order):
        entity = LinkCategoryEntity()
        return entity.set_link_category_id(self.__db.insert(user_id, link_category_name, link_category_display_order))

    def update(self, link_category_id, user_id, link_category_name, link_category_display_order):
        is_success = self.__db.update(link_category_id, user_id, link_category_name, link_category_display_order)
        if is_success == True:
            return link_category_id
        else:
            return ''

    def delete(self, link_category_id, user_id):
        is_success = self.__db.delete(link_category_id, user_id)
        if is_success == True:
            return link_category_id
        else:
            return ''