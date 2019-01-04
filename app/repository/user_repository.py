# -*- coding: UTF-8 -*-

from app.entity.user_list_entity import UserListEntity
from app.entity.user_entity import UserEntity
from app.infrastructure.user_db import DbUsers

'''
User Repository Module
'''
class UsersRepository():
    __db = None
    
    def __init__(self):
        self.__db = DbUsers()
        pass

    def findByLoginInfo(self, username, password):
        record = self.__db.selectByLoginInfo(username, password)
        print(record[0])
        if len(record) > 0:
            return record[0]
        else:
            return None

    def findList(self, limit, offset):
        records = self.__db.selectAll(limit, offset)
        
        list_entity = UserListEntity()
        entities = []
        for record in records:
            entity = UserEntity()
            entity.set_user_id(record[0])
            entity.set_user_username(record[1])
            entity.set_user_hashed_password(record[2])
            entities.append(entity)
            
        return list_entity.set_user_entity_list(entities);

    def find(self, user_id):
        record = self.__db.selectOne(user_id)

        entity = UserEntity()
        if record is not None:
            entity.set_user_id(record[0])
            entity.set_user_username(record[1])
            entity.set_user_hashed_password(record[2])
        
        return entity

    def insert(self, user_name, user_hashed_password):
        entity = UserEntity()
        entity.set_user_id(self.__db.insert(user_name, user_hashed_password))
        return entity

    def update(self, user_id, user_name, user_hashed_password):
        return self.__db.update(user_id, user_name, user_hashed_password)

    def delete(self, user_id):
        return self.__db.delete(user_id)
