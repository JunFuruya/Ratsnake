# -*- coding: UTF-8 -*-

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
        self.set_page_info('言語マスタ', '単語帳を作成する対象の言語を登録・編集・削除します。', '')
        self.__user_id = self.get_login_user()
        self.__service = LanguageService()
        pass

    def index(self):
        limit = self.get_param('limit', 10)
        offset = self.get_param('offset', 0)

        # session をクリアする
        self.set_session('language_id', '')
        self.set_session('language_name', '')
        
        return self.view('./template/admin/languages/list.html', self.__service.getList(self.__user_id, limit, offset))
    
    def create(self):
        return self.view('./template/admin/languages/create.html', LanguageEntity())

    def detail(self, language_id):
        # TODO validation
        
        self.set_session('language_id', language_id)
        
        return self.view('./template/admin/languages/detail.html', self.__service.get(self.__user_id, language_id))

    def edit(self, language_id):
        language_id = self.get_session('language_id')
        # TODO validation        
        return self.view('./template/admin/languages/edit.html', self.__service.get(self.__user_id, language_id))
    
    def confirm(self):
        language_id = self.get_session('language_id')
        language_name = self.get_param('language_name')

        # TODO validation
        
        self.set_session('language_name', language_name)
        
        # TODO もっと良い設計があるはず
        entity = LanguageEntity()
        entity.set_language_id(language_id)
        entity.set_language_name(language_name)
        return self.view('./template/admin/languages/confirm.html', entity)

    def insert(self):
        language_name = self.get_session('language_name')
        
        # TODO validation
        
        # session をクリアする
        self.set_session('language_id', '')
        self.set_session('language_name', '')

        return self.view('./template/admin/languages/complete.html', self.__service.create(self.__user_id, language_name))

    def update(self):
        language_id = self.get_session('language_id')
        language_name = self.get_session('language_name')
        
        # session をクリアする
        self.set_session('language_id', '')
        self.set_session('language_name', '')

        entity = LanguageEntity()
        entity.set_language_id(self.__service.update(language_id, self.__user_id, language_name))
        return self.view('./template/admin/languages/complete.html', entity)
    
    def delete(self):
        language_id = self.get_param('language_id')

        # session をクリアする
        self.set_session('language_id', '')
        self.set_session('language_name', '')

        entity = LanguageEntity()
        entity.set_language_id(self.__service.delete(language_id, self.__user_id))
        return self.view('./template/admin/languages/complete.html', entity)    