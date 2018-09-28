#-*- UTF-8 -*-

from app.controller.base_controller import BaseController
from app.service.word_service import WordService
from app.entity.word_entity import WordEntity

from app.helper.helper import HashHelper

'''
Word Controller Module
'''
class WordController(BaseController):

    def __init__(self):
        self.__service = WordService()
        self.__title = '単語帳'
        self.__description = '選択した言語の単語を登録・編集・削除します。'
        pass

    def index(self, request):
        # TODO もっと良い方法を考える
        limit = request.query.get('limit')
        limit = limit if limit is not None else 10
            
        # TODO もっと良い方法を考える
        offset = request.query.get('offset')
        offset = offset if offset is not None else 0

        session = request.environ.get('beaker.session')
        session[HashHelper.hexdigest('word_id')] = ''
        session[HashHelper.hexdigest('word_name')] = ''
        session.save()

        # TODO もっと良い方法を考える
        entity = self.__service.getList(limit, offset)
        # TODO もっと良い方法を考える
        entity.set_title(self.__title)
        entity.set_description(self.__description)
        entity.set_notification('This is the index page.')
        
        return self.view('./template/admin/words/list.html', entity)
    
    def create(self, request):
        entity = wordEntity()
        entity.set_title(self.__title)
        entity.set_description(self.__description)
        entity.set_notification('This is the index page.')
        return self.view('./template/admin/words/create.html', entity)

    def detail(self, request, word_id):
        
        # TODO user_id 取得する
        user_id = 1
        # TODO validation
        
        session = request.environ.get('beaker.session')
        session[HashHelper.hexdigest('word_id')] = word_id
        session.save()
        
        entity = self.__service.get(user_id, word_id)
        entity.set_title(self.__title)
        entity.set_description(self.__description)
        entity.set_notification('This is the index page.')
        return self.view('./template/admin/words/detail.html', entity)

    def edit(self, request, word_id):
        session = request.environ.get('beaker.session')
        word_id = session.get(HashHelper.hexdigest('word_id'), False)
        # TODO user_id 取得する
        user_id = 1
        
        entity = self.__service.get(user_id, word_id)
        entity.set_title(self.__title)
        entity.set_description(self.__description)
        entity.set_notification('This is the index page.')
        return self.view('./template/admin/words/edit.html', entity)
    
    def confirm(self, request):
        session = request.environ.get('beaker.session')
        word_id = session.get(HashHelper.hexdigest('word_id'), False)
        word_name = request.forms.get('word_name')

        # TODO validation
        
        session[HashHelper.hexdigest('word_name')] = word_name
        session.save()
        
        # TODO もっと良い設計があるはず
        entity = wordEntity()
        entity.set_title(self.__title)
        entity.set_word_id(word_id)
        entity.set_word_name(word_name)
        entity.set_description(self.__description)
        entity.set_notification('This is the index page.')
        return self.view('./template/admin/words/confirm.html', entity)

    def insert(self, request):
        session = request.environ.get('beaker.session')
        word_name = session.get(HashHelper.hexdigest('word_name'), False)
        
        #TODO ログイン時に取得するようにする 
        user_id = 1
        
        # TODO validation
        
        session = request.environ.get('beaker.session')
        session[HashHelper.hexdigest('word_id')] = ''
        session[HashHelper.hexdigest('word_name')] = ''
        session.save()

        entity = self.__service.create(user_id, word_name)
        entity.set_title(self.__title)
        entity.set_description(self.__description)
        entity.set_notification('This is the index page.')
        return self.view('./template/admin/words/complete.html', entity)

    def update(self, request):
        session = request.environ.get('beaker.session')
        word_id = session.get(HashHelper.hexdigest('word_id'), False)
        word_name = session.get(HashHelper.hexdigest('word_name'), False)
        #TODO ログイン時に取得するようにする 
        user_id = 1
        
        session = request.environ.get('beaker.session')
        session[HashHelper.hexdigest('word_id')] = ''
        session[HashHelper.hexdigest('word_name')] = ''
        session.save()

        entity = wordEntity()
        entity.set_word_id(self.__service.update(word_id, user_id, word_name))
        entity.set_title(self.__title)
        entity.set_description(self.__description)
        entity.set_notification('This is the index page.')
        return self.view('./template/admin/words/complete.html', entity)
    
    def delete(self, request):
        word_id = request.forms.get('word_id')
        #TODO ログイン時に取得するようにする 
        user_id = 1

        session = request.environ.get('beaker.session')
        session[HashHelper.hexdigest('word_id')] = ''
        session[HashHelper.hexdigest('word_name')] = ''
        session.save()

        entity = wordEntity()
        entity.set_word_id(self.__service.delete(word_id, user_id))
        entity.set_title(self.__title)
        entity.set_description(self.__description)
        entity.set_notification('This is the index page.')
        return self.view('./template/admin/words/complete.html', entity)
    