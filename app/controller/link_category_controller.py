#-*- UTF-8 -*-

from app.controller.base_controller import BaseController
from app.service.link_category_service import LinkCategoryService
from app.entity.link_category_entity import LinkCategoryEntity

from app.helper.helper import HashHelper

'''
Link Category Controller Module
'''
class LinkCategoryController(BaseController):

    def __init__(self):
        super().__init__(request)
        self.__title = 'リンクカテゴリマスタ'
        self.__description = 'リンクを分類するためのカテゴリを登録・編集・削除します。'
        self.__notification = 'Please enter your id and password.'

        self.__service = LinkCategoryService()
        pass

    def index(self):
        # TODO もっと良い方法を考える
        limit = request.query.get('limit')
        limit = limit if limit is not None else 10
            
        # TODO もっと良い方法を考える
        offset = request.query.get('offset')
        offset = offset if offset is not None else 0

        session[HashHelper.hexdigest('link_category_id')] = ''
        session[HashHelper.hexdigest('link_category_name')] = ''

        return self.view('./template/admin/link_categories/list.html', self.__service.getList(limit, offset))
    
    def create(self):
        return self.view('./template/admin/link_categories/create.html', LinkCategoryEntity())

    def detail(self, link_category_id):
        
        # TODO user_id 取得する
        user_id = 1
        # TODO validation
        
        session = request.environ.get('beaker.session')
        session[HashHelper.hexdigest('link_category_id')] = link_category_id
        session.save()
        
        entity = self.__service.get(user_id, link_category_id)
        return self.view('./template/admin/link_categories/detail.html', entity)

    def edit(self, link_category_id):
        link_category_id = session.get(HashHelper.hexdigest('link_category_id'), False)
        # TODO user_id 取得する
        user_id = 1
        
        entity = self.__service.get(user_id, link_category_id)
        return self.view('./template/admin/link_categories/edit.html', entity)
    
    def confirm(self):
        link_category_id = session.get(HashHelper.hexdigest('link_category_id'), False)
        link_category_name = request.forms.get('link_category_name')

        # TODO validation
        
        session[HashHelper.hexdigest('link_category_name')] = link_category_name
        
        # TODO もっと良い設計があるはず
        entity = LinkCategoryEntity()
        entity.set_link_category_id(link_category_id)
        entity.set_link_category_name(link_category_name)
        return self.view('./template/admin/link_categories/confirm.html', entity)

    def insert(self):
        link_category_name = session.get(HashHelper.hexdigest('link_category_name'), False)
        
        #TODO ログイン時に取得するようにする 
        user_id = 1
        
        # TODO validation
        
        session[HashHelper.hexdigest('link_category_id')] = ''
        session[HashHelper.hexdigest('link_category_name')] = ''

        entity = self.__service.create(user_id, link_category_name)
        return self.view('./template/admin/link_categories/complete.html', entity)

    def update(self):
        link_category_id = session.get(HashHelper.hexdigest('link_category_id'), False)
        link_category_name = session.get(HashHelper.hexdigest('link_category_name'), False)
        #TODO ログイン時に取得するようにする 
        user_id = 1
        
        session[HashHelper.hexdigest('link_category_id')] = ''
        session[HashHelper.hexdigest('link_category_name')] = ''

        entity = LinkCategoryEntity()
        entity.set_link_category_id(self.__service.update(link_category_id, user_id, link_category_name))
        return self.view('./template/admin/link_categories/complete.html', entity)
    
    def delete(self):
        link_category_id = request.forms.get('link_category_id')
        #TODO ログイン時に取得するようにする 
        user_id = 1

        session[HashHelper.hexdigest('link_category_id')] = ''
        session[HashHelper.hexdigest('link_category_name')] = ''

        entity = LinkCategoryEntity()
        entity.set_link_category_id(self.__service.delete(link_category_id, user_id))
        return self.view('./template/admin/link_categories/complete.html', entity)
