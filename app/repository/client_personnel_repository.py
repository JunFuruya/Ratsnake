# -*- coding: UTF-8 -*-

from app.entity.client_personnel_list_entity import ClientPersonnelListEntity
from app.entity.client_personnel_entity import ClientPersonnelEntity
from app.infrastructure.client_personnel_db import DbClientPersonnels

'''
Client Personnel Repository Module
'''
class ClientPersonnelRepository():
    __db = None
    
    def __init__(self):
        self.__db = DbClientPersonnels()
        pass

    def findByLoginInfo(self, username, password):
        record = self.__db.selectByLoginInfo(username, password)
        
        if record is not None:
            return record[0]
        else:
            return None

    def findList(self, limit, offset):
        records = self.__db.selectAll(limit, offset)
        
        list_entity = ClientListEntity()
        entities = []
        for record in records:
            entity = ClientPersonnelEntity()
            entity.set_user_id(record[0])
            entity.set_user_username(record[1])
            entity.set_user_hashed_password(record[2])
            entities.append(entity)
            
        return list_entity.set_user_entity_list(entities);

    def find(self, user_id):
        record = self.__db.selectOne(user_id)

        entity = ClientPersonnelEntity()
        if record is not None:
            entity.set_user_id(record[0])
            entity.set_user_username(record[1])
            entity.set_user_hashed_password(record[2])
        
        return entity

    def insert(self, user_name, user_hashed_password):
        entity = ClientPersonnelEntity()
        entity.set_user_id(self.__db.insert(user_name, user_hashed_password))
        return entity

    def update(self, user_id, user_name, user_hashed_password):
        return self.__db.update(user_id, user_name, user_hashed_password)

    def delete(self, user_id):
        return self.__db.delete(user_id)
