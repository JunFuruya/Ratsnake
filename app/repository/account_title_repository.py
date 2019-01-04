# -*- coding: UTF-8 -*-

from app.infrastructure.account_title_db import DbAccountTitles
from app.entity.account_title_entity import AccountTitleEntity
from app.entity.account_title_list_entity import AccountTitleListEntity

'''
Account Title Repository Module
'''
class AccountTitleRepository():
    __db = None
    
    def __init__(self):
        self.__db = DbAccountTitles()
        pass

    def find(self, user_id, account_title_id):
        record = self.__db.selectOne(user_id, account_title_id)

        entity = AccountTitleEntity()
        if record is not None:
            entity.set_account_title_id(record[0])
            entity.set_account_title_name(record[1])
            entity.set_account_title_classification_type(record[2])
            
        return entity

    def findList(self, user_id, limit, offset):
        records = self.__db.selectAll(user_id, limit, offset)
        list_entity = AccountTitleListEntity()
        
        entities = []
        for record in records:
            entity = AccountTitleEntity()
            entity.set_account_title_id(record[0])
            entity.set_account_title_name(record[1])
            entity.set_account_title_classification_type(record[2])
            entities.append(entity)
            
        list_entity.set_account_title_entity_list(entities)
        
        return list_entity

    def insert(self, user_id, account_title_name, account_title_classification_type):
        entity = AccountTitleEntity()
        return entity.set_account_title_id(self.__db.insert(user_id, account_title_name, account_title_classification_type))

    def update(self, account_title_id, user_id, account_title_name, account_title_classification_type):
        is_success = self.__db.update(account_title_id, user_id, account_title_name, account_title_classification_type)
        if is_success == True:
            return account_title_id
        else:
            return ''

    def delete(self, account_title_id, user_id):
        is_success = self.__db.delete(account_title_id, user_id)
        if is_success == True:
            return account_title_id
        else:
            return ''