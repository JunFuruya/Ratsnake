# -*- coding: UTF-8 -*-

from app.controller.base_controller import BaseController
from app.validator.account_title_validator import AccountTitleValidator
from app.service.account_title_service import AccountTitleService
from app.entity.account_title_entity import AccountTitleEntity

from app.helper.helper import HashHelper

'''
Account Title Controller Module
'''
class AccountTitleController(BaseController):

    def __init__(self, request):
        super().__init__(request)
        self.set_page_info('勘定科目マスタ', '勘定科目を登録・編集・削除します。', '')
        self.__user_id = self.get_login_user()
        self.__service = AccountTitleService()
        self.__validator = AccountTitleValidator()

    def index(self):
        limit = self.get_param('limit', 100)
        offset = self.get_param('offset', 0)

        self.set_session('account_title_id', '')
        self.set_session('account_title_name', '')
        self.set_session('account_title_classification_type', '')

        return self.view('./template/admin/account_titles/list.html', self.__service.getList(self.__user_id, limit, offset))
    
    def create(self):
        # TODO Factory
        entity = AccountTitleEntity()
        entity.set_account_title_name('')
        entity.set_account_title_classification_type(1)
        return self.view('./template/admin/account_titles/create.html', entity)

    def detail(self, account_title_id):
        # TODO validation
        
        self.set_session('account_title_id', account_title_id)
        return self.view('./template/admin/account_titles/detail.html', self.__service.get(self.__user_id, account_title_id))

    def edit(self, account_title_id):
        account_title_id = self.get_session('account_title_id')
        # TODO validation
        
        self.set_session('account_title_id', account_title_id)
        return self.view('./template/admin/account_titles/edit.html', self.__service.get(self.__user_id, account_title_id))
    
    def confirm(self):
        account_title_id = self.get_session('account_title_id')
        account_title_name = self.get_param('account_title_name')
        account_title_classification_type = self.get_param('account_title_classification_type')

        error_messages = self.__validator.get_error_messages(account_title_name, account_title_classification_type)
        if(len(error_messages) == 0):
            self.set_session('account_title_id', account_title_id)
            self.set_session('account_title_name', account_title_name)
            self.set_session('account_title_classification_type', account_title_classification_type)
            template = './template/admin/account_titles/confirm.html'
        else:
            template = './template/admin/account_titles/create.html'
        
        # TODO Factoryにする
        entity = AccountTitleEntity()
        entity.set_account_title_id(account_title_id)
        entity.set_account_title_name(account_title_name)
        entity.set_account_title_classification_type(account_title_classification_type)
        entity.set_error_messages(error_messages)
        return self.view(template, entity)

    def insert(self):
        account_title_name = self.get_session('account_title_name')
        account_title_classification_type = self.get_session('account_title_classification_type')

        return self.view('./template/admin/account_titles/complete.html', self.__service.create(self.__user_id, account_title_name, account_title_classification_type))

    def update(self, account_title_id):
        account_title_id = self.get_session('account_title_id')
        account_title_name = self.get_session('account_title_name')
        account_title_classification_type = self.get_session('account_title_classification_type')

        entity = AccountTitleEntity()
        entity.set_account_title_id(self.__service.update(account_title_id, self.__user_id, account_title_name, account_title_classification_type))
        return self.view('./template/admin/account_titles/complete.html', entity)
    
    def delete(self, account_title_id):
        self.set_session('account_title_id', '')
        self.set_session('account_title_name', '')
        self.set_session('account_title_classification_type', '')

        entity = AccountTitleEntity()
        entity.set_account_title_id(self.__service.delete(account_title_id, self.__user_id))
        return self.view('./template/admin/account_titles/complete.html', entity)