# -*- coding: UTF-8 -*-

from app.controller.base_controller import BaseController
from app.validator.link_validator import LinkValidator
from app.service.link_service import LinkService
from app.entity.link_entity import LinkEntity
from app.entity.link_list_entity import LinkListEntity

from app.helper.log_helper import LogHelper

'''
Link Controller Module
'''
class LinkController(BaseController):
    RECORD_NUM_PER_PAGE = 30;
    
    def __init__(self, request):
        super().__init__(request)
        # TODO デザイン変更＋必要な文言のみ表示する
        self.set_page_info('リンク集', 'リンク集を登録・編集・削除します。', 'リンク集を登録・編集・削除します。')
        self.__user_id = self.get_login_user()
        self.__service = LinkService()
        self.__validator = LinkValidator()
        
        pass

    def index(self):
        page = int(self.get_param('p', 1))

        error_messages = self.__validator.get_index_error_message(page)
        if (len(error_messages) > 0):
            entity.set_error_messages(error_messages)
            page = 1

        offset = self.get_offset(self.RECORD_NUM_PER_PAGE, page)
        entity = self.__service.getList(self.__user_id, self.RECORD_NUM_PER_PAGE, offset)
        entity.set_current_page(page)

        self.set_session('link_id', '')
        self.set_session('link_category_id', '')
        self.set_session('link_site_name', '')
        self.set_session('link_url', '')
        self.set_session('link_display_order', '')
                
        return self.view('./template/admin/links/list.html', entity=entity)

    def create(self):
        entity = LinkEntity()
        # TODO limit に暫定で9999件を設定する。仕様を検討する
        entity.set_link_category_entity_list(self.__service.get_link_categories(self.__user_id ,9999 ,0).get_link_category_entity_list())
        return self.view('./template/admin/links/create.html', entity=entity)

    def detail(self, link_id):
        link_id = self.get_param('link_id')
        # TODO validation

        self.set_session('link_id', link_id)

        return self.view('./template/admin/links/detail.html', entity=self.__service.get(self.__user_id, link_id))

    def edit(self, link_id):
        link_id = self.get_session('link_id')
        entity = self.__service.get(self.__user_id, link_id)
        entity.set_link_category_entity_list(self.__service.get_link_categories(self.__user_id, 100 ,0).get_link_category_entity_list())
        return self.view('./template/admin/links/edit.html', entity=entity)

    def confirm(self):
        link_id = self.get_session('link_id')

        link_category_id = self.get_param('link_category_id')
        link_site_name = self.get_param('link_site_name')
        link_url = self.get_param('link_url')
        link_display_order = self.get_param('link_display_order')

        error_messages = self.__validator.get_error_messages(link_site_name, link_url, link_display_order)
        if(len(error_messages) == 0):
            self.set_session('link_id', link_id)
            self.set_session('link_category_id', link_category_id)
            self.set_session('link_site_name', link_site_name)
            self.set_session('link_url', link_url)
            self.set_session('link_display_order', link_display_order)
            template = './template/admin/links/confirm.html'
        else:
            template = './template/admin/links/create.html'

        link_category_entity = self.__service.get_link_category(self.__user_id, link_category_id)

        # TODO Factory class
        entity = LinkEntity()
        entity.set_link_id(link_id)
        entity.set_link_category_id(link_category_id)
        entity.set_link_category_name(link_category_entity.get_link_category_name())
        entity.set_link_site_name(link_site_name)
        entity.set_link_url(link_url)
        entity.set_link_display_order(link_display_order)
        entity.set_error_messages(error_messages)
        return self.view(template, entity=entity)

    def insert(self):
        link_category_id = self.get_session('link_category_id')
        link_site_name = self.get_session('link_site_name')
        link_url = self.get_session('link_url')
        link_display_order = self.get_session('link_display_order')

        # TODO validation

        self.set_session('link_category_id', '')
        self.set_session('link_site_name', '')
        self.set_session('link_url', '')
        self.set_session('link_display_order', '')
        
        try:
            entity = self.__service.create(self.__user_id, link_category_id, link_site_name, link_url, link_display_order)
        except:
            entity = LinkEntity()
            entity.set_link_category_entity_list(self.__service.get_link_categories(self.__user_id, 100 ,0).get_link_category_entity_list())
            log = LogHelper()
            log.error('DB Error')
        
        return self.view('./template/admin/links/complete.html', entity=entity)

    def update(self):
        link_id = self.get_session('link_id')
        link_category_id = self.get_session('link_category_id')
        link_site_name = self.get_session('link_site_name')
        link_url = self.get_session('link_url')
        link_display_order = self.get_session('link_display_order')

        self.set_session('link_id', '')
        self.set_session('link_category_id', '')
        self.set_session('link_site_name', '')
        self.set_session('link_url', '')
        self.set_session('link_display_order', '')

        entity = LinkEntity()
        entity.set_link_id(self.__service.update(self.__user_id, link_id, link_category_id, link_site_name, link_url, link_display_order))
        return self.view('./template/admin/links/complete.html', entity=entity)

    def delete(self):
        link_id = self.get_param('link_id')

        self.set_session('link_id', '')

        entity = LinkEntity()
        entity.set_link_id(self.__service.delete(self.__user_id, link_id))
        return self.view('./template/admin/links/complete.html', entity=entity)