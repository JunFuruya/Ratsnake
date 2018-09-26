#-*- UTF-8 -*-

from app.controller.base_controller import BaseController
from app.service.web_service import LanguageService
from app.entity.language_entity import LanguageEntity

from app.helper.helper import HashHelper

'''
Language Controller Module
'''
class LanguageController(BaseController):

    def __init__(self):
        self.__service = LanguageService()
        self.__title = '言語マスタ'
        self.__description = '単語帳を作成する言語を登録・編集・削除します。'
        pass

    def index(self, request):
        # TODO もっと良い方法を考える
        limit = request.query.get('limit')
        limit = limit if limit is not None else 10
            
        # TODO もっと良い方法を考える
        offset = request.query.get('offset')
        offset = offset if offset is not None else 0
        
        # TODO もっと良い方法を考える
        entity = self.__service.getList(limit, offset)
        # TODO もっと良い方法を考える
        if(entity is not None):
            entity.set_title(self.__title)
            entity.set_description(self.__description)
            entity.set_notification('This is the index page.')
        
        return self.view('./template/admin/languages/list.html', entity)
    
    def detail(self, request):
        language_id = request.query.get('language_id')
        entity = self.__service.get(language_id)
        entity.set_title(self.__title)
        entity.set_description(self.__description)
        entity.set_notification('This is the index page.')
        return self.view('./template/admin/languages/detail.html', entity)
    
    def create(self, request):
        entity = LanguageEntity()
        entity.set_title(self.__title)
        entity.set_description(self.__description)
        entity.set_notification('This is the index page.')
        return self.view('./template/admin/languages/create.html', entity)

    def confirm(self, request):
        language_name = request.forms.get('language_name')
        # TODO validation
        
        session = request.environ.get('beaker.session')
        session['language_name'] = HashHelper.hexdigest(language_name)
        session.save()
        
        print(language_name)
        # TODO もっと良い設計があるはず
        entity = LanguageEntity()
        entity.set_title(self.__title)
        entity.set_language_name(language_name)
        entity.set_description(self.__description)
        entity.set_notification('This is the index page.')
        return self.view('./template/admin/languages/confirm.html', entity)

    def insert(self, request):
        session = request.environ.get('beaker.session')
        language_name = session.get('language_name', False)
        
        #TODO ログイン時に取得するようにする 
        user_id = 1
        
        # TODO validation
        
        entity = self.__service.insert(user_id, language_name)
        entity.set_title(self.__title)
        entity.set_description(self.__description)
        entity.set_notification('This is the index page.')
        return self.view('./template/admin/languages/complete.html', entity)

    def update(self, request):
        session = request.environ.get('beaker.session')
        language_name = session.get('language_name', False)
        
        entity.set_title(self.__title)
        entity = self.__service.update(language_id, language_name)
        entity.set_description(self.__description)
        entity.set_notification('This is the index page.')
        return self.view('./template/admin/languages/complete.html', entity)
    
    def delete(self, request):
        language_id = request.query.get('language_id')
        entity = self.__service.delete(language_id)
        entity.set_title(self.__title)
        entity.set_description(self.__description)
        entity.set_notification('This is the index page.')
        return self.view('./template/admin/languages/complete.html', entity)
    