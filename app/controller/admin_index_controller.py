#-*- UTF-8 -*-

from app.controller.base_controller import BaseController
from app.entity.index_entity import IndexEntity

from app.helper.helper import HashHelper

'''
Word Controller Module
'''
class AdminIndexController(BaseController):
    def __init__(self, request):
        super().__init__(request)
        self.set_page_info('Hideout管理画面', '', '')
        self.__user_id = self.get_login_user()

    def index(self):
        return self.view('./template/admin/index.html', entity=IndexEntity())