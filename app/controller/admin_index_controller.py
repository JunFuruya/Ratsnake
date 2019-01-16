# -*- coding: UTF-8 -*-

from app.controller.base_controller import BaseController
from app.entity.index_entity import IndexEntity

'''
Word Controller Module
'''
class AdminIndexController(BaseController):
    def __init__(self, request):
        super().__init__(request)
        self.set_page_info('管理サイトメニュー', '', '')
        self.__user_id = self.get_login_user()

    def index(self):
        return self.view('./template/admin/index.html', entity=IndexEntity())