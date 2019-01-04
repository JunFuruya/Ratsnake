# -*- coding: UTF-8 -*-

from app.service.base_service import BaseService
from app.repository.user_repository import UsersRepository

class UserService(BaseService):
    def __init__(self):
        self.__reposiroty = UsersRepository()
        pass

    def getList(self, limit, offset):
        return self.__reposiroty.findList(limit, offset)

    def get(self, user_id):
        return self.__reposiroty.find(user_id)

    def create(self, user_name, user_hashed_password):
        return self.__reposiroty.insert(user_name, user_hashed_password)

    def update(self, user_id, user_name, user_hashed_password):
        return self.__reposiroty.update(user_id, user_name, user_hashed_password)

    def delete(self, user_id):
        return self.__reposiroty.delete(user_id)
