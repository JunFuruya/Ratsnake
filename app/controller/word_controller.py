#-*- UTF-8 -*-

from app.controller.base_controller import BaseController
from app.service.word_service import WordService
from app.entity.word_entity import WordEntity

from app.helper.helper import HashHelper

'''
Word Controller Module
'''
class WordController(BaseController):
    def __init__(self, request):
        super().__init__(request)
        self.__service = WordService()
        self.__title = '単語帳'
        self.__description = '選択した言語の単語を登録・編集・削除します。'
        self.__notification = 'Please enter your id and password.'
        pass

    def index(self, language_id=0):
        # TODO セッションからとる
        user_id = 1
        language_id = self.get_param('language_id') if self.get_param('language_id') != '' else self.get_session('language_id')
        limit = self.get_param('limit', 10)
        offset = self.get_param('offset', 0)
        
        # TODO validation
        # session をクリアする
        self.set_session('language_id', '')
        self.set_session('word_id', '')
        self.set_session('word_spell', '')
        self.set_session('word_explanation', '')
        self.set_session('word_pronounciation', '')
        self.set_session('word_is_learned', '')
        self.set_session('word_note', '')

        # TODO もっと良い方法を考える
        entity = self.__service.getList(user_id, language_id, limit, offset)
        entity.set_language_id(language_id)
        return self.view('./template/admin/words/list.html', entity=entity)
    
    def create(self, language_id):
        # TODO セッションからとる
        user_id = 1

        # TODO validation
        
        self.set_session('language_id', language_id)

        entity = WordEntity()
        entity.set_language_id(language_id)
        return self.view('./template/admin/words/create.html', entity=entity)

    def detail(self, language_id, word_id):
        # TODO user_id 取得する
        user_id = 1
        # TODO validation
        
        # session に値をセットする
        self.set_session('language_id', language_id)
        self.set_session('word_id', word_id)
        
        return self.view('./template/admin/words/detail.html', entity=self.__service.get(user_id, language_id, word_id))

    def edit(self, language_id, word_id):
        # TODO user_id 取得する
        user_id = 1
        return self.view('./template/admin/words/edit.html', entity=self.__service.get(user_id, language_id, word_id))
    
    def confirm(self, language_id):
        language_id = self.get_session('language_id')
        word_id = self.get_session('word_id')
        # TODO user_id 取得する
        user_id = 1
        
        word_spell = self.get_param('word_spell')
        word_explanation = self.get_param('word_explanation')
        word_pronounciation = self.get_param('word_pronounciation')
        word_is_learned = self.get_param('word_is_learned', 0)
        word_note = self.get_param('word_note')
        
        # TODO validation
        
        self.set_session('word_spell', word_spell)
        self.set_session('word_explanation', word_explanation)
        self.set_session('word_pronounciation', word_pronounciation)
        self.set_session('word_is_learned', word_is_learned)
        self.set_session('word_note', word_note)
        
        # TODO もっと良い設計があるはず
        entity = WordEntity()
        entity.set_language_id(language_id)
        entity.set_word_id(word_id)
        entity.set_word_spell(word_spell)
        entity.set_word_explanation(word_explanation)
        entity.set_word_pronounciation(word_pronounciation)
        entity.set_word_is_learned(word_is_learned)
        entity.set_word_note(word_note)
        return self.view('./template/admin/words/confirm.html', entity=entity)

    def insert(self, language_id):
        language_id = self.get_session('language_id')
        word_spell = self.get_session('word_spell')
        word_explanation = self.get_session('word_explanation')
        word_pronounciation = self.get_session('word_pronounciation')
        word_is_learned = self.get_session('word_is_learned')
        word_note = self.get_session('word_note')
        
        #TODO ログイン時に取得するようにする
        user_id = 1
        
        # TODO validation
        
        # session をクリアする
        self.set_session('word_id', '')
        self.set_session('word_spell', '')
        self.set_session('word_explanation', '')
        self.set_session('word_pronounciation', '')
        self.set_session('word_is_learned', '')
        self.set_session('word_note', '')

        entity = self.__service.create(user_id, language_id, word_spell, word_explanation, word_pronounciation, word_is_learned, word_note)
        entity.set_language_id(language_id)
        return self.view('./template/admin/words/complete.html', entity=entity)

    def update(self, language_id, word_id):
        language_id = self.get_session('language_id')
        word_id = self.get_session('word_id')
        word_spell = self.get_session('word_spell')
        word_explanation = self.get_session('word_explanation')
        word_pronounciation = self.get_session('word_pronounciation')
        word_is_learned = self.get_session('word_is_learned')
        word_note = self.get_session('word_note')
        #TODO ログイン時に取得するようにする 
        user_id = 1
        
        # session をクリアする
        self.set_session('word_id', '')
        self.set_session('word_spell', '')
        self.set_session('word_explanation', '')
        self.set_session('word_pronounciation', '')
        self.set_session('word_is_learned', '')
        self.set_session('word_note', '')

        entity = WordEntity()
        entity.set_language_id(language_id)
        entity.set_word_id(self.__service.update(user_id, language_id, word_id, word_spell, word_explanation, word_pronounciation, word_is_learned, word_note))
        return self.view('./template/admin/words/complete.html', entity=entity)
    
    def delete(self, language_id, word_id):
        word_id = self.get_param('word_id')
        #TODO ログイン時に取得するようにする 
        user_id = 1

        self.set_session('language_id', language_id)
        # session をクリアする
        self.set_session('word_id', '')
        
        entity = WordEntity()
        entity.set_language_id(language_id)
        entity.set_word_id(self.__service.delete(user_id, language_id, word_id))
        return self.view('./template/admin/words/complete.html', entity=entity)   