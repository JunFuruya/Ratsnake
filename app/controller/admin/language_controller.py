# -*- coding: UTF-8 -*-

import g

from app.controller.base_controller import BaseController
from app.validator.language_validator import LanguageValidator
from app.service.language_service import LanguageService
from app.entity.language_entity import LanguageEntity

'''
Language Controller Module
'''
class LanguageController(BaseController):
    
    def __init__(self, request):
        super().__init__(request)
        self.set_page_info('言語マスタ', '単語帳を作成する対象の言語を登録・編集・削除します。', '')
        self.__user_id = self.get_login_user()
        self.__service = LanguageService()
        self.__validator = LanguageValidator()
        self.set_template_path('./template/admin/languages/')
        pass

    def index(self):
        limit = self.get_param('limit', 10)
        offset = self.get_param('offset', 0)

        # session をクリアする
        self.set_session('language_id', '')
        self.set_session('language_name', '')
        
        return self.view('list.html', self.__service.getList(self.__user_id, limit, offset))
    
    def create(self):
        entity = LanguageEntity()
        entity.set_error_messages(self.get_session('error_messages'))
        self.set_session('error_messages', '')
        return self.view('create.html', entity=entity)

    def detail(self, language_id):
        # TODO validation
        
        self.set_session('language_id', language_id)
        
        return self.view('detail.html', self.__service.get(self.__user_id, language_id))

    def edit(self, language_id):
        language_id = self.get_session('language_id')
        entity = self.__service.get(self.__user_id, language_id)
        entity.set_error_messages(self.get_session('error_messages'))

        self.set_session('error_messages', '')
        
        # TODO validation
        return self.view('edit.html', entity=entity)
    
    def confirm(self):
        language_id = self.get_session('language_id')
        language_name = self.get_param('language_name')

        error_messages = self.__validator.get_error_messages(language_name)
        if(len(error_messages) == 0):
            self.set_session('language_name', language_name)
            template = 'confirm.html'
        else:
            self.set_session('error_messages', error_messages)
            if language_id == '':
                self.redirect('/admin/languages/create')
            else:
                self.redirect('/admin/languages/' + language_id)
        
        # TODO Factory Class
        entity = LanguageEntity()
        entity.set_language_id(language_id)
        entity.set_language_name(language_name)
        entity.set_error_message(error_messages)
        return self.view(template, entity)

    def insert(self):
        language_name = self.get_session('language_name')
        
        # TODO validation
        
        # session をクリアする
        self.set_session('language_id', '')
        self.set_session('language_name', '')

        return self.view('complete.html', self.__service.create(self.__user_id, language_name))

    def update(self):
        language_id = self.get_session('language_id')
        language_name = self.get_session('language_name')
        
        # session をクリアする
        self.set_session('language_id', '')
        self.set_session('language_name', '')

        entity = LanguageEntity()
        entity.set_language_id(self.__service.update(language_id, self.__user_id, language_name))
        return self.view('complete.html', entity)
    
    def delete(self):
        language_id = self.get_param('language_id')

        # session をクリアする
        self.set_session('language_id', '')
        self.set_session('language_name', '')

        entity = LanguageEntity()
        entity.set_language_id(self.__service.delete(language_id, self.__user_id))
        return self.view('complete.html', entity)    