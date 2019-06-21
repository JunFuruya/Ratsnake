# -*- coding: UTF-8 -*-

from app.controller.base_controller import BaseController
from app.validator.link_category_validator import LinkCategoryValidator
from app.service.link_category_service import LinkCategoryService
from app.entity.link_category_entity import LinkCategoryEntity

from app.helper.log_helper import LogHelper

'''
Link Category Controller Module
'''
class LinkCategoryController(BaseController):

    def __init__(self, request):
        super().__init__(request)
        self.set_page_info('リンクカテゴリマスタ', 'リンクを分類するためのカテゴリを登録・編集・削除します。', '')
        self.__user_id = self.get_login_user()
        self.__service = LinkCategoryService()
        self.__validator = LinkCategoryValidator()
        self.__logger = LogHelper()

    def index(self):
        limit = self.get_param('limit', 10)
        offset = self.get_param('offset', 0)

        self.set_session('link_category_id', '')
        
        entity = self.__service.getList(self.__user_id, limit, offset)
        try:
            entity = self.__service.getList(self.__user_id, limit, offset)
        except:
            self.__logger.critical('DB Error')
            # TODO 例外をスロー
            
        return self.view('./template/admin/link_categories/list.html', entity=entity)
    
    def create(self):
        return self.view('./template/admin/link_categories/create.html', LinkCategoryEntity())

    def detail(self, link_category_id):
        link_categoty_id = self.get_param('link_categoty_id')

        try:
            entity = self.__service.get(self.__user_id, link_category_id)
        except:
            self.__logger.critical('DB Error')
            # TODO 500 例外をスロー
        
        if entity is None:
            self.__logger.error('不正な遷移')
            # TODO 404 例外をスロー
        
        self.set_session('link_category_id', link_categoty_id)
        return self.view('./template/admin/link_categories/detail.html', entity=entity)

    def edit(self, link_category_id):
        # TODO validation
        
        self.set_session('link_category_id', link_category_id)
        return self.view('./template/admin/link_categories/edit.html', self.__service.get(self.__user_id, link_category_id))
    
    def confirm(self):
        link_category_id = self.get_session('link_category_id')
        link_category_name = self.get_param('link_category_name')
        link_category_display_order = self.get_param('link_category_display_order')

        error_messages = self.__validator.get_error_messages(link_category_name, link_category_display_order)
        if(len(error_messages) == 0):
            self.set_session('link_category_id', link_category_id)
            self.set_session('link_category_name', link_category_name)
            self.set_session('link_category_display_order', link_category_display_order)
            template = './template/admin/link_categories/confirm.html'
        else:
            template = './template/admin/link_categories/create.html'
        
        # TODO Factoryにする
        entity = LinkCategoryEntity()
        entity.set_link_category_id(link_category_id)
        entity.set_link_category_name(link_category_name)
        entity.set_link_category_display_order(link_category_display_order)
        entity.set_error_message(error_messages)
        return self.view(template, entity)

    def insert(self):
        link_category_name = self.get_session('link_category_name')
        link_category_display_order = self.get_session('link_category_display_order')
                
        error_messages = self.__validator.get_error_messages(link_category_name, link_category_display_order)

        if(len(error_messages) == 0):
            self.set_session('link_category_id', '')
            self.set_session('link_category_name', '')
            self.set_session('link_category_display_order', '')
            template = './template/admin/link_categories/confirm.html'

            try:
                entity = self.__service.create(self.__user_id, link_category_name, link_category_display_order)
            except:
                self.__logger.critical('DB Error')
                # TODO 500 例外をスロー

        else:
            template = './template/admin/link_categories/create.html'

        return self.view(template, entity=entity)

    def update(self, link_category_id):
        link_category_id = self.get_session('link_category_id')
        link_category_name = self.get_session('link_category_name')
        link_category_display_order = self.get_session('link_category_display_order')

        error_messages = self.__validator.get_error_messages(link_category_name, link_category_display_order)
        if(len(error_messages) == 0):
            self.set_session('link_category_id', '')
            self.set_session('link_category_name', '')
            self.set_session('link_category_display_order', '')

            entity = LinkCategoryEntity()
            entity.set_link_category_id(self.__service.update(link_category_id, self.__user_id, link_category_name, link_category_display_order))
        else:
            self.__logger.critical('不正な遷移')
            # TODO 404 例外をスロー
            
        return self.view('./template/admin/link_categories/complete.html', entity)
    
    def delete(self, link_category_id):
        link_category_id = self.get_param('link_category_id')

        self.set_session('link_category_id', '')
        self.set_session('link_category_name', '')
        self.set_session('link_category_display_order', '')

        entity = LinkCategoryEntity()
        try:
            entity.set_link_category_id(self.__service.delete(link_category_id, self.__user_id))
        except:
            self.__logger.critical('DB Error')
            # TODO 500 例外をスロー

        return self.view('./template/admin/link_categories/complete.html', entity)