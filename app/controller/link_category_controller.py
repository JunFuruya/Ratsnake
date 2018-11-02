#-*- UTF-8 -*-

from app.controller.base_controller import BaseController
from app.service.link_category_service import LinkCategoryService
from app.entity.link_category_entity import LinkCategoryEntity

from app.helper.helper import HashHelper

'''
Link Category Controller Module
'''
class LinkCategoryController(BaseController):

    def __init__(self, request):
        super().__init__(request)
        self.__title = 'リンクカテゴリマスタ'
        self.__description = 'リンクを分類するためのカテゴリを登録・編集・削除します。'
        self.__notification = 'Please enter your id and password.'

        self.__service = LinkCategoryService()
        pass

    def index(self):
        user_id = 1
        limit = self.get_param('limit', 10)
        offset = self.get_param('offset', 0)

        self.set_session('link_category_id', '')

        return self.view('./template/admin/link_categories/list.html', self.__service.getList(user_id, limit, offset))
    
    def create(self):
        return self.view('./template/admin/link_categories/create.html', LinkCategoryEntity())

    def detail(self, link_category_id):
        link_categoty_id = self.get_param('link_categoty_id')
        # TODO user_id 取得する
        user_id = 1
        # TODO validation
        
        self.set_session('link_category_id', link_categoty_id)
        return self.view('./template/admin/link_categories/detail.html', self.__service.get(user_id, link_category_id))

    def edit(self, link_category_id):
        # TODO user_id 取得する
        user_id = 1
        # TODO validation
        
        self.set_session('link_category_id', link_category_id)
        return self.view('./template/admin/link_categories/edit.html', self.__service.get(user_id, link_category_id))
    
    def confirm(self):
        link_category_id = self.get_session('link_category_id')
        link_category_name = self.get_param('link_category_name')
        link_category_display_order = self.get_param('link_category_display_order')

        # TODO validation
        
        self.set_session('link_category_id', link_category_id)
        self.set_session('link_category_name', link_category_name)
        self.set_session('link_category_display_order', link_category_display_order)
        
        # TODO もっと良い設計があるはず
        entity = LinkCategoryEntity()
        entity.set_link_category_id(link_category_id)
        entity.set_link_category_name(link_category_name)
        entity.set_link_category_display_order(link_category_display_order)
        return self.view('./template/admin/link_categories/confirm.html', entity)

    def insert(self):
        link_category_name = self.get_session('link_category_name')
        link_category_display_order = self.get_session('link_category_display_order')
        
        #TODO ログイン時に取得するようにする 
        user_id = 1
        
        # TODO validation
        
        self.set_session('link_category_id', '')
        self.set_session('link_category_name', '')
        self.set_session('link_category_display_order', '')
        return self.view('./template/admin/link_categories/complete.html', self.__service.create(user_id, link_category_name, link_category_display_order))

    def update(self, link_category_id):
        link_category_id = self.get_session('link_category_id')
        link_category_name = self.get_session('link_category_name')
        link_category_display_order = self.get_session('link_category_display_order')
        #TODO ログイン時に取得するようにする 
        user_id = 1
        
        self.set_session('link_category_id', '')
        self.set_session('link_category_name', '')
        self.set_session('link_category_display_order', '')

        entity = LinkCategoryEntity()
        entity.set_link_category_id(self.__service.update(link_category_id, user_id, link_category_name, link_category_display_order))
        return self.view('./template/admin/link_categories/complete.html', entity)
    
    def delete(self, link_category_id):
        link_category_id = self.get_param('link_category_id')
        #TODO ログイン時に取得するようにする 
        user_id = 1

        self.set_session('link_category_id', '')
        self.set_session('link_category_name', '')
        self.set_session('link_category_display_order', '')

        entity = LinkCategoryEntity()
        entity.set_link_category_id(self.__service.delete(link_category_id, user_id))
        return self.view('./template/admin/link_categories/complete.html', entity)