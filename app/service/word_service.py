# -*- coding: UTF-8 -*-

from app.service.base_service import BaseService
from app.repository.word_repository import WordRepository
from app.repository.language_repository import LanguageRepository
from app.repository.user_repository import UsersRepository
from app.entity.word_entity import WordEntity

class WordService(BaseService):
    
    def __init__(self):
        self.__reposiroty = WordRepository()
        self.__language_repository = LanguageRepository()
        pass

    def getList(self, user_id, language_id, limit, offset):
        return self.__reposiroty.findList(user_id, language_id, limit, offset)

    def get(self, user_id, language_id, word_id):
        return self.__reposiroty.find(user_id, language_id, word_id)

    def create(self, user_id, language_id, word_spell, word_explanation, word_pronunciation, word_is_learned, word_note):
        return self.__reposiroty.insert(user_id, language_id, word_spell, word_explanation, word_pronunciation, word_is_learned, word_note)

    def update(self, user_id, language_id, word_id, word_spell, word_explanation, word_pronunciation, word_is_learned, word_note):
        return self.__reposiroty.update(user_id, language_id, word_id, word_spell, word_explanation, word_pronunciation, word_is_learned, word_note)

    def delete(self, user_id, language_id, word_id):
        return self.__reposiroty.delete(user_id, language_id, word_id)

    def get_language(self, user_id, language_id):
        entity = WordEntity()
        language_entity = self.__language_repository.find(user_id, language_id)
        entity.set_language_name(language_entity.get_language_name())
        return entity
    
    def consult_dictionary(self, foreign_word):
        return self.__reposiroty.consult_google_dictionary(foreign_word)
