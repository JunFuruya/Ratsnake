#-*- UTF-8 -*-

from app.controller.base_controller import BaseController
from app.service.language_service import LanguageService
from app.entity.language_entity import LanguageEntity

from app.helper.helper import HashHelper

'''
Language Controller Module
'''
class LanguageController(BaseController):
    def __init__(self, request):
        super().__init__(request)
        self.__title = '言語マスタ'
        self.__description = '単語帳を作成する対象の言語を登録・編集・削除します。'
        self.__notification = 'Please enter your id and password.'
        
        self.__service = LanguageService()
        pass

    def index(self):
        limit = self.get_param('limit', 10)
        offset = self.get_param('offset', 0)

        # session をクリアする
        self.set_session('language_id', '')
        self.set_session('language_name', '')
        
        return self.view('./template/admin/languages/list.html', self.__service.getList(limit, offset))
    
    def create(self):
        return self.view('./template/admin/languages/create.html', LanguageEntity())

    def detail(self, language_id):
        
        # TODO user_id 取得する
        user_id = 1
        # TODO validation
        
        session = request.environ.get('beaker.session')
        session[HashHelper.hexdigest('language_id')] = language_id
        session.save()
        
        entity = self.__service.get(user_id, language_id)
        return self.view('./template/admin/languages/detail.html', entity)

    def edit(self, language_id):
        session = request.environ.get('beaker.session')
        language_id = session.get(HashHelper.hexdigest('language_id'), False)
        # TODO user_id 取得する
        user_id = 1
        
        entity = self.__service.get(user_id, language_id)
        return self.view('./template/admin/languages/edit.html', entity)
    
    def confirm(self):
        session = request.environ.get('beaker.session')
        language_id = session.get(HashHelper.hexdigest('language_id'), False)
        language_name = request.forms.get('language_name')

        # TODO validation
        
        self.set_session('language_name', language_name)
        
        # TODO もっと良い設計があるはず
        entity = LanguageEntity()
        entity.set_language_id(language_id)
        entity.set_language_name(language_name)
        return self.view('./template/admin/languages/confirm.html', entity)

    def insert(self):
        session = request.environ.get('beaker.session')
        language_name = session.get(HashHelper.hexdigest('language_name'), False)
        
        #TODO ログイン時に取得するようにする 
        user_id = 1
        
        # TODO validation
        
        # session をクリアする
        self.set_session('language_id', '')
        self.set_session('language_name', '')

        return self.view('./template/admin/languages/complete.html', self.__service.create(user_id, language_name))

    def update(self):
        session = request.environ.get('beaker.session')
        language_id = session.get(HashHelper.hexdigest('language_id'), False)
        language_name = session.get(HashHelper.hexdigest('language_name'), False)
        #TODO ログイン時に取得するようにする 
        user_id = 1
        
        # session をクリアする
        self.set_session('language_id', '')
        self.set_session('language_name', '')

        entity = LanguageEntity()
        entity.set_language_id(self.__service.update(language_id, user_id, language_name))
        return self.view('./template/admin/languages/complete.html', entity)
    
    def delete(self):
        language_id = request.forms.get('language_id')
        #TODO ログイン時に取得するようにする 
        user_id = 1

        # session をクリアする
        self.set_session('language_id', '')
        self.set_session('language_name', '')

        entity = LanguageEntity()
        entity.set_language_id(self.__service.delete(language_id, user_id))
        return self.view('./template/admin/languages/complete.html', entity)
    