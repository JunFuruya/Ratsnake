#-*- UTF-8 -*-

from app.controller.base_controller import BaseController
from app.entity.base_web_entity import BaseWebEntity

from app.helper.helper import HashHelper

'''
Word Controller Module
'''
class IndexController(BaseController):
    def __init__(self, request):
        super().__init__(request)
        self.set_page_info('管理画面トップ', '', '')
        self.__user_id = self.get_login_user()
        pass

    def index(self):
        return self.view('./template/index.html', entity=BaseEntity())
