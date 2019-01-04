# -*- coding: UTF-8 -*-

from app.controller.base_controller import BaseController
from app.validator.word_validator import WordValidator
from app.service.word_service import WordService
from app.entity.word_entity import WordEntity

from app.helper.helper import HashHelper

'''
Word Controller Module
'''
class WordController(BaseController):
    def __init__(self, request):
        super().__init__(request)
        self.set_page_info('単語帳', '選択した言語の単語を登録・編集・削除します。', '')
        self.__user_id = self.get_login_user()
        self.__service = WordService()
        self.__validator = WordValidator()
        pass

    def index(self, language_id=0):
        language_id = self.get_param('language_id') if self.get_param('language_id') != '' else self.get_session('language_id')
        limit = self.get_param('limit', 10)
        offset = self.get_param('offset', 0)
        
        # TODO validation
        # session をクリアする
        self.set_session('language_id', '')
        self.set_session('word_id', '')
        self.set_session('word_spell', '')
        self.set_session('word_explanation', '')
        self.set_session('word_pronunciation', '')
        self.set_session('word_is_learned', '')
        self.set_session('word_note', '')

        # TODO もっと良い方法を考える
        entity = self.__service.getList(self.__user_id, language_id, limit, offset)
        entity.set_language_id(language_id)
        return self.view('./template/admin/words/list.html', entity=entity)
    
    def create(self, language_id):
        # TODO validation
        
        self.set_session('language_id', language_id)

        entity = WordEntity()
        entity.set_language_id(language_id)
        return self.view('./template/admin/words/create.html', entity=entity)

    def detail(self, language_id, word_id):
        # TODO validation
        
        # session に値をセットする
        self.set_session('language_id', language_id)
        self.set_session('word_id', word_id)
        
        return self.view('./template/admin/words/detail.html', entity=self.__service.get(self.__user_id, language_id, word_id))

    def edit(self, language_id, word_id):
        return self.view('./template/admin/words/edit.html', entity=self.__service.get(self.__user_id, language_id, word_id))
    
    def confirm(self, language_id):
        language_id = self.get_session('language_id')
        word_id = self.get_session('word_id')
        
        word_spell = self.get_param('word_spell')
        word_explanation = self.get_param('word_explanation')
        word_pronunciation = self.get_param('word_pronunciation')
        word_is_learned = self.get_param('word_is_learned', 0)
        word_note = self.get_param('word_note')
        
        error_messages = self.__validator.get_error_messages(link_category_name, link_category_display_order)
        if(len(error_messages) == 0):
            self.set_session('word_spell', word_spell)
            self.set_session('word_explanation', word_explanation)
            self.set_session('word_pronunciation', word_pronunciation)
            self.set_session('word_is_learned', word_is_learned)
            self.set_session('word_note', word_note)
            template = './template/admin/words/confirm.html'
        else:
            template = './template/admin/words/create.html'
            
        # TODO Factory Class
        entity = WordEntity()
        entity.set_language_id(language_id)
        entity.set_word_id(word_id)
        entity.set_word_spell(word_spell)
        entity.set_word_explanation(word_explanation)
        entity.set_word_pronunciation(word_pronunciation)
        entity.set_word_is_learned(word_is_learned)
        entity.set_word_note(word_note)
        entity.set_error_message(error_messages)
        return self.view(template, entity=entity)

    def insert(self, language_id):
        language_id = self.get_session('language_id')
        word_spell = self.get_session('word_spell')
        word_explanation = self.get_session('word_explanation')
        word_pronunciation = self.get_session('word_pronunciation')
        word_is_learned = self.get_session('word_is_learned')
        word_note = self.get_session('word_note')
        
        # TODO validation
        
        # session をクリアする
        self.set_session('word_id', '')
        self.set_session('word_spell', '')
        self.set_session('word_explanation', '')
        self.set_session('word_pronunciation', '')
        self.set_session('word_is_learned', '')
        self.set_session('word_note', '')

        entity = self.__service.create(self.__user_id, language_id, word_spell, word_explanation, word_pronunciation, word_is_learned, word_note)
        entity.set_language_id(language_id)
        return self.view('./template/admin/words/complete.html', entity=entity)

    def update(self, language_id, word_id):
        language_id = self.get_session('language_id')
        word_id = self.get_session('word_id')
        word_spell = self.get_session('word_spell')
        word_explanation = self.get_session('word_explanation')
        word_pronunciation = self.get_session('word_pronunciation')
        word_is_learned = self.get_session('word_is_learned')
        word_note = self.get_session('word_note')
        
        # session をクリアする
        self.set_session('word_id', '')
        self.set_session('word_spell', '')
        self.set_session('word_explanation', '')
        self.set_session('word_pronunciation', '')
        self.set_session('word_is_learned', '')
        self.set_session('word_note', '')

        entity = WordEntity()
        entity.set_language_id(language_id)
        entity.set_word_id(self.__service.update(self.__user_id, language_id, word_id, word_spell, word_explanation, word_pronunciation, word_is_learned, word_note))
        return self.view('./template/admin/words/complete.html', entity=entity)
    
    def delete(self, language_id, word_id):
        word_id = self.get_param('word_id')

        self.set_session('language_id', language_id)
        # session をクリアする
        self.set_session('word_id', '')
        
        entity = WordEntity()
        entity.set_language_id(language_id)
        entity.set_word_id(self.__service.delete(self.__user_id, language_id, word_id))
        return self.view('./template/admin/words/complete.html', entity=entity)   