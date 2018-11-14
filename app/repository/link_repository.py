# -*- UTF-8 -*-

from app.infrastructure.link_db import DbLinks
from app.infrastructure.link_category_db import DbLinkCategories
from app.entity.link_entity import LinkEntity
from app.entity.link_category_entity import LinkCategoryEntity
from app.entity.link_list_entity import LinkListEntity

'''
Links Repository Module
'''
class LinkRepository():
    __link_db = None
    __link_category_db = None

    def __init__(self):
        self.__link_db = DbLinks()
        self.__link_category_db = DbLinkCategories()
        pass

    def find(self, user_id, link_id):
        record = self.__link_db.selectOne(user_id, link_id)

        entity = LinkEntity()
        entity.set_link_id(link_id)
        if record is not None:
            entity.set_link_id(record[0])
            entity.set_link_category_id(record[1])
            entity.set_link_site_name(record[2])
            entity.set_link_url(record[3])
            entity.set_link_display_order(record[4])
        return entity

    def findList(self, user_id, limit, offset):
        list_entity = LinkListEntity()

        # TODO link cateogry は select() と selectAll() が混在しているので、selectAll() に統一する
        link_ctegory_records = self.__link_category_db.selectAll(user_id, limit, offset)
        link_ctegory_entities = []
        for link_ctegory_record in link_ctegory_records:
            entity = LinkCategoryEntity()
            entity.set_link_category_id(link_ctegory_record[0])
            entity.set_link_category_name(link_ctegory_record[1])
            link_ctegory_entities.append(entity)

        link_records = self.__link_db.selectAll(user_id, limit, offset)
        entities = []
        for link_record in link_records:
            entity = LinkEntity()
            entity.set_link_id(link_record[0])
            entity.set_link_category_id(link_record[1])
            entity.set_link_site_name(link_record[2])
            entity.set_link_url(link_record[3])
            entities.append(entity)

        list_entity.set_link_entity_list(entities)

        return list_entity

    def insert(self, user_id, link_category_id, link_site_name, link_url, link_display_order):
        return LinkEntity().set_link_id(
            self.__link_db.insert(user_id, link_category_id, link_site_name, link_url, link_display_order))

    def update(self, user_id, link_id, link_category_id, link_site_name, link_url, link_display_order):
        is_success = self.__link_db.update(user_id, link_id, link_category_id, link_site_name, link_url, link_display_order)
        if is_success == True:
            return word_id
        else:
            return ''

    def delete(self, user_id, link_id):
        is_success = self.__link_db.delete(user_id, link_id)
        if is_success == True:
            return link_id
        else:
            return ''
