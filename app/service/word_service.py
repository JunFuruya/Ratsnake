# -*- coding: utf-8 -*-

from app.service.base_service import BaseService
from app.repository.word_repository import WordRepository
from app.repository.db_user_repository import DbUsersRepository

class WordService(BaseService):
    def __init__(self):
        self.__reposiroty = WordRepository()
        pass

    def getList(self, user_id, language_id, limit, offset):
        return self.__reposiroty.findList(user_id, language_id, limit, offset)

    def get(self, user_id, language_id, word_id):
        return self.__reposiroty.find(user_id, language_id, word_id)

    def create(self, user_id, language_id, word_spell, word_explanation, word_pronanciation, word_is_learned, word_note):
        return self.__reposiroty.insert(user_id, language_id, word_spell, word_explanation, word_pronanciation, word_is_learned, word_note)

    def update(self, user_id, language_id, word_id, word_spell, word_explanation, word_pronanciation, word_is_learned, word_note):
        return self.__reposiroty.update(user_id, language_id, word_id, word_spell, word_explanation, word_pronanciation, word_is_learned, word_note)

    def delete(self, user_id, language_id, word_id):
        return self.__reposiroty.delete(user_id, language_id, word_id)
