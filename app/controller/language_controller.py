#-*- UTF-8 -*-

from app.controller.base_controller import BaseController
from app.service.language_service import LanguageService
from app.entity.language_entity import LanguageEntity

from app.helper.helper import HashHelper

'''
Language Controller Module
'''
class LanguageController(BaseController):

    def __init__(self):
        self.__service = LanguageService()
        self.__title = '言語マスタ'
        self.__description = '単語帳を作成する対象の言語を登録・編集・削除します。'
        pass

    def index(self, request):
        # TODO もっと良い方法を考える
        limit = request.query.get('limit')
        limit = limit if limit is not None else 10
            
        # TODO もっと良い方法を考える
        offset = request.query.get('offset')
        offset = offset if offset is not None else 0

        session = request.environ.get('beaker.session')
        session[HashHelper.hexdigest('language_id')] = ''
        session[HashHelper.hexdigest('language_name')] = ''
        session.save()

        # TODO もっと良い方法を考える
        entity = self.__service.getList(limit, offset)
        # TODO もっと良い方法を考える
        entity.set_title(self.__title)
        entity.set_description(self.__description)
        entity.set_notification('This is the index page.')
        
        return self.view('./template/admin/languages/list.html', entity)
    
    def create(self, request):
        entity = LanguageEntity()
        entity.set_title(self.__title)
        entity.set_description(self.__description)
        entity.set_notification('This is the index page.')
        return self.view('./template/admin/languages/create.html', entity)

    def detail(self, request, language_id):
        
        # TODO user_id 取得する
        user_id = 1
        # TODO validation
        
        session = request.environ.get('beaker.session')
        session[HashHelper.hexdigest('language_id')] = language_id
        session.save()
        
        entity = self.__service.get(user_id, language_id)
        entity.set_title(self.__title)
        entity.set_description(self.__description)
        entity.set_notification('This is the index page.')
        return self.view('./template/admin/languages/detail.html', entity)

    def edit(self, request, language_id):
        session = request.environ.get('beaker.session')
        language_id = session.get(HashHelper.hexdigest('language_id'), False)
        # TODO user_id 取得する
        user_id = 1
        
        entity = self.__service.get(user_id, language_id)
        entity.set_title(self.__title)
        entity.set_description(self.__description)
        entity.set_notification('This is the index page.')
        return self.view('./template/admin/languages/edit.html', entity)
    
    def confirm(self, request):
        session = request.environ.get('beaker.session')
        language_id = session.get(HashHelper.hexdigest('language_id'), False)
        language_name = request.forms.get('language_name')

        # TODO validation
        
        session[HashHelper.hexdigest('language_name')] = language_name
        session.save()
        
        # TODO もっと良い設計があるはず
        entity = LanguageEntity()
        entity.set_title(self.__title)
        entity.set_language_id(language_id)
        entity.set_language_name(language_name)
        entity.set_description(self.__description)
        entity.set_notification('This is the index page.')
        return self.view('./template/admin/languages/confirm.html', entity)

    def insert(self, request):
        session = request.environ.get('beaker.session')
        language_name = session.get(HashHelper.hexdigest('language_name'), False)
        
        #TODO ログイン時に取得するようにする 
        user_id = 1
        
        # TODO validation
        
        session = request.environ.get('beaker.session')
        session[HashHelper.hexdigest('language_id')] = ''
        session[HashHelper.hexdigest('language_name')] = ''
        session.save()

        entity = self.__service.create(user_id, language_name)
        entity.set_title(self.__title)
        entity.set_description(self.__description)
        entity.set_notification('This is the index page.')
        return self.view('./template/admin/languages/complete.html', entity)

    def update(self, request):
        session = request.environ.get('beaker.session')
        language_id = session.get(HashHelper.hexdigest('language_id'), False)
        language_name = session.get(HashHelper.hexdigest('language_name'), False)
        #TODO ログイン時に取得するようにする 
        user_id = 1
        
        session = request.environ.get('beaker.session')
        session[HashHelper.hexdigest('language_id')] = ''
        session[HashHelper.hexdigest('language_name')] = ''
        session.save()

        entity = LanguageEntity()
        entity.set_language_id(self.__service.update(language_id, user_id, language_name))
        entity.set_title(self.__title)
        entity.set_description(self.__description)
        entity.set_notification('This is the index page.')
        return self.view('./template/admin/languages/complete.html', entity)
    
    def delete(self, request):
        language_id = request.forms.get('language_id')
        #TODO ログイン時に取得するようにする 
        user_id = 1

        session = request.environ.get('beaker.session')
        session[HashHelper.hexdigest('language_id')] = ''
        session[HashHelper.hexdigest('language_name')] = ''
        session.save()

        entity = LanguageEntity()
        entity.set_language_id(self.__service.delete(language_id, user_id))
        entity.set_title(self.__title)
        entity.set_description(self.__description)
        entity.set_notification('This is the index page.')
        return self.view('./template/admin/languages/complete.html', entity)
    