# -*- coding: utf-8 -*-

from app.service.base_service import BaseService
from app.repository.language_repository import LanguageRepository
from app.repository.user_repository import UsersRepository

class LanguageService(BaseService):
    def __init__(self):
        self.__reposiroty = LanguageRepository()
        pass

    def getList(self, user_id, limit, oiffset):
        return self.__reposiroty.findList(user_id, limit, oiffset)

    def get(self, user_id, language_id):
        return self.__reposiroty.find(user_id, language_id)

    def create(self, user_id, language_name):
        return self.__reposiroty.insert(user_id, language_name)

    def update(self, language_id, user_id, language_name):
        return self.__reposiroty.update(language_id, user_id, language_name)

    def delete(self, language_id, user_id):
        return self.__reposiroty.delete(language_id, user_id)
