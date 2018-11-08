# -*- UTF-8 -*-

from app.controller.base_controller import BaseController
from app.service.link_service import LinkService
from app.entity.link_entity import LinkEntity

from app.helper.helper import HashHelper

'''
Link Controller Module
'''
class LinkController(BaseController):

    def __init__(self, request):
        self.__title = 'リンク集'
        self.__description = 'リンク集を登録・編集・削除します。'
        self.__notification = 'Please enter your id and password.'
        super().__init__(request)

        self.__service = LinkService()
        pass

    def index(self):
        # TODO セッションからとる
        user_id = 1
        link_id = self.get_session('link_id')

        limit = self.get_param('limit', 10)
        offset = self.get_param('offset', 0)

        self.set_session('link_id', '')
        self.set_session('link_category_id', '')
        self.set_session('link_site_name', '')
        self.set_session('link_url', '')
        self.set_session('link_display_order', '')

        return self.view('./template/admin/links/list.html', entity=self.__service.getList(user_id, limit, offset))

    def create(self):
        # TODO セッションからとる
        user_id = 1
        # TODO validation
        entity = LinkEntity()
        entity.set_link_category_entity_list(self.__service.get_link_categories(user_id, 100 ,0).get_link_category_entity_list())
        return self.view('./template/admin/links/create.html', entity=entity)

    def detail(self, link_id):
        link_id = self.get_param('link_id')
        # TODO , user_id 取得する
        user_id = 1
        # TODO validation

        self.set_session('link_id', link_id)

        return self.view('./template/admin/links/detail.html', entity=self.__service.get(user_id, link_id))

    def edit(self, link_id):
        link_id = self.get_session('link_id')
        # TODO user_id 取得する
        user_id = 1

        return self.view('./template/admin/links/edit.html', entity=self.__service.get(user_id, link_id))

    def confirm(self):
        link_id = self.get_session('link_id')
        # TODO user_id 取得する
        user_id = 1

        link_category_id = self.get_param('link_category_id')
        link_site_name = self.get_param('link_site_name')
        link_url = self.get_param('link_url')
        link_display_order = self.get_param('link_display_order')

        # TODO validation

        self.set_session('link_id', link_id)
        self.set_session('link_category_id', link_category_id)
        self.set_session('link_site_name', link_site_name)
        self.set_session('link_url', link_url)
        self.set_session('link_display_order', link_display_order)

        # TODO もっと良い設計があるはず
        entity = LinkEntity()
        entity.set_link_id(link_id)
        entity.set_link_category_id(link_category_id)
        entity.set_link_site_name(link_site_name)
        entity.set_link_url(link_url)
        entity.set_link_display_order(link_display_order)
        return self.view('./template/admin/links/confirm.html', entity=entity)

    def insert(self):
        link_category_id = self.get_session('link_category_id')
        link_site_name = self.get_session('link_site_name')
        link_url = self.get_session('link_url')
        link_display_order = self.get_session('link_display_order')

        # TODO ログイン時に取得するようにする
        user_id = 1

        # TODO validation

        self.set_session('link_category_id', '')
        self.set_session('link_site_name', '')
        self.set_session('link_url', '')
        self.set_session('link_display_order', '')

        return self.view('./template/admin/links/complete.html', entity=self.__service.create(user_id, link_category_id, link_site_name, link_url, link_display_order))

    def update(self, link_id):
        link_id = self.get_session('link_id')
        link_category_id = self.get_session('link_category_id')
        link_site_name = self.get_session('link_site_name')
        link_url = self.get_session('link_url')
        link_display_order = self.get_session('link_display_order')
        # TODO ログイン時に取得するようにする
        user_id = 1

        sell.set_session('link_id', '')
        sell.set_session('link_category_id', '')
        sell.set_session('link_site_name', '')
        sell.set_session('link_url', '')
        sell.set_session('link_display_order', '')

        entity = linkEntity()
        entity.set_link_id(link_id)
        return self.view('./template/admin/links/complete.html', entity=entity)

    def delete(self, link_id):
        link_id = self.get_param('link_id')
        # TODO ログイン時に取得するようにする
        user_id = 1

        self.set_session('link_id', '')

        entity = linkEntity()
        entity.set_link_id(self.__service.delete(user_id, link_id))
        return self.view('./template/admin/links/complete.html', entity=entity)