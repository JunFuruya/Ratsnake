# -*- coding: utf-8 -*-

from app.service.base_service import BaseService
from app.repository.Word_repository import WordRepository
from app.repository.db_user_repository import DbUsersRepository

class WordService(BaseService):
    def __init__(self):
        self.__reposiroty = WordRepository()
        pass

    def getList(self, limit, oiffset):
        return self.__reposiroty.findList(limit, oiffset)

    def get(self, user_id, word_id):
        return self.__reposiroty.find(user_id, word_id)

    def create(self, user_id, word_name):
        return self.__reposiroty.insert(user_id, word_name)

    def update(self, word_id, user_id, word_name):
        return self.__reposiroty.update(word_id, user_id, word_name)

    def delete(self, word_id, user_id):
        return self.__reposiroty.delete(word_id, user_id)
