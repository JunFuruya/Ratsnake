# -*- coding: utf-8 -*-

from app.service.base_service import BaseService
from app.repository.language_repository import LanguageRepository
from app.repository.db_user_repository import DbUsersRepository

class LanguageService(BaseService):
    def __init__(self):
        self.__reposiroty = LanguageRepository()
        pass

    def getList(self, limit, oiffset):
        return self.__reposiroty.findList(limit, oiffset)

    def get(self, language_id):
        return self.__reposiroty.find(language_id)

    def create(self, user_id, language_name):
        return self.__reposiroty.insert(user_id, language_name)

    def update(self, language_id, user_id, language_name):
        return self.__reposiroty.update(language_id, user_id, language_name)

    def delete(self, language_id, user_id, language_name):
        return self.__reposiroty.delete(language_id, user_id, language_name)
