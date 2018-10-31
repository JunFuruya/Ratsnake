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
        session = request.environ.get('beaker.session')
        # TODO セッションからとる
        user_id = 1
        # TODO もっと良い方法を考える
        if language_id == 0:
            language_id = request.query.get('language_id')
        if language_id == '':
            language_id = HashHelper.hexdigest('language_id') in session
 
        # TODO もっと良い方法を考える
        limit = request.query.get('limit')
        limit = limit if limit is not None else 10
            
        # TODO もっと良い方法を考える
        offset = request.query.get('offset')
        offset = offset if offset is not None else 0
        
        # session をクリアする
        self.set_settion('language_id', '')
        self.set_settion('word_id', '')
        self.set_settion('word_name', '')

        # TODO もっと良い方法を考える
        entity = self.__service.getList(user_id, language_id, limit, offset)
        entity.set_language_id(language_id)
        
        return self.view('./template/admin/words/list.html', entity=entity)
    
    def create(self, language_id):
        # TODO セッションからとる
        user_id = 1

        # TODO validation
        
        session = request.environ.get('beaker.session')
        session[HashHelper.hexdigest('language_id')] = language_id
        session.save()

        entity = WordEntity()
        entity.set_language_id(language_id)
        return self.view('./template/admin/words/create.html', entity=entity)

    def detail(self, language_id, word_id):
        # TODO user_id 取得する
        user_id = 1
        # TODO validation
        
        # session に値をセットする
        self.set_settion('language_id', language_id)
        self.set_settion('word_id', word_id)
        
        return self.view('./template/admin/words/detail.html', entity=self.__service.get(user_id, language_id, word_id))

    def edit(self, request, language_id, word_id):
        # TODO user_id 取得する
        user_id = 1
        
        return self.view('./template/admin/words/edit.html', entity=self.__service.get(user_id, language_id, word_id))
    
    def confirm(self, language_id):
        language_id = self.get_session('language_id')
        word_id = self.get_session.get('word_id')
        # TODO user_id 取得する
        user_id = 1
        
        word_spell = self.get_param('word_spell', '')
        word_explanation = self.get_param('word_explanation', '')
        word_pronounciation = self.get_param('word_pronounciation', '')
        # TODO 取得した値に応じて表示する
        word_is_learned = 0
        word_note = request.forms.get('word_note')
        
        # TODO validation
        
        self.set_settion('word_spell', word_spell)
        self.set_settion('word_explanation', word_explanation)
        self.set_settion('word_pronounciation', word_pronounciation)
        self.set_settion('word_is_learned', word_is_learned)
        self.set_settion('word_note', word_note)
        
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
        session = request.environ.get('beaker.session')
        language_id = session.get(HashHelper.hexdigest('language_id'), False)
        word_spell = session.get(HashHelper.hexdigest('word_spell'), False)
        word_explanation = session.get(HashHelper.hexdigest('word_explanation'), False)
        word_pronounciation = session.get(HashHelper.hexdigest('word_pronounciation'), False)
        word_is_learned = session.get(HashHelper.hexdigest('word_is_learned'), False)
        word_note = session.get(HashHelper.hexdigest('word_note'), False)
        
        #TODO ログイン時に取得するようにする
        user_id = 1
        
        # TODO validation
        
        # session をクリアする
        self.set_settion('word_id', '')
        self.set_settion('word_spell', '')

        entity = self.__service.create(user_id, language_id, word_spell, word_explanation, word_pronounciation, word_is_learned, word_note)
        entity.set_language_id(language_id)
        return self.view('./template/admin/words/complete.html', entity=entity)

    def update(self, language_id, word_id):
        language_id = session.get(HashHelper.hexdigest('language_id'), False)
        word_id = session.get(HashHelper.hexdigest('word_id'), False)
        word_spell = session.get(HashHelper.hexdigest('word_spell'), False)
        word_explanation = session.get(HashHelper.hexdigest('word_explanation'), False)
        word_pronounciation = session.get(HashHelper.hexdigest('word_pronounciation'), False)
        word_is_learned = session.get(HashHelper.hexdigest('word_is_learned'), False)
        word_note = session.get(HashHelper.hexdigest('word_note'), False)
        #TODO ログイン時に取得するようにする 
        user_id = 1
        
        # session をクリアする
        self.set_settion('word_id', '')
        self.set_settion('word_spell', '')
        self.set_settion('word_explanation', '')
        self.set_settion('word_pronounciation', '')
        self.set_settion('word_is_learned', '')
        self.set_settion('word_note', '')

        entity = WordEntity()
        entity.set_language_id(language_id)
        entity.set_word_id(self.__service.update(user_id, language_id, word_id, word_spell, word_explanation, word_pronounciation, word_is_learned, word_note))

        return self.view('./template/admin/words/complete.html', entity=entity)
    
    def delete(self, language_id, word_id):
        word_id = request.forms.get('word_id')
        #TODO ログイン時に取得するようにする 
        user_id = 1

        # session をクリアする
        self.set_settion('word_id', '')
        
        entity = WordEntity()
        entity.set_language_id(language_id)
        entity.set_word_id(self.__service.delete(user_id, language_id, word_id))
        
        return self.view('./template/admin/words/complete.html', entity=entity)
    